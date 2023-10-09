#!/bin/bash

uvicorn -w 2 -b :8080 -t 300 -k uvicorn.workers.UvicornWorker  --reload main:app