cd /sys/kernel/debug/tracing/
cat available_tracers
echo ':mod:amdgpu' > set_ftrace_filter
echo function_graph > current_tracer
