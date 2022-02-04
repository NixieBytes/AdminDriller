
# AdminDriller

AdminDriller is an open source tool designed to automate fetching from a target site's admin panel using brute force in the wordlist.

## Installation

Download the project:


```python
git clone https://github.com/NixieBytes/AdminDriller
```

Enter the project folder and install:

```python
cd AdminDriller && pip install -r requirements.txt
```

## Usage

Run AdminDrilller:

```python
sudo python2 admindriller.py -u https://exmaple.com
```

Check all paths with php extension:

```python
sudo python2 admindriller.py -u https://exmaple.com --type php
```
## Features

- Check the robots.txt file, see if there is any useful information in it
- Locates admin webpage using over 900+ lines of dictionary list
- Supports php, asp and html extensions


