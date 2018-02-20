# Tornodes
Fetch list of tornodes every 30 minutes from https://www.dan.me.uk/tornodes

**Scripted in Python 2.7.11**

## Required Modules
* w3lib
* requests
* schedule

## Installation Instructions
1. Go to your python directory > Scripts
2. Open Command Prompt
3. **run command:** pip install w3lib requests schedule
4. Now you can run get_nodes.py script

## General Guidelines
* This script fetch list of tornodes every 30 minutes according to support of website.
* List fetched is stored in file tornodes.txt which is overwritten every 30 minutes with new nodes from website.
* Feed this tornodes.txt into your security solution such as web proxies/gateways/SIEM to monitor your network for TOR related activities.

**Cheers!**
Twitter: @ngrovyer
