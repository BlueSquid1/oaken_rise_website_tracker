#!/usr/bin/env bash
set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
rm -rf ${SCRIPT_DIR}/venv
python3 -m venv ${SCRIPT_DIR}/venv
${SCRIPT_DIR}/venv/bin/pip3 install -r ./requirements.txt