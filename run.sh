#!/bin/sh

# Check if python3 exists
if command -v python3 >/dev/null 2>&1; then
    python program.py
    exit
fi

echo "Python3 not found. Attempting installation..."

# Detect package manager and install
if command -v apt >/dev/null 2>&1; then
    sudo apt update
    sudo apt install -y python3

elif command -v dnf >/dev/null 2>&1; then
    sudo dnf install -y python3

elif command -v pacman >/dev/null 2>&1; then
    sudo pacman -Sy --noconfirm python

elif command -v zypper >/dev/null 2>&1; then
    sudo zypper install -y python3

else
    echo "Unsupported distribution. Please install Python manually."
    exit 1
fi

# Verify installation
if command -v python3 >/dev/null 2>&1; then
    echo "Python3 installed successfully!"
    python program.py
else
    echo "Installation failed."
fi