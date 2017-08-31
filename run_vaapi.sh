export LIBVA_DRIVER_NAME=gallium
gst-launch-1.0 filesrc location='/home/rpatlega/AES4kRioTestClip_H264_3840x2160_40Mbps_HP@L5.2_60fps.mp4' ! qtdemux ! h264parse ! vaapidecode ! vaapisink
