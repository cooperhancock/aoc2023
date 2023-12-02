#!/bin/bash

name="day$1"
mkdir $name
cd $name
touch "$name.py"
touch "$name.txt"
touch "${name}test.txt"
