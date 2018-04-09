#!/bin/bash
#this sh use for start sucai_api
nohup gunicorn -w 2 -b 0.0.0.0:8900 run:app &
