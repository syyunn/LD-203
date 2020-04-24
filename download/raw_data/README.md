## Run `unzip.sh` to unzip all "YY_{MID/END}YEAR_XML.zip" inside `./unzipped` in the `./raw_data`
    source unzip.sh

## To Count how many unzipped `*.xml` inside the `./unzipped`
    ls -l | grep -v ^l | wc -l  #424337 as of 24 April 2020

    