#pprof  --nodecount=200 --focus=glxSwapBuffer --callgrind myXwinPlayer myXwin.prof > ls.callgrind
pprof  --nodecount=200 --focus=$3 --callgrind $1 $2 > ls.callgrind
kcachegrind ls.callgrind
