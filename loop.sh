#!/bin/sh
while true
do

    for i in rain sun cloud four three two one zero
do
    curl http://localhost:5000/icon/ture/$i
    sleep 5
done

done

