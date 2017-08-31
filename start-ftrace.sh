cd /sys/kernel/debug/tracing/
cat available_tracers
echo ':mod:amdgpu' > set_ftrace_filter
echo 0 > tracing_on
echo 1 > tracing_thresh
#echo function_duration > current_tracer
echo function_graph > current_tracer
#echo function_duration > current_tracer
echo 1 > tracing_on
