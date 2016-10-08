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

up: | build ; docker-compose up -d && $(MAKE) configure

configure:
	sleep 5
	curl 'http://admin:admin@localhost:3000/api/datasources' \
		-X POST \
		-H 'Content-Type: application/json;charset=UTF-8' \
		--data-binary \
		'{"name":"graphite","type":"graphite","url":"http://graphite:8080","access":"proxy","isDefault":true}'

down: ; docker-compose down
