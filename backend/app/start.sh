#!/bin/bash

gunicorn -w 2 -b :$1 -t 300 -k uvicorn.workers.UvicornWorker  --reload main:app