# Scripts to convert/post videos to YouTube

## Overview

Given a directory containing a set of video files in `mp4` format, the `convert-and-push` script will do what the name implies:
* Find the file with the latest date
* Generate an output file name of the form `filename-converted.mp4`
* Use [ffmpeg](www.fmpeg.org) to convert o optimal format for YouTube, using your GPU if available
* Upload the Video to YouTube with details provided on the command line

## Requirements

* ffmpeg
* Python 3.0 or greater
* A Google API key that has write access to your YT account

## Usage

TODO

## Testing

TODO

## Further work

Complete this Readme file.

