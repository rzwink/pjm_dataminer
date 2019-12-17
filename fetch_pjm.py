import argparse
import datetime

import requests
import tablib

from get_pjm_url import get_pjm_url, get_pjm_list
from get_subscription_headers import get_subsription_headers

# create header with subscription key
headers = get_subsription_headers()

# initiate the parser
parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--url", "-u", help="set url for data extraction")
parser.add_argument("--output", "-o", help="set filename to output csv")
parser.add_argument("--format", "-f", help="set format for output", default="csv")
parser.add_argument("--list", "-l", help="output list of all urls", default=False, dest='list', action='store_true')
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

# read arguments from the command line
args = parser.parse_args()

if args.list is True:
    list = get_pjm_list()
    print("|url|description|")
    print("|---|---|")
    for l in list:
        print(f"|{l['name']}|{l['description']}|")
    # print(list)
    exit()

# check for --url
if args.url:
    url = get_pjm_url(args.url)
    print("set url to %s" % url)
else:
    exit()

# fetch data at URL
response = requests.get(url, headers=headers)

if args.output:
    output = args.output
else:
    output = args.url + "-" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "." + args.format

if args.format == "raw":
    print(response.json())
else:
    data = tablib.Dataset(headers=response.json()['items'][0].keys())
    for item in response.json()['items']:
        data.append(item.values())

    if args.format in ["csv", "json", "yaml"]:
        with open(output, 'w', newline='') as f:
            f.write(data.export(args.format))
    elif args.format == "xls":
        with open(output, 'wb') as f:
            f.write(data.export(args.format))
    elif args.format == "stdout":
        print(data.csv)
    else:
        exit("Invalid output format")