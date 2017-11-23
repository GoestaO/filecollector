# filecollector CLI

Tool to support analysis and solution of incidents.

## Setup

To install the requirements and setup the skript run the following command
```
$ sudo -H pip install setuptools
path/to/filecollector/python$ pip install --editable .
```

After you executed this, the `filecollector` command should be available everywhere.
```
path/to/anywhere$ filecollector --help
```

### Activate autocompletion

You have two option to enable autocompletion.
1. Add `eval "$(_FILECOLLECTOR_COMPLETE=source filecollector)"` to your `~/.bashrc`
2. Use the activation script

### Activation script

The above activation example will always invoke your application on startup. This might be slowing down the shell activation time significantly if you have many applications. Alternatively, you could also ship a file with the contents of that, which is what Git and other systems are doing.

This can be easily accomplished:

```
_filecollector_COMPLETE=source filecollector > filecollector-complete.sh
```

And then you would put this into your `~/.bashrc` instead:

```
. path/to/filecollector/python/filecollector-complete.sh
```


