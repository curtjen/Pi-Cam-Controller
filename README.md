# Pi-Cam-Controller

## Purpose

Provide a controller for digital camera(s) facilitated through a Raspberry Pi. This was also made to work with running the Django app, [davis1410's django_cam_controller](https://github.com/davis1410/django_cam_controller "davis1410/django_cam_controller"), on a raspberry pi.
This installs the following libraries and dependencies:

- dh-autoreconf (utility for compiling packages from source files)
- gphoto2 (tool for controlling digital cameras)
- x264 (codec for compiling video from images)
- ffmpeg (utility for compiling video)

Even though this project was originally created to be used with a Django project, it can still be used for controlling a digital camera independently via CLI.

## Installation

Run `python install_linux_packages.py` from the project's directory. This will create the necessary directories, clone the needed repos and install and compile all needed libraries.

## Usage

After installation, you should be able to connect your digital camera and run via command line.

You can see if your digital camera is supported here: [Projects :: libgphoto2 :: supported cameras](http://gphoto.sourceforge.net/proj/libgphoto2/support.php)

Configuring for video recording: [Doc :: Remote controlling cameras](http://www.gphoto.org/doc/remote/)

Useful gphoto2 commands: [The gPhoto2 Reference (the man pages)](http://gphoto.sourceforge.net/doc/manual/ref-gphoto2-cli.html)