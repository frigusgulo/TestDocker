#!/bin/bash

docker compose up

#!/bin/bash

build_docker() {
    docker compose build
}

start_app () {
    docker compose up
}