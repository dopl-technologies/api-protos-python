# api-protos-python
API protos built in python

## Build
```shell
# Generate python files
$ docker build -t dopltechnologies/api-protos-python --build-arg CACHEBUST="$(curl https://api.github.com/repos/dopl-technologies/api-protos/commits/main 2>&1 | grep '"date"' | tail -n 1)" -f build.Dockerfile .

# Copy generated files to local dir
$ docker cp $(docker create --rm dopltechnologies/api-protos-python:latest):/output/. ./dopltech/protos/
```