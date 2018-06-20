#!/usr/bin/env python

import glob, re, hashlib, sys, os

root_dir = ""
if len(sys.argv) > 1:
    root_dir = sys.argv[1]
else:
    exit()


def find_conflicts(root_dir):
    files = []
    print("Searching for conflicted files in {}...".format(root_dir))
    path = os.path.join(root_dir.rstrip("\\").rstrip("/"), "**", "*SFConflict*")
    for file_conflict in glob.iglob(path, recursive=True):
        file_original = re.sub(r"\s\(SFConflict\s.+\)", "", file_conflict)
        files.append({"original": file_original, "conflict": file_conflict})
    return files


def md5(file):
    hasher = hashlib.md5()
    with open(file, "rb") as open_file:
        content = open_file.read()
        hasher.update(content)
    return hasher.hexdigest()


def categorize_files(files):
    changed_files = []
    unchanged_files = []
    for file in files:
        if file["original_md5"] == file["conflict_md5"]:
            unchanged_files.append(file)
        else:
            changed_files.append(file)
    return unchanged_files, changed_files


def calc_checksums(files):
    files_total = len(files)
    print("Calculating Checksum for {} files (original and conflict):".format(files_total))
    for file in files:
        # time.sleep(0.01)
        print("\r\t=> Progress: {}/{}".format(files.index(file) + 1, files_total), end="")
        file["original_md5"] = md5(file["original"])
        file["conflict_md5"] = md5(file["conflict"])


def print_result(unchanged_files, changed_files):
    print("\n\t=> Result:")
    print("\t\t {} files with matching MD5".format(len(unchanged_files)))
    for file in unchanged_files:
        print("\t\t\t - {}".format(file["original"]))

    print("\t\t {} files with different MD5".format(len(changed_files)))
    for file in changed_files:
        print("\t\t\t - {}".format(file["original"]))

    if len(unchanged_files) > 0:
        print("\nFiles that can be safely deleted (the conflicted file matches the original one):")
        for file in unchanged_files:
            print("\t\t - {}".format(file["conflict"]))

files = find_conflicts(root_dir)
unchanged_files = []

# Calculate checksums if there are any conflicted files and print the results.
if len(files) > 0:
    calc_checksums(files)
    unchanged_files, changed_files = categorize_files(files)
    print_result(unchanged_files, changed_files)
else:
    print("No conflicted files found.")

# Ask if the conflicted files (that have the same MD5sum as the original ones) should be deleted
if len(unchanged_files) > 0:
    should_delete = input("\nDo you want to delete the unchanged conflict files? y/n [n] ")
    if should_delete.lower() == "y":
        print("Deleting {} files:\n".format(len(unchanged_files)))
        for file in unchanged_files:
            print("\t\t - deleted {}".format(file["conflict"]))
            os.remove(file["conflict"])
        print("\nFinished deleting the {} unchanged conflict files.".format(len(unchanged_files)))
