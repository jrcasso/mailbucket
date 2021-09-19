#!/bin/bash
PROCESS_NAMES=( postfix qmgr pickup )

for process in "${PROCESS_NAMES[@]}"; do
    check=$(ps ax | grep -v grep | grep -c "$process")
    if [ "$check" = 0 ]; then
        echo "FAIL: $process not running!"
        exit 1
    else
        echo "PASS: $process running!"
    fi;
done
