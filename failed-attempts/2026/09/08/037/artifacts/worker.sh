#!/bin/bash
# worker: worker.sh N "a|b"  ->  "a|b|count"
N=$1
line=$2
a="${line%%|*}"; b="${line#*|}"
aa=$(echo "$a" | tr ',' ' '); bb=$(echo "$b" | tr ',' ' ')
v=$(./output/artifacts/enum2 $N $aa $bb)
echo "$line|$v"
