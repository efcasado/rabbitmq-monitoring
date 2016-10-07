###========================================================================
### File: Makefile
###
### Author(s):
###   - Enrique Fernandez <efcasado@gmail.com>
###========================================================================
.PHONY: all build up down

##== Targets ==============================================================
all: | up

build: ; docker-compose build

up: | build ; docker-compose up -d

down: ; docker-compose down
