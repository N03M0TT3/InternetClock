# InternetClock
A simple web crawler that fetches the date & time from the web

It has been developed in order to actualize the date and time in linux, hence why the format is a bit strange

# Warning
Careful, it has been designed to fetch the date and time from France, but this can be easily adapted.

# Actualizing at home
If you want to use this script to actualize the date and time of your own computer, you can build a bash script that looks roughly like this:

```
    ddate=`python $HOME/path_to_directory/clock.py`

    sudo date $ddate
```
Then you need to export your directory in which you stored this script to the PATH environment variable. To do that, you need to add to your .bashrc and/or .zshrc this line:
```
    export PATH=$PATH:/path_to_directory
```


