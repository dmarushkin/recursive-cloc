import os
import sys
import json
import subprocess
from pathlib import Path

def run_cloc(directory):
    cmd = ['cloc', directory, '--json']
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode != 0:
        print(f"Error running cloc on directory {directory}: {result.stderr}")
        return None

    return json.loads(result.stdout)

def filter_languages(languages, lang_filter):
    return {lang: {'files':stats['nFiles'],'code':stats['code']} for lang, stats in languages.items() if lang in lang_filter}

def process_directory(path, lang_filter):
    cloc_data = run_cloc(str(path))
    if cloc_data:
        filtered_languages = filter_languages(cloc_data, lang_filter)
        print(f"{path}")
        for lang, loc in filtered_languages.items():
            files = loc['files']
            code = loc['code']
            print(f"   {lang}: files - {files}, lines - {code}")

def recursive_cloc(path, lang_filter, depth, max_depth):
    if depth > max_depth:
        return

    for root, dirs, files in os.walk(path):
        process_directory(Path(root), lang_filter)
        for dir_name in dirs:
            sub_path = os.path.join(root, dir_name)
            recursive_cloc(sub_path, lang_filter, depth + 1, max_depth)
        break

def main():
    if len(sys.argv) < 4:
        print(f"Usage: {sys.argv[0]} <directory> <lang1,lang2,...> <max_depth>")
        sys.exit(1)

    directory = sys.argv[1]
    lang_filter = set(sys.argv[2].split(','))
    max_depth = int(sys.argv[3])

    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        sys.exit(1)

    recursive_cloc(directory, lang_filter, 0, max_depth)

if __name__ == "__main__":
    main()
