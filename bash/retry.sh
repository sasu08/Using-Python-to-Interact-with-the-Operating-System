#!/bin/bash

# Ejecutar ./retry.sh ./random-exit.py

n=0
commando=$1
while ! $command && [ $n -le 5]; do
    sleep $n
    ((n=n+1))
    echo "Retry #$n"
done;