# Moodle Version Checker

This python script show [moodle](https://moodle.org) version by reading the `version.php` file under the specified directory.

```txt
dir
├── moodle-1
│   └── version.php  <-- target file
├── moodle-1-data
├── moodle-2
│   └── version.php  <-- target file
├── moodle-2-data
```

## Requirements

```bash
pip3 install prettytable
```

## Usage

```bash
./moodle-version-checker.py <dir>
```
