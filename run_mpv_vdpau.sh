
while true; do
mpv  --hwdec=vdpau -vo vdpau -fs $1 &
sleep $2
kill -s SIGINT `pidof mpv`
mpv --hwdec=vdpau -vo vdpau -fs $1 &
sleep $2
kill -s SIGINT `pidof mpv`
mpv --hwdec=vdpau -vo vdpau -fs $1&
sleep $2
kill -s SIGINT `pidof mpv`
mpv --hwdec=vdpau -vo vdpau -fs $1&
sleep $2
kill -s SIGINT `pidof mpv`
mpv --hwdec=vdpau -vo vdpau -fs $1&
sleep $2
kill -s SIGINT `pidof mpv`
mpv --hwdec=vdpau -vo vdpau -fs $1&
sleep $2
kill -s SIGINT `pidof mpv`
done;


