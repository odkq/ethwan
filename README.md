# ethwan

Simple setup to make a linux box a routing device

## Requirements

- Docker Enginer 17.3+
- Docker Compose 1.13+

## Usage

the ethwan bash script is a wrapper around the more common docker-compose
operations. It configures the docker-compose with the host ethernet device.

Build and running `` ./ethwan -e=<ethernet interface> start `` (Example: `` ./ethwan -e=eth0 start `` )

Stopping: `` ./ethwan -e=eth0 stop ``

Removing all images and networks: ``./ethwan delete``

Help in-line: ``./ethwan -h``

Open shell in running container through docker-compose exec ``./ethwan shell``

Ssh client is installed to be able to connect to any connected client. Leases
are at /var/lib/misc/dnsmasq.leases

## Web monitor
