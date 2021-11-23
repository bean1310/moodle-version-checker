#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os, re
from prettytable import PrettyTable

def getVersion(path: str) -> str:
    result = None
    versionFilePath = path + "/version.php"
    if not os.path.isfile(versionFilePath):
        return result
    with open(versionFilePath) as f:
        line = f.readlines()
        versionLine = [s for s in line if '$release' in s]
        for s in versionLine:
            result = re.search(r'(\d|\.|\+)+', s).group()
    
    return result


def main():
    if len(sys.argv) != 2:
        print("Usage: " + sys.argv[0] + " <dir>")
        exit()

    dirPath = sys.argv[1]

    if not os.path.isdir(dirPath):
        print("Error: " + dirPath + " directory is not found.")
        exit()
    
    dirPath = os.path.abspath(dirPath)

    moodleDirs = []
    
    for path in os.listdir(dirPath):
        subDirAbsPath = dirPath + "/" + path
        if os.path.isdir(subDirAbsPath):
            moodleDirs.append(subDirAbsPath)

    table = PrettyTable()
    table.field_names = ['Directory', 'Version']
    
    for moodleSystemDir in moodleDirs:
        version = getVersion(moodleSystemDir)
        if version == None:
            table.add_row([moodleSystemDir, 'Not Found'])
        else:
            table.add_row([moodleSystemDir, version])

    print(table.get_string())


if __name__ == '__main__':
    main()
