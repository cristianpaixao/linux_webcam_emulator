#!/bin/bash

echo "Installing Node Requirements to Bodypix Server"
cd bodypix_server/
npm install

echo "Installing Python Requirements to Webcam Emulators"
cd ../linux_webcam_emulator/
pip install -r requirements.txt
