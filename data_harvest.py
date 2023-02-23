# Importing the Required Modules

from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os

# !pip install python-dotenv

# Function to extract product Title
def get_title(soup):
	try:
		# get the product title as a string
		title = soup.find("span", attrs={"id": "productTitle"}).text.strip()
	
	except AttributeError:
		title = ""
	return title

# Function to extract Product Price
def get_price(soup):
	try:
		# get the product title as a string
		price = soup.find("span", attrs={"class": "a-offscreen"}).text.strip()
	except AttributeError:
		try:
			# If there is some deal price
			price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()
			
		except:
			price = ""
	return price

# Function to extract product rating
def get_rating(soup):
	try:
		# get the product rating as a string
		rating = soup.find("span", attrs={"class": "a-icon-alt"}).text.strip()
	except AttributeError:
		rating = ""
	return rating

# Function to get the number of product reviews by amazon users
def get_review_count(soup):
	try:
		# get the number of product reviews as a string
		review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).text.strip()
	except AttributeError:
		review_count = ""
	return review_count

# Function to extract the availability status of a product
def get_availability(soup):
	try:
		# get the availability status of a product
		availability = soup.find("div", attrs={'id':'availability'})
		availability = availability.find("span").text.strip()
	except AttributeError:
		availability = "Not in Stock"
	return availability

# Main Program to extract the data using the above functions
if __name__ == '__main__':

	# The Amazon URL to check
	url = "https://www.amazon.com/s?k=laptop&crid=3S0WZLZ9Y84JK&sprefix=laptop%2Caps%2C592&ref=nb_sb_noss_1"
	
	
	# read my credentials
	user_agent = os.environ['USER_AGENT']
	
	# my header
	header = ({'user-agent': user_agent, 'Accept-Language': 'en-US, em;q=0.5'})

	# HTTP request to the amazon website

	amazon = requests.get(url, headers=header).text

	# soup object containing all HTML data
	soup = BeautifulSoup(amazon, "html.parser")

	# Fetch links from the HTML archor tags
	links = soup.find_all("a", attrs={'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})

	# Store the links in an list
	links_list = []

	# Extract the links from the links text
	for link in links:
		links_list.append(link.get('href'))
	
	# create a dictionary for the data

	cols = {"title":[], "price":[], "rating":[], "reviews":[], "availability":[]}

	# extract product detail from all the links in the links_list
	for link in links_list:
		amazon_page = requests.get("https://www.amazon.com" + link, headers=header)
		sub_soup = BeautifulSoup(amazon_page.content, "html.parser")

		# Function calls to display all necessary product information
		cols['title'].append(get_title(sub_soup))
		cols['price'].append(get_price(sub_soup))
		cols['rating'].append(get_rating(sub_soup))
		cols['reviews'].append(get_review_count(sub_soup))
		cols['availability'].append(get_availability(sub_soup))
	
	amazon_data = pd.DataFrame.from_dict(cols)
	amazon_data['title'].replace('',np.nan, inplace=True)
	amazon_data = amazon_data.dropna(subset=['title'])
	amazon_data.to_csv("amazon_data.csv", header=True, index=True)

	amazon_data