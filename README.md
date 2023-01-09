# Car Rental Task

## Table of Contents

- [Changelog](#changelog-)
- [Introduction](#introduction---the-projects-aim-)
- [Technologies and tools](#technologies-and-tools-)
    - [Technologies](#technologies)
    - [Databases](#databases)
    - [Tools](#tools)
- [Release Versions](#release-versions-)
- [Launch](#launch-)
    
## Changelog ➡

- 2023/01/02 - initial commit
- 2023/01/03 - "same_day" and "next_day" branches
  - added description about possible solutions and its branches
- 2023/01/05 - added information about local branches and keyring
  

## Introduction - the project's aim 🎯

This is Python 3 project to generate dummy services data for fictive car rental. 

## Technologies and tools 👨‍💻

In our project we are using following technologies and tools:

### Technologies

- Python programming language in version 3.9.

### Databases

- MariaDB
### Tools

- Git
- Keyring for store confidential data

## Release Versions 🔨

Currently working on version where if service is needed for particular car then it happens immediately after car is 
returned to the rental (in the "same_day"). It is impossible to rent this car again before necessary services.
This solution is being developed on the "same_day" branch. It is planned to develop also version where it is possible
to rent car immediately after previous rental without necessary service. In this scenario service will happen "next_day"
after car will be returned to the rental if there will be one day break between rentals. This solution will be developed
on "next_day" branch. 

## Launch 🚀

Simply run main.py file from main branch or use development branches: "same_day" or "next_day". Both has also its local
version.