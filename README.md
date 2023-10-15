# HashArtisan
A very simple command-based hash dictionary creator for MD5 and Sha-256

---

## Important usage disclaimer:

This project is currently a work in progress, I cannot guarantee that it will work in every given situation.

This application was developed for the ethical testing of a given system's security, I do not support its usage on any system you are not authorized to access by the owner.

---

## Installation:

To utilize this app's latest build simply download or clone this repository.

HashArtisan requires the latest Python version and the alive_progress package which may be installed
via this command on your console terminal of choice:

```shell
pip install alive_progress
```

---

## Usage

Go into the src folder and open your console terminal of choice. This is a command prompt-based application and cannot be interacted with in any other way.
Here is a list of the arguments that the application takes:

| Command | Description |
| --- | --- |
| -h / --help | Displays a brief description of the usage of the app |
| -v / --version | Displays the current build version |
| -d / --display | Makes it so that the results are displayed on the console terminal (requires -c, -a and an encryption flag) |
| -w / --write | Saves the results onto the specified file (much faster than display) (requires -c, -a, an encryption flag and a -f) |
| -a / --alphabet | Requires a text argument corresponding to the available alphabets (see -h) (has to be paired with -d or -w)  |
| -c / --complexity | Requires a whole number value corresponding to the length of the desired dictionary words (has to be paired with -d or -w) |
| -f / --file | Requires a file path that will become the -w output (has to be paired with -w) |
| -sha / --sha | Indicates that the dictionary to be created will be of Sha-256 encryption (needs to have -w or -d) |
| -md5 / --md5 | Indicates that the dictionary to be created will be of MD5 encryption (needs to have -w or -d) |


