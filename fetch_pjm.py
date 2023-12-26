import argparse
import datetime
import logging
import requests
import tablib
from get_pjm_url import get_pjm_list, get_pjm_url
from get_subscription_headers import get_subsription_headers
import coloredlogs

# Constants
VERSION = "1.0"
DEFAULT_OUTPUT_FORMAT = "csv"
OUTPUT_FORMATS = ["csv", "json", "xls", "stdout", "raw"]

# Initialize Logger
def setup_logger():
    logger = logging.getLogger("fetch_pjm")
    logger.setLevel(logging.DEBUG)
    coloredlogs.install()
    return logger

logger = setup_logger()

# Argument Parsing
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", "-u", help="Set URL key for data extraction. e.g., solar_gen, pnode, etc.")
    parser.add_argument("--output", "-o", help="Set filename to output")
    parser.add_argument("--format", "-f", help="Set format for output", choices=OUTPUT_FORMATS, default=DEFAULT_OUTPUT_FORMAT)
    parser.add_argument("--list", "-l", help="Output list of all URLs", action="store_true")
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    return parser.parse_args()

args = parse_arguments()

# Functions
def get_header():
    headers = get_subsription_headers()
    logger.info(f"Fetch subscription header {headers}")
    return headers

def output_data_list():
    list = get_pjm_list()
    print("|url|display name and description|")
    print("|---|---|")
    for l in list:
        print(f"|{l['name']}|*{l['displayName']}* {l['description']}|")

def fetch_paginated_data(url, headers):
    items = []
    total_rows = None
    retrieved_rows = 0

    while url:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()

            if total_rows is None:
                total_rows = data['totalRows']

            new_items = data['items']
            items.extend(new_items)
            retrieved_rows += len(new_items)
            logger.info(f"Retrieved {retrieved_rows}/{total_rows} rows")

            # Check for next page
            next_page = next((link['href'] for link in data['links'] if link['rel'] == 'next'), None)
            url = next_page
        except requests.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            exit(1)

    return items

def generate_output_filename(url, format):
    return f"{url}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.{format}"

def save_data(data, output, format):
    with open(output, "w" if format != "xls" else "wb") as f:
        if format != "xls":
            f.write(data.export(format))
        else:
            f.write(data.export(format))

# Main Script Logic
if args.list:
    output_data_list()
    exit()

if not args.url:
    logger.error("URL not provided")
    exit(1)

url = get_pjm_url(args.url)
logger.info(f"Set URL to {url}")

headers = get_header()
items = fetch_paginated_data(url, headers)

output = args.output if args.output else generate_output_filename(args.url, args.format)
logger.info(f"Writing {args.format} - {output}")

if args.format == "raw":
    print(items)
else:
    data = tablib.Dataset()
    if items:
        data.headers = items[0].keys()
        for item in items:
            data.append(item.values())

    if args.format == "stdout":
        print(data.csv)
    elif args.format in OUTPUT_FORMATS:
        save_data(data, output, args.format)
    else:
        logger.error("Invalid output format")
        exit(1)

logger.info("Complete")
