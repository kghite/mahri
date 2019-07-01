#!/bin/bash
echo Running Mahri Startup

# Auto update rpi branch
cd mahri && git pull origin rpi
echo Updated Git Repo

# Start robot scripts
echo Finished Mahri Startup
