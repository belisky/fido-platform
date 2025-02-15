#!/bin/bash
k3d cluster delete --all
k3d registry delete --all
docker network rm fido-exam