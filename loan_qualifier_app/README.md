# Loan Qualifier Application

The purpose of this application is to provide a user with an application capable of comparing their given loan requriements with a list of available lendors and determining if the user can qualify for a loan. The application can then save the qualified loans to a CSV file determined by the user. The application takes into account the user's credit score, monthly debt, monthly income, desired loan amount and home value to determine their qualification status. 

---

## Technologies

This application was written in Python 3.7 and is to be used within the Command Line Interface. In addition to the standard Python library, the following libraries were also used:

[Sys Library](https://docs.python.org/3/library/sys.html)
    The Sys library was used to help exit the program when an error was encountered or when it had finished running.

[Fire Library](https://pypi.org/project/fire/)
    The Fire library was used to help integrate and run the program in the command line interface.
    
[Questionary Library](https://pypi.org/project/questionary/)
    The Questionary library was used to generate intuitive prompts for the user to interact with the program in the command line interface and to enter their information.
    
[Pathlib Library](https://docs.python.org/3/library/pathlib.html)
    The Pathlib library was used to help define and utilize the Paths to access and write to CSV files.
    
[CSV Library](https://docs.python.org/3/library/csv.html)
    The CSV library was used to write data to a CSV file.

    
---

## Installation Guide

In order to utilize this application, the user needs to import the Fire and Questionary libraries into Python. This can be done in the command line using the following code:

```
    pip install fire
    pip install questionary
```

---

## Usage


To use this application the user must first open their command line interface and activate an Anaconda environment, code shown uses the standard dev environment, using the following:

```
    conda activate dev
```

Next, the user must change directories into the one containing the application file, app.py, on their machine. Once the user has changed into the correct directory, the application can be called from the command line using the following code:

```
    python app.py
```

The application will then begin to run and will first prompt the user to enter the path to the CSV file containing the current available loans. This path is 'data/daily_rate_sheet.csv'. If the user enters an incorrect path, the application will prompt the user that it is incorrect and then quit.

Once the path is entered correctly, the application will prompt the user for their relevant loan qualification information. With the information coolected, the application will determine which loans the user has qualified for and display the number. It will then prompt the user to choose whether they would like to save the information for their qualified loans. If the user chooses not to, the application will quit. If the user chooses to save it, the application will prompt the user for the path to their desired CSV file. The user can utilize one of their own or the included file 'qualifying_loans.csv' using the path: 'data/qualifying_loans.csv'. If the user enters an incorrect path, the application will prompt the user that it is incorrect and then quit.

---

## Contributors

This application was updated and completed by Briggs Lalor. His email is briggsclalor@gmail.com.

His LinkedIn can be found by following this [link](www.linkedin.com/in/briggsclalor).

---

## License

MIT License

Copyright (c) [2021] [Briggs Lalor]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.