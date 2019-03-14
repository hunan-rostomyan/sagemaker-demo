#!/bin/bash

payload=$1
content=${2:-application/json}

# CURL
#curl --data-binary @${payload} -H "Content-Type: ${content}" -v http://localhost:8080/invocations
# httpie
http POST http://localhost:8080/invocations < $payload