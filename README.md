# seafile-conflict-resolver
From time to time, when using seafile, it happens that conflicts occur. The `seafile-conflict-solver` is a Script that recursively searches for conflicted files and compares the MD5sum of the different versions. If the Checksums match, the conflicted files can be safely deleted. `seafile-conflict-solver` will delete the conflicted duplicates automatically, if you want to.

## Usage

Clone the repo or download the file `seafile-conflict-resolver.py`.  

Then execute it with the path to the seafile directory as parameter:
```bash
python seafile-conflict-resolver.py <path-to-seafile-directory>
```


