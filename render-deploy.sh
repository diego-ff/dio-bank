#!/sh/bin/env bash
set -e

poetry run flash --app src.app db upgrade
poetry run gunicorn src.wsgi:app
