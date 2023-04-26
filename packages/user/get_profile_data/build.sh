#!/bin/bash

set -e

virtualenv virtualenv
source virtualenv/bin/activate
python3 -m pip install -r requirements.txt
deactivate