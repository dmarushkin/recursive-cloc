# recursive-cloc

Wrapper on cloc to run recursevly on supfolders and get birds eye view for big projects.
You can set depth and set of languages that you want see in results.

## Install

You need cloc, python3 and this script

```
apt install cloc

```

## Usage

```
python3 recursive-cloc.py <directory> <lang1,lang2,...> <max_depth>
```

Example:

```
python3 recursive-cloc.py ./code_folder Java,TypeScript,Dockerfile,YAML 3

code_folder
    Java: files - 7004, lines - 274016
    TypeScript: files - 3218, lines - 131476
    YAML: files - 654, lines - 48003
    Dockerfile: files - 25, lines - 229
code_folder/ci
    YAML: files - 5, lines - 357
    Dockerfile: files - 1, lines - 57
code_folder/ci/builder-image
    Dockerfile: files - 1, lines - 57
    YAML: files - 1, lines - 20

```
