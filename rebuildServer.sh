#!/bin/bash
shopt -s extglob 
rm -rfv !("openapi.yaml"|"rebuildServer.sh")
openapi-generator-cli generate -g python-flask -i openapi.yaml
sudo python3 setup.py install
python3 -m openapi_server