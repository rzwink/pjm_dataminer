# PJM data miner scripts to make exporting data easier

## Install

### Install Python3 + Pip + Virtualenv
```
virtualenv venv -p python3
. ./venv/bin/activate
pip install -r requirements.txt
```

### Look at the pjm_urls.py script for valid urls
This file contains a key:value mapping of "url" to the actual url.  These urls come from the data that populates the 
Explore Data link found on these pages:
http://dataminer2.pjm.com/feed/hrl_load_metered/definition
Go to the page, click on explore data.  In google chrome 

1. launch the "inspect" tool, 
2. select the network tab, 
3. Click download csv
4. Copy the link to the pjm_urls.py 

### Run the data collection script
```
python fetch_pjm_csv.py -u pnode
python fetch_pjm_csv.py -u ops_sum_prev_period
python fetch_pjm_csv.py -u hrl_load_metered
python fetch_pjm_csv.py -u solar_gen
```
optionally add -o output.csv to override filename
