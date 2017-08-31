cd /sys/kernel/debug/tracing/
cat available_tracers
echo ':mod:amdgpu' > set_ftrace_filter
echo 0 > tracing_on
echo function_graph > current_tracer
echo 1 > tracing_on
$1
echo 0 > tracing_on
cp trace $2
