lttng create
lttng enable-channel my-channel -u 
lttng enable-channel my-channel -k 
lttng enable-event --kernel --all --channel my-channel
lttng enable-event --userspace --all --channel my-channel
lttng start
