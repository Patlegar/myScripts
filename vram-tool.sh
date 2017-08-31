while true; do {
date
echo "-------------------------------------------------------"
printf "\nCPU-info:\n"
echo  -n "no of processors = ";cat /proc/cpuinfo | grep "processor" | wc -l; 
cat /proc/cpuinfo | grep "cpu MHz" | sort -u;  
echo "-------------------------------------------------------"
cat /sys/kernel/debug/dri/0/amdgpu_vram_mm | grep total | awk '{ print  "\n Total Video Memory: " $2*4/1024 " MB, " "Used Memory: "  $4*4/1024 " MB," "Free Memory: " $6*4/1024 " MB"}';
echo "-------------------------------------------------------"
 printf "\nGPU Clock:\n"
 cat /sys/kernel/debug/dri/0/amdgpu_pm_info
echo "-------------------------------------------------------"
 printf "\nGTT MEM:\n"
cat /sys/kernel/debug/dri/0/amdgpu_gtt_mm | grep -i total | awk '{ print  "\n Total GTT  Memory: " $2*4/1024 " MB, " "Used Memory: "  $4*4/1024 " MB," "Free Memory: " $6*4/1024 " MB"}';
echo "-------------------------------------------------------"
echo " Process Information:"
echo -n " Process : "; echo -n $2; echo -n " : Memory usage = ";cat /proc/`pidof $2`/status | grep -i VmSize | awk '{ print $2 " KB"}';
echo -n " Process : Xorg : Memory usage = "; cat /proc/`pidof Xorg`/status | grep -i VmSize| awk '{ print $2 " KB"}';
echo "======================================================="

# echo "Process Imformation:"
# cat /proc/`pidof gst-launch-1.0`/status | grep -i VmSize;
# cat /proc/`pidof gst-launch-1.0`/status | grep -i State;

sleep $1

tput cup 0 0; tput el; tput el1; printf "\33[2J" 
}
done
