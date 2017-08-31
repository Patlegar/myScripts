# This needs to be done from the parent process which will run this script
#cd $1
#source setup-env.sh

# Please refer to the Vulkan SDK manual. Please run the folowing command 
# for the selected Vulkan SDK to set $VULKAN_SDK
# from <VulkanSDK> folder run 
# source setup-env.sh

git clone https://github.com/McNopper/Vulkan.git
cd Vulkan/
sudo apt-get install libx11-xcb-dev libxrandr-dev
export C_INCLUDE_PATH=$VULKAN_SDK/include
export CPLUS_INCLUDE_PATH=$VULKAN_SDK/include
export LIBRARY_PATH=$VULKAN_SDK/lib
python3 get_binaries.py
python3 create_master_CMakeLists.py
cmake .
cmake --build .
cd VKTS_Binaries
