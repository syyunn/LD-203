import os
import sys
import argparse
import logging
import urllib.request

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Download LD-203 dump data from lobbying contribution database at house.gov'
    )

    parser.add_argument("--year1",
                        help="Starting year to download",
                        type=int)

    parser.add_argument("--year2",
                        help="End year to download",
                        type=int)

    args = parser.parse_args()

    return args


def main(args):
    url_suffix = '_XML.zip'
    url_prefix = 'https://disclosurespreview.house.gov/data/LC/'
    half_year_suffixes = ['MidYear', 'YearEnd']
    years = list(range(args.year1, args.year2+1))
    print(years)

    # Make data dir where to download files
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    dir_name = "raw_data"
    dir_to_create = os.path.join(parent_dir, dir_name)

    try:
        os.mkir(dir_to_create)
        print("Created ")
    except OSError as error:
        print(error)

    log.info("Downloading following urls ... ")
    urls = []
    for year in years:
        for half_year_suffix in half_year_suffixes:
            filename = str(year) + '_' + half_year_suffix + url_suffix

            # download_path =
            url = url_prefix + filename
            urls.append(url)
            print(url)

    # filenmae = "test.xml"
    # urllib.request.urlretrieve(url, filenmae)


if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)
