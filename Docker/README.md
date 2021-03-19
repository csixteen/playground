Docker Playground
=================

Here you'll find a `docker-compose` configuration file and two subdirectories: `nginx` and `myapp`.

Under `nginx` you'll find a simple `Dockerfile` and uses the default `nginx` image and copies a custom configuration to the resulting Docker image.

Under `myapp`, you'll find a simple Python application built using [FastAPI](https://fastapi.tiangolo.com/). I also used [Poetry](https://python-poetry.org/) for packaging and dependency management and some other bells and whistles. The resulting Docker image is fairly small, since I'm using multi-stage Docker builds.

# Dependencies

- [Docker](https://www.docker.com/)

# Building

```
$ docker-compose build
```

# Testing

```
$ curl -i localhost:8080
HTTP/1.1 200 OK
Server: nginx/1.19.8
Date: Fri, 19 Mar 2021 14:30:14 GMT
Content-Type: application/json
Content-Length: 26
Connection: keep-alive

{"message":"Hello, world"}
```
