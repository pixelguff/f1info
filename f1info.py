#!/usr/bin/env python3

import pandas as pd
import getopt, sys
import argparse

def get_driver_standings(year):
    url = "https://www.formula1.com/en/results.html/"+str(year)+"/drivers.html"
    try:
        dfs = pd.read_html(url)
        df = dfs[0]
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        return(df)
    except:
        return(None)

def get_constructor_standings(year):
    url = "https://www.formula1.com/en/results.html/"+str(year)+"/team.html"
    try:
        dfs = pd.read_html(url)
        df = dfs[0]
        df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
        return(df)
    except:
        return(None)


def main(year, drivers, constructors):
    if drivers:
        standings = get_driver_standings(year)
        if standings is not None:
            print(standings)
        else:
            print("No data available for "+str(year))
    if constructors:
        standings = get_constructor_standings(year)
        if standings is not None:
            print(standings)
        else:
            print("No data available for "+str(year))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("f1.py")
    parser.add_argument("-y","--year", help="The year to look up.", type=int)
    parser.add_argument('-d',"--drivers", help="Show drivers standings.", action='store_true')
    parser.add_argument('-c',"--constructors", help="Show constructors standings.", action='store_true')
    args = parser.parse_args()

    try:
        drivers = False
        constructors = False
        if args.drivers:
            drivers = True
        if args.constructors:
            constructors = True
        main(args.year, drivers, constructors)
    except:
        print("Defaulting to the 2023 drivers standings.")
        main(2023, True, False)
