# seafile-conflict-resolver
From time to time, when using seafile, it happens that conflicts occur. The `seafile-conflict-solver` is a script that recursively searches for conflicted files and compares the MD5sum of the different versions. If the checksums match, the conflicted files can be safely deleted. `seafile-conflict-solver` will delete the conflicted duplicates automatically, if you want to.

## Install

```bash
wget https://raw.githubusercontent.com/bstie/seafile-conflict-resolver/master/seafile-conflict-resolver.py
chmod +x seafile-conflict-resolver.py
sudo mv seafile-conflict-resolver.py /usr/local/bin
```

## Usage

Install the script like mentioned above, clone the repo or download the file `seafile-conflict-resolver.py`.  

Then execute it with the path to the seafile directory as parameter:

If you installted it to `/usr/local/bin`
```bash
seafile-conflict-resolver.py <path-to-seafile-directory>
```

If you did not install it to `/usr/local/bin`
```bash
python seafile-conflict-resolver.py <path-to-seafile-directory>
```


