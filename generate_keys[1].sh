#!/bin/bash
openssl genrsa -out mykey.pem 2048
openssl req -x509 -new -key mykey.pem -out mycert.pem -days 365 -subj "/CN=StudentSign"
