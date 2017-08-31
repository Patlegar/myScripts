cd /sys/kernel/debug/tracing/
echo 0 > tracing_on
#echo duration-proc >trace_options
cp trace $1 
