FROM python:3.9.1-alpine3.13 AS base

LABEL maintainer="Pedro Rodrigues <csixteen@protonmail.com>"

ENV PYTHONFAULTHANDLER=1 \
	PYTHONHASHSEED=random \
	PYTHONUNBUFFERED=1

RUN addgroup -S web && adduser -S web -G web

WORKDIR /app

FROM base AS builder

ENV PIP_DEFAULT_TIMEOUT=100 \
	PIP_DISABLE_PIP_VERSION_CHECK=1 \
	PIP_NO_CACHE_DIR=1 \
	POETRY_VERSION=1.1.4

RUN apk add --no-cache gcc make libffi-dev python3-dev musl-dev openssl-dev cargo
RUN pip install "poetry==$POETRY_VERSION"
RUN python -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

FROM base AS final

USER web

COPY --chown=web:web --from=builder /venv /venv
COPY --chown=web:web docker-entrypoint.sh wsgi.py ./
CMD ["./docker-entrypoint.sh"]
