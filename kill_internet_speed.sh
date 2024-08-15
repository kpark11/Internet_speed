#!/bin/bash

kill $(ps ax | grep check_internet_speed.py | awk '{print $1}' | head -n 1)
kill $(ps ax | grep livePlot.py | awk '{print $1}' | head -n 1)

