# data_harvest - Amazon Data Scraper

data_harvest is a Python program that scrapes product information from Amazon's website. Specifically, it extracts the product name, price, rating out of 5 stars, and availability information. This program can be used for various purposes such as competitor research, price monitoring, or data analysis.

## Requirements
The following Python libraries are required to run the program:

- BeautifulSoup4
- Requests
- Pandas
- Numpy

## Usage
1. Install the required libraries by running pip install -r requirements.txt in the terminal.
2. Open the amazon_scraper.py file in your Python editor of choice
3. Replace the url variable with the Amazon product page link you want to scrape.
4. Run the program.
5. Once the program has finished running, the product information will be displayed on the terminal console.

## Sample Output
Here is an example of the output you can expect from the program:

```
Product name: Example Product Name
Price: $99.99
Rating: 4.5 out of 5 stars
Availability: In stock
```

## Acknowledgments
Thank you to the authors of the BeautifulSoup4 and Requests libraries for providing the tools necessary to build this program.