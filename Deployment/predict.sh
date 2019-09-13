#!/bin/bash

payload='payload.csv'
#content=${2:-text/csv}
content='text/csv'

curl --data-binary @${payload} -H "Content-Type: ${content}" -v http://localhost:8080/invocations
