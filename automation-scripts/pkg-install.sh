#!/bin/bash
# This Script takes the desired package name from user and installs it.

read -p "Enter the package name : " package_name

echo "Updating and upgrading the system first & then Installting the package $package_name"

sudo apt update -y

sudo apt upgrade -y

sudo apt install $package_name -y


