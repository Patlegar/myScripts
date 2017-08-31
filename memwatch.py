#!/usr/bin/python
#author david.mao@amd.com 12/08/2015

from fcntl import ioctl
import re
import os
import errno
import time
from optparse import OptionParser
import signal

def lastLine(file_in):
    last = os.popen("tail -n 1 %s" % file_in).read()
    return last

class vram(object):
    def __init__(self, file_in):
        self.patternStr = "man size:([0-9]*) pages, ram usage:([0-9]*)MB, vis usage:([0-9]*)MB"
        self.pattern = re.compile(self.patternStr)
        self.file_in = file_in
        self.total_size = 0.0
        self.used_size = 0.0
        self.free_size = 0.0
        self.used_vis_size = 0.0
        self.update()
    def get_params(self):
        return ["vram total", "vram used", "visible used", "vram free"]
    def get_values(self):
        self.update()
        return [str(self.total_size), str(self.used_size), str(self.used_vis_size), str(self.free_size)]
    def update(self):
        desc = lastLine(self.file_in)
        result = self.pattern.match(desc)
        if result:
            self.total_size = float(result.group(1)) * 4 / 1024 
            self.used_size = float(result.group(2))
            self.used_vis_size = float(result.group(3))
        self.free_size = self.total_size - self.used_size
    def display(self):
        self.update()
        print "vram total               = ", self.total_size, " MB"
        print "vram used                = ", self.used_size, " MB"
        print "vram used visible        = ", self.used_vis_size, " MB"
        print "vram available           = ", self.free_size, " MB"
class gtt(object):
    def __init__(self, file_in):
        self.patternStr = "total: ([0-9]*), used ([0-9]*) free ([0-9]*)"
        self.pattern = re.compile(self.patternStr)
        self.file_in = file_in
        self.total_size = 0.0
        self.used_size = 0.0
        self.free_size = 0.0
        self.update()
    def get_params(self):
        return  ["vram total", "vram used", "vram free"]
    def get_values(self):
        self.update()
        return [str(self.total_size), str(self.used_size), str(self.free_size)]
    def update(self):
        desc = lastLine(self.file_in)
        result = self.pattern.match(desc)
        if result:    
            self.total_size = float(result.group(1)) *  4 / 1024 
            self.used_size = float(result.group(2)) * 4 / 1024
            self.free_size = float(result.group(3)) * 4 / 1024
    def display(self):
        self.update()
        print "remote total             = ", self.total_size, " MB"
        print "remote used              = ", self.used_size, " MB"
        print "remote available         = ", self.free_size, " MB"
class sys(object):
    def __init__(self, file_in):
        self.file_in = file_in
        self.total_size = 0.0
        self.used_size = 0.0
        self.free_size = 0.0
        self.update()
    def get_params(self):
        return ["system total", "system used", "system free"]
    def get_values(self):
        self.update()
        return [str(self.total_size), str(self.used_size), str(self.free_size)]
    def update(self):
        try:
            self.fd = open(self.file_in, 'r')
        except IOError:
            print 'cannot open', self.file_in 
            print "please check whether you can access proc file system\n"
            exit()

        lines = self.fd.readlines(1)
        for line in lines:
            total = re.match(r"MemTotal:[ \t]*([0-9]*) kB", line)
            free = re.match(r"MemAvailable:[ \t]*([0-9]*) kB", line)
            if total:
                self.total_size = float(total.group(1)) / 1024
            elif free:
                self.free_size = float(free.group(1)) / 1024
                self.used_size = self.total_size - self.free_size
                break
            else:
                next
        self.fd.close()
    def display(self):
        self.update()
        print "system memory total      = ", self.total_size, " MB"
        print "system memory used       = ", self.used_size, " MB"
        print "system memory available  = ", self.free_size, " MB"

class activity(object):
    def __init__(self, file_in):
        self.patternStr = "GPU load:[ \t]*([0-9]*) \%"
        self.pattern = re.compile(self.patternStr)
        self.file_in = file_in
        self.perf = 0
        self.update()
    def get_params(self):
        return  ["GPU Activity"]
    def get_values(self):
        self.update()
        return [str(self.perf)]
    def update(self):
        desc = lastLine(self.file_in)
        result = self.pattern.match(desc)
        if result:    
            self.perf= float(result.group(1))
    def display(self):
        self.update()
        print "GPU Activity = ", self.perf, " %"

class GpuInfo(object):
    def __init__(self, prefix, log_file):
        self.log_file = log_file
        if self.log_file:
            try:
                self.fd = open(log_file, 'w')
            except IOError:
                print 'cannot open', log_file
                print "please check whether you can create file in current location\n"
                exit()
        else:
            self.fd = 0
        self.initialize();
    def initialize(self):
        self.vram = vram(prefix + '/dri/0/amdgpu_vram_mm')
        self.gtt = gtt(prefix + '/dri/0/amdgpu_gtt_mm')
        self.sys = sys('/proc/meminfo');
        self.activity = activity(prefix + '/dri/0/amdgpu_pm_info')
        if self.fd:
            line = "" 
            params = self.vram.get_params()
            for param in params:
                line += param + ","
            params = self.gtt.get_params()
            for param in params:
                line += param + ","
            params = self.sys.get_params()
            for param in params:
                line += param + ","
            params = self.activity.get_params()
            for param in params:
                line += param + ","
            line = line[:-1] + "\n"
            self.fd.write(line)
    def display(self):
        if self.fd:
            line = ""
            params = self.vram.get_values()
            for param in params:
                line += param + ','
            params = self.gtt.get_values()
            for param in params:
                line += param + ','
            params = self.sys.get_values()
            for param in params:
                line += param + ','
            params = self.activity.get_values()
            for param in params:
                line += param + ','
            line = line[:-1] + '\n'
            self.fd.write(line)
        else:
            os.system('clear')
            self.vram.display()
            self.gtt.display()
            self.sys.display()
            self.activity.display()
    def close(self):
        if self.fd:
            self.fd.close()
            exit()
        else:
            exit()
        

tick = 0.1
log_file = ""
prefix = "/sys/kernel/debug"
parser = OptionParser("%prog : Help info")
parser.add_option("-t", "--tick", dest="tick", type="float",  help="the frequency of sampling data", metavar="TICK")
parser.add_option("-l", "--log", dest="log", type="string", help="log the data to csv file", metavar="FILE")
parser.add_option("-d", "--debugfs", dest="prefix", type="string", help="the path to your mounted debugfs", metavar="DEBUGFS")

def signal_handler(signum, frame):
    print "get the signal\n"
    gpu.close()
    os.system("umount "+ path);

def setup_debugfs(prefix):
    try:
        if os.path.isdir(prefix) == True:
            pass
        else:
            os.makedirs(prefix)
    except:
            print "cannot create ", prefix
            exit()
    try:
        if os.path.isdir(prefix+"/dri/0"):
            pass
        else:
            os.system("mount -t debugfs /dev/nodev " + prefix)
    except:
        print "cannot mount debugfs to ", prefix
        exit()


signal.signal(signal.SIGINT, signal_handler)

(options, args)  = parser.parse_args()
if options.tick:
    tick = options.tick
if options.log:
    log_file = options.log
if options.prefix:
    prefix = options.prefix

setup_debugfs(prefix)
gpu = GpuInfo(prefix, log_file)

while 1:
    gpu.display()
    time.sleep(tick)

