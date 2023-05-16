The AirBnB Clone Project

AirBnB Logo
Project Overview

This project is the first part of an AirBnB clone project, where we built the backend using Python and interfaced it with a console application using the cmd module. The data generated is stored in a JSON file, and we can access it using the JSON module in Python.
Command Interpreter Description

The interface of the application is similar to the Bash shell, except that it has a limited number of accepted commands defined solely for the AirBnB website. The command line interpreter serves as the frontend of the web app where users can interact with the backend developed with Python OOP programming.

The following commands are available:

    show
    create
    update
    destroy
    count

With the implementation of the command line interpreter coupled with the backend and file storage system, the following actions can be performed:

    Creating new objects (e.g., a new User or a new Place)
    Retrieving an object from a file, a database, etc.
    Performing operations on objects (count, compute stats, etc.)
    Updating attributes of an object
    Destroying an object

Getting Started

To get started with this project, you need to clone the repository from GitHub. It contains the simple shell program and all its dependencies.

bash

git clone https://github.com/ndandax/AirBnB_clone.git

After cloning the repository, you will have a folder called AirBnB_clone, which will contain several files that allow the program to work.

    /console.py: The main executable of the project, which is the command interpreter.

    models/engine/file_storage.py: Class that serializes instances to a JSON file and deserializes a JSON file to instances

    models/__ init __.py: A unique FileStorage instance for the application

    models/base_model.py: Class that defines all common attributes/methods for other classes.

    models/user.py: User class that inherits from BaseModel

    models/state.py: State class that inherits from BaseModel

    models/city.py: City class that inherits from BaseModel

    models/amenity.py: Amenity class that inherits from BaseModel

    models/place.py: Place class that inherits from BaseModel

    models/review.py: Review class that inherits from BaseModel

Usage

The program can work in two different modes: Interactive and Non-interactive.

In Interactive mode, the console will display a prompt (hbnb), indicating that the user can write and execute a command. After running a command, the prompt will appear again and wait for a new command. This can go on indefinitely as long as the user does not exit the program.

bash

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

In Non-interactive mode, the shell will need to be run with a command input piped into its execution so that the command runs as soon as the shell starts. In this mode, no prompt will appear, and no further input will be expected from the user.

bash

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
