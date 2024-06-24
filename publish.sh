#!/bin/bash

echo "Publishing build to Raspberry Pi..."
DIST_FILE=$(find ./dist -name "yardbot-*.tar.gz" -print -quit)
scp -P 22 "update.sh" "${DIST_FILE}" bcampolo@raspberrypi4.local:/opt/yardbot/update/
