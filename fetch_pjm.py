import argparse
import datetime
import logging

import coloredlogs
import requests
import tablib

from get_pjm_url import get_pjm_list
from get_pjm_url import get_pjm_url
from get_subscription_headers import get_subsription_headers

# create logger with 'fetch_pjm'
logger = logging.getLogger("fetch_pjm")
logger.setLevel(logging.DEBUG)
coloredlogs.install()

# initiate the parser to interpret command line arguments
parser = argparse.ArgumentParser()

# add long and short arguments
parser.add_argument(
    "--url", "-u", help="set url key for data extraction. exp. solar_gen, pnode, etc."
)
parser.add_argument("--output", "-o", help="set filename to output")
parser.add_argument(
    "--format",
    "-f",
    help="set format for output",
    choices=["csv", "json", "xls", "stdout"],
    default="csv",
)
parser.add_argument(
    "--list",
    "-l",
    help="output list of all urls",
    default=False,
    dest="list",
    action="store_true",
)
parser.add_argument("--version", action="version", version="%(prog)s 1.0")

# read arguments from the command line
args = parser.parse_args()

# create header with subscription key
headers = get_subsription_headers()
logger.info(f"Fetch subscription header {headers}")

# show a list of all available data feeds if --list is passed
if args.list is True:
    list = get_pjm_list()
    print("|url|display name and description|")
    print("|---|---|")
    for l in list:
        print(f"|{l['name']}|*{l['displayName']}* {l['description']}|")
    exit()

# check for --url and exit if not found
if args.url:
    # This gets the actual URL based on the URL key passed
    url = get_pjm_url(args.url)
    logger.info("Set url to %s" % url)
else:
    exit()

# fetch data at URL
response = requests.get(url, headers=headers)
logger.info(f"Received response {response.status_code}")

# command line arg --output overrides the default filename
if args.output:
    output = args.output
else:
    # create default filename
    output = (
        args.url
        + "-"
        + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        + "."
        + args.format
    )
logger.info(f"Writing {args.format} - {output}")
# if --format is "raw" then just print out what we got from PJM
if args.format == "raw":
    print(response.json())
else:
    # otherwise use the tablib library to massage data into desired format
    data = tablib.Dataset(headers=response.json()["items"][0].keys())
    for item in response.json()["items"]:
        data.append(item.values())

    if args.format in ["csv", "json", "yaml"]:
        with open(output, "w", newline="") as f:
            f.write(data.export(args.format))
    elif args.format == "xls":
        with open(output, "wb") as f:
            f.write(data.export(args.format))
    elif args.format == "stdout":
        print(data.csv)
    else:
        exit("Invalid output format")
logger.info("Complete")
