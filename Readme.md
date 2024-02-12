# Scripts to convert/post videos to YouTube

## Overview

Given a directory containing a set of video files in `mp4` format, the command `publish-youtube.sh` script will do what the name implies:
* Find the file with the latest date. Say it's called "video.mp4".
* Generate an output file name of the form `video-converted.mp4`.
* Use [ffmpeg](www.fmpeg.org) to do the conversion using optimal format for YouTube, using your GPU if available.
* Upload the Video to YouTube with details provided on the command line.

## Command Line Arguments

* TODO

## Requirements

* ffmpeg
* Python 3.0 or greater
* A Google API key that has write access to your YT account

## Usage

* TODO

## Testing

* TODO
 
## Further work

Complete this Readme file.

