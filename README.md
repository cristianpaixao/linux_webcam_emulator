# Linux Webcam Emulator
A emulator to add background &amp; effects to webcam on linux.

This is still in work in progress. Feel free to contribute.


## Setup

You need first to install all requirements running bellow command in root path:

```bash
  $ chmod+x setup.sh
  $ ./setup.sh
```

## Running

You need first to start the bodypix server:

```bash
# if you are in root path
  $ cd bodypix_server
  $ npm run server # if you are using NPM
  $ yarn server # if you are using Yarn
```

After you need to open a new terminal session and run command bellow:


```bash
# if you are in root path
  $ cd linux_webcam_emulator
  $ python app.py
```
