while true;  date; do echo Pass - ;cat $1 | grep Pass | wc -l; echo Fail - ;cat $1 | grep Fail | wc -l; echo -------;sleep 60; done
