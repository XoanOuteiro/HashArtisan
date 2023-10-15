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

``` shell
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

### A simple example

Opening a shell window in the same folder as hashart.py. This command will give us all 0-9 numbers encrypted with Sha-256:
```shell
python hashart.py -d -c 1 -a DIG -sha
```
An alternative would be:

``` shell
python hashart.py --display --complexity 1 --alphabet DIG --sha
```

The *--display* area makes the results be outputted to the console terminal, the *--complexity 1* area indicates that the length of the dictionary results will be 1, the *--alphabet DIG* indicates that we will be using the DIGIT charset to make combinations, finally the *--sha* area indicates that we will be encrypting those combinations via Sha-256

The result is as follows:
``` shell
on 1: 0 -> 5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9
on 2: 1 -> 6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
on 3: 2 -> d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35
on 4: 3 -> 4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce
on 5: 4 -> 4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a
on 6: 5 -> ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d
on 7: 6 -> e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683
on 8: 7 -> 7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451
on 9: 8 -> 2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3
on 10: 9 -> 19581e27de7ced00ff1ce50b2047e7a567c76b1cbaebabe5ef03f7c3017bb5b7
Progress |████████████████████████████████████████| 10/10 [100%] in 0.0s (710.96/s)
```

The first column (starting with on) represents the iteration, this data is omitted when writing into a file. The second column is the dictionary combination, and the third column is said combination hash on the given encryption flag digest

---

## List of current alphabets:

Depending on the length of the used alphabet dictionary production times may change radically. Always remember --complexity values change production time exponentially.

| Abbreviation | Name | Length |
| --- | --- | --- |
| EN_FULL | English Full | 57 |
| EN_LOW | English Lowercase | 26 |
| EN_UP | English Uppercase | 26 |
| DIG | Digits | 10 |

