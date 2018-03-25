#!/bin/bash

echo "Starting script to accumulate speed test result, default at every 10 mins"

n=1
name="$(date)"
filename="log$(date +'%d%m%y')"
touch "${filename}.txt"

echo "${name}"

while [ $n -le 23 ]
do
  echo "------ Start Of Test " $n "-------" >> "${filename}.txt"
  date >> "${filename}.txt"
  speedtest-cli >> "${filename}.txt"
  echo "------ End Of Test " $n "-------" >> "${filename}.txt"
  sleep 10m
  ((n++))
done

echo "Running Python Script "
python "SpeedGraph.py" "${filename}"
