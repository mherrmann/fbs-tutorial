# fbs-sample
Sample project for creating cross-platform desktop appications with
[fbs](https://github.com/mherrmann/fbs)

## Getting Started
This example should work on Windows, Mac and Ubuntu. You need Python 3.5.
(Higher versions may work as well, but are not officially supported.)

Clone this repository and `cd` into it:

    git clone https://github.com/mherrmann/fbs-sample
    cd fbs-sample

Create a virtual environment:

    python3 -m venv venv

Activate the virtual environment:

    # On Mac/Linux:
    source venv/bin/activate
    # On Windows:
    call venv\scripts\activate.bat

Install the required libraries (most notably, `fbs` and `PyQt5`):

    pip install -r requirements.txt

Run the sample app:

    python -m fbs run