import os
import sys
import argparse
import logging
import urllib.request
import progressbar

log = logging.getLogger("my-logger")
log.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('[%(levelname)s] %(message)s')
handler.setFormatter(formatter)
log.addHandler(handler)


class Progressbar:
    def __init__(self):
        self.pbar = None

    def __call__(self, block_num, block_size, total_size):
        if not self.pbar:
            self.pbar=progressbar.ProgressBar(maxval=total_size)
            self.pbar.start()

        downloaded = block_num * block_size
        if downloaded < total_size:
            self.pbar.update(downloaded)
        else:
            self.pbar.finish()


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
    log.info("Target years to download: \n {}".format(str(years)))

    # Make data dir where to download files
    parent_dir = os.path.dirname(os.path.realpath(__file__))
    dir_name = "raw_data"
    download_dir = os.path.join(parent_dir, dir_name)

    try:
        os.mkdir(download_dir)
        log.info("Created directory where to download raw data: \n {}".format(download_dir))
    except OSError as error:
        # log.info(error)
        log.info("Directory to download raw data: \n {}".format(download_dir))

    # urls = []
    for year in years:
        for half_year_suffix in half_year_suffixes:
            filename = str(year) + '_' + half_year_suffix + url_suffix
            download_path = os.path.join(download_dir, filename)
            url = url_prefix + filename
            log.info("Downloading the url \n \"{}\" to \n {}".format(url, download_path))
            urllib.request.urlretrieve(url, download_path, Progressbar())


if __name__ == "__main__":
    arguments = parse_arguments()
    main(arguments)
