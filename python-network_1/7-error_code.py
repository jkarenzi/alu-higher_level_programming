#!/usr/bin/python3
""" this module sends a request
    and gets a response with a specific
    status code
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print("Regular request")
