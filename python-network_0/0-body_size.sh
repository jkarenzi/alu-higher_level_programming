#!/bin/bash 
# a script that takes in a url and displays the content 
curl -sI "$1" | grep 'Content-Length'| cut -d " " -f2
