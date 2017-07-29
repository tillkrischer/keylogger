# Keylogger

recording and playback for keyboard presses

## Dependencies
- xte (xautomation)
- xmodmap (xorg-xmodmap)
- xinput (xorg-xinput)

## Usage
```
usage: keylogger.py [-h] inputid output

Record Keypresses. Ctrl+q to stop recording

positional arguments:
  inputid     input device id (xinput list)
  output      output file

optional arguments:
  -h, --help  show this help message and exit

```

```
usage: keyplayback.py [-h] [--speed SPEED] input

Record Keypresses.

positional arguments:
  input                 input file

optional arguments:
  -h, --help            show this help message and exit
  --speed SPEED, -s SPEED
                        relative speed of playback
```
