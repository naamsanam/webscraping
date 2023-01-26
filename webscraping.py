import pandas as pd
import requests
from bs4 import BeautifulSoup

gst_mapping = pd.read_csv("C:/Users/IT/Downloads/gst.csv")

#scraping products from website

url = 'https://www.amazon.in/ASUS-15-6-inch-GeForce-Windows-FA506IHRZ-HN111W/dp/B0B5DZTNZQ?ref_=Oct_DLandingS_D_d4afb6b4_60'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#product information

product_name = soup.find_all(class_='product-name')
product_price = soup.find_all(class_='product-price')
product_category = soup.find_all(class_='product-category')

#dataframe

products_df = pd.DataFrame({'product_name':product_name, 'product_price':product_price, 'product_category':product_category})

#scraping products from website

url = 'https://www.flipkart.com/samsung-galaxy-f23-5g-forest-green-128-gb/p/itm4001e68fda319?pid=MOBGBKQF3QM4GHWN&lid=LSTMOBGBKQF3QM4GHWNJ56YXY&marketplace=FLIPKART&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=b_1_1&otracker=clp_banner_1_12.bannerX3.BANNER_mobile-phones-store_BVS8F6DVDXLE&fm=neo%2Fmerchandising&iid=5a62e19b-8ad9-4440-9e1d-355f46c2c8c7.MOBGBKQF3QM4GHWN.SEARCH&ppt=browse&ppn=browse&ssid=55el1zxyv40000001674742336213'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#product information

product_name = soup.find_all(class_='product-name')
product_price = soup.find_all(class_='product-price')
product_category = soup.find_all(class_='product-category')


#dataframe
temp_df = pd.DataFrame({'product_name':product_name, 'product_price':product_price, 'product_category':product_category})

#append dataframe
products_df=products_df.append(temp_df)

#Add gst rate to each product based on its category
products_df=pd.merge(products_df, gst_mapping, on='product_category')

#data analysis
avg_gst_by_category = products_df.groupby('product_category')['gst_rate'].mean()

#Export the dataframe to CSV file
avg_gst_by_category.to_csv("avg_gst_by_category.csv")

#Export all scraped product information to CSV file
products_df.to_csv('produts_info.csv', index=False)