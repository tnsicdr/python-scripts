#!/usr/bin/env python3

import sys, argparse, unicodedata
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("file_path", type=Path)

p = parser.parse_args()

if p.file_path.exists():
  with open(p.file_path, "r+") as file:
    lines = file.readlines()

    for line in lines:
      normalized = unicodedata.normalize('NFKC', line).encode('utf8', errors='ignore').decode()
      print(f"Line: {line}")
      print(f"Normalization: {normalized}")
      line = normalized
    
    file.seek(0)
    file.truncate()
    file.writelines(lines)
    file.close()
    sys.exit("File Normalized")
else:
  sys.exit("File Not Found")