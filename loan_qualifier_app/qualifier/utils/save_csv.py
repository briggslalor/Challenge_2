import csv

def save_csv(qualifying_loans):
    csvpath = Path("qualifying_loans.csv")
    
    with open(csvpath, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        for loan in qualifying_loans:
            csvwriter.writerow(loan)


