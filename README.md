## Dockerized speech to text.

### Description

Transcribe a given audio file into text, auto-detecting the input language

### Usage

To use the docker image, first pull the image using

`docker pull jumpst3r/speech2text`

And then execute 
```
docker run -it --rm -v /FULL_PATH_TO/audio.mp3:/input/audio.mp3 -v /FULL_PATH_TO_OUTPUT_FOLDER/:/output/ jumpst3r/speech2text sh /input/script.sh /input/audio.mp3 /output/
```

where `/FULL_PATH_TO/audio.mp3` corresponds to the input audio file.

The output consists of:

- A text file containing the transcribed audio.

The docker image is also compatible with [DIVAServices](https://github.com/lunactic/DIVAServices) a web-based framework providing streamlined access to DOI methods.

### Sources / Comments

Uses public (unofficial) google-speech API and as such might be limited in terms of numbers of numbers of words to be transcribed.
