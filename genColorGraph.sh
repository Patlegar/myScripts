pprof  --nodecount=200 --callgrind myXwinPlayer $1 > ls.callgrind
kcachegrind ls.callgrind
