#!/bin/bash
# displays methods
curl -sI "$1" -X OPTIONS | grep "Allow" | cut -c 8-
