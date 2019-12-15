import argparse
import datetime

import requests

import pjm_urls

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
today = datetime.datetime.now()

# fetch public subscription key
response = requests.get('http://dataminer2.pjm.com/config/settings.json')
settings = response.json()
key = settings['subscriptionKey']

# create header with subscription key
headers = {
    'Ocp-Apim-Subscription-Key': key,
}

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--url", "-u", help="set url for data extraction")
parser.add_argument("--output", "-o", help="set filename to output csv")

# read arguments from the command line
args = parser.parse_args()

# check for --width
if args.url:
    url = pjm_urls.urls[args.url]
    print("set url to %s" % url)
else:
    exit()

# fetch data at URL
response = requests.get(url, headers=headers)

if args.output:
    output = args.output
else:
    output = args.url + "-" + today.strftime("%Y%m%d%H%M%S") + ".csv"

print("store output to %s" % output)
file = open(output, 'w+', newline='\n')
file.write(response.text)
