#to be run from the linux-stable folder
# $1 - kernel version for which admgpu.ko module needs to install

#for compilation of kernel code with 10 cores
#make -j10

make kernelrelease
#rm /lib/modules/4.4.11+/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko 
#cp drivers/gpu/drm/amd/amdgpu/amdgpu.ko /lib/modules/4.4.11+/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko 
#update-initramfs -c -k 4.4.11+
rm /lib/modules/$1/kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko 
cp drivers/gpu/drm/amd/amdgpu/amdgpu.ko /lib/modules/$1//kernel/drivers/gpu/drm/amd/amdgpu/amdgpu.ko 
update-initramfs -c -k $1 
