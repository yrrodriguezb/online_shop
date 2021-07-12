#!/bin/bash

set -eo pipefail
shopt -s nullglob

mysql_service_ready() {
python << END
import sys
from MySQLdb import _mysql

try:
    _mysql.connect(
        host='${MYSQL_HOST}',
        user='${MYSQL_USER}',
        passwd='${MYSQL_PASSWORD}',
        db='${MYSQL_DATABASE}'
    )
except:
    sys.exit(-1)
sys.exit(0)

END
}
until mysql_service_ready; do
  >&2 echo 'Waiting for MYSQL to become available.'
  sleep 1
done
>&2 echo 'MySQL is available'


exec "$@"