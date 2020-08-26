# Used Car Web Scraper Bot

A simple utility for scraping used car info based on VIN.

## Setup

1. Requires ChromeDriver to be installed. [Download](https://sites.google.com/a/chromium.org/chromedriver/downloads) the version that matches your installation of Google Chrome and place the executable in `C:\Program Files (x86)` (or wherever you like, just adjust the PATH variable in `scraper.py` to point to the executable)

2. Download the repository

3. Create a virtual environment within the repository, then activate it

```
> virtualenv .venv
> .\.venv\Scripts\activate
```

4. Install the required packages

```
pip install -r requirements.txt
```

5. Add VINs to the `VIN_LIST` in `scraper.py`

6. Run `> python .\scraper.py`

Output in PowerShell:

```
...
Getting info for VIN: {vin}

 -- DATA SUMMARY --

                 vin  year make    model trim   mileage   below  average    above
0  5XYKT3A69DG353356  2013  Kia  Sorento   LX  102635.0  7396.0   8991.0  10586.0
```

The `below`, `average`, and `above` columns represent the first quartile, mean, and third quartile market values, as estimated from vinaudit.com