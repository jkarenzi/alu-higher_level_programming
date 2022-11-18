#!/bin/bash
# display size of body
curl -sI $1 | grep Content-Length | tail -c 4
