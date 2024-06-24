#!/bin/bash
YARDBOT_DIR=/opt/yardbot
YARDBOT_DIST=$(find "${YARDBOT_DIR}/update" -name "yardbot-*.tar.gz" -print -quit)

echo "Checking for updates..."
if [ -f "${YARDBOT_DIST}" ]; then
  echo "Uninstalling Yard Bot..."
  pip uninstall -y yardbot --break-system-packages

  echo "Installing Yard Bot..."
  pip install "${YARDBOT_DIST}" --break-system-packages

  echo "Cleaning up..."
  rm "${YARDBOT_DIST}" 
fi

echo "Starting Yard Bot..."
~/.local/bin/yardbot
