#!/usr/bin/env bash
apt-get update
apt-get install software-properties-common -y
add-apt-repository ppa:deadsnakes/ppa
apt-get update
apt-get install python3.7 -y