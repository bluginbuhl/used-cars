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