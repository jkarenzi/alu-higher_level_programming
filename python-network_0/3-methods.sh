#!/bin/bash
# a script that gets all the allowed methods 
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2-
