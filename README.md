# gitTools
A collection of gui based versions of the git command's. This tool has only been tested on debian and requires that python be installed before attempting installation. This tool should still work (for the most part) with any operating system however you cannot install with the shortcuts unless your os is that of debian; This is only because the installation of the program will attempt to install the shortcuts in a specific location that may not exist on other operating systems. 

## Status
This project is still in progress and is in development.

## Todo
    - [4/5] Add single commands
        - [x] Add a pull gui and shortcut.
        - [x] Add a push gui and shortcut.
        - [x] Add a status gui and shortcut.
        - [x] Add a commit gui and shortcut.
            - [x] Add custom messages to commits.
        - [ ] Convert all scripts into modules for importing use.
    - [0/4] Add mass commands
        - [ ] Pull
        - [ ] Push
        - [ ] Status
        - [ ] Commit
    - [4/23] Add every command in some way
        - [x] Pull
        - [x] Push
        - [x] Status
        - [x] Commit
        - [ ] Clone
        - [ ] Init
        - [ ] Add
        - [ ] Move
        - [ ] Reset
        - [ ] Remove
        - [ ] Bisect
        - [ ] Grep
        - [ ] Log
        - [ ] Show
        - [ ] Status
        - [ ] Branch
        - [ ] Checkout
        - [ ] Diff
        - [ ] Merge
        - [ ] Rebase
        - [ ] Tag
        - [ ] Fetch
        - [ ] Help


## Instructions for Installation
- Installing (No Shortcuts)
    1. Download or clone this repository.
    2. This program is actually ready right out of the box so long as python is installed.
        - If python isnt installed then goto https://www.python.org/downloads/ to find out how to install it.
        - If python is installed then inside this reposition you will find several directorys labeled things like "push", "pull", etc; These directorys contain script.py files that when run will do their respective console functions.

- Installing (With Shortcuts)

    1. Inside this repository you will find a file inside the update directory called script.py, run it.
    2. This script will automatically search for your home directory, if it...
        - Does find it then it will ask you to verify if it is indeed your home directory.
        - Does NOT find it then it will ask you to manually search for it.
    3. It will ask you if you would like to install/update the shortcuts, press yes.
    4. That's all unless you got a message stating that the installation failed.
        - Please feel free to make any comments based on any exceptions that may be raised throughout the program. I will try to help you sort through them if possible.

## Instructions for Updating
- Updating with either shortcuts or no shortcuts only differs slightly.
    1. Pull changes from github for this repository
        - Use the pull script.py or the "git pull" command.
    2. Only do these steps if you have the shortcut verion.
        1. Click Applications > Github > Git Tools Updater
        2. Follow the same steps as [ Installing (With Shortcuts) ]
    3. Your done, git has automatically updated all of the script.py functions, they are ready to use.

## Instructions for Uninstalling
- If you did not install the shortcuts then you can simply delete the directorys containing this repository.
- If you did install the shortcuts then you will need to follow these steps.
    - Manual uninstallation
        1. The files for the shortcuts are located at ~/.local/share/applications/ simply look for the files labeled "Git_**.desktop" where ** is the name of the git function.
        2. The files for the categorys are located at ~/.config/menus/applications-merged/ simply look for the file labeled "git.menu" and delete it. (Do this after you delete all the application shortcuts, as it is easier to check under Applications > Github to check if you missed any of the shortcut files.)
        3. Delete your local version of this repository.
    - Automatic uninstallation
        1. Do the same thing as updating or installing this program and simply say no when it asks you to install/update this program.
        2. Then say yes if prompted to uninstall this program.
            - If you did not get prompted then the program did not detect that it had shortcuts installed.
        3. Delete your local version of this repository.