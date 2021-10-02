import csv
import sys

from pathlib import Path

def save_csv(qualifying_loans, csvpath):
    csvpath = Path(csvpath)
    
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")
    
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for loan in qualifying_loans:
            csvwriter.writerow(loan)


