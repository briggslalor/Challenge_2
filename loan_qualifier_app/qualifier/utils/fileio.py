# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
import sys

from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(qualifying_loans, csvpath):
    """Function loads a CSV from the path provided and determines if the path exists. 
       If the path does exist, the function saves the provided list of qualifying loans to the CSV file.
    
    Args:
        qualifying_loans (List): List conatining the loans that the user has qualified for.
        csvpath (Path): The csv file path.
    
    """
    
    csvpath = Path(csvpath)
    
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")
    
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for loan in qualifying_loans:
            csvwriter.writerow(loan)