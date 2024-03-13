#!/bin/sh
docker build -t j30v/django_2024 ./web/.
docker push j30v/django_2024

docker build -t j30v/api_2024 ./api/.
docker push j30v/api_2024

az container create --resource-group RG_VANGANSBERGJ --file deploy.yaml