#!/bin/sh

set -eu -o pipefail -o errexit -o nounset

. /venv/bin/activate

exec gunicorn                         \
     -w 4                             \
     --max-requests=2000              \
     --max-requests-jitter=400        \
     -k uvicorn.workers.UvicornWorker \
     --bind 0.0.0.0:8080              \
     --forwarded-allow-ips='*'        \
     wsgi:app
