import csv
import requests
from bs4 import BeautifulSoup

url = "https://www.prizeinfo.net/1500-prize-bond-first-second-record"

# Make a request to the website
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the table rows
rows = soup.find_all('tr')

# Create an empty list to store the data
data = []

# Iterate through the rows
for row in rows:
    # Find the first, second, and third prize bond numbers
    first_number = row.find('td', class_='table-success my-bold').text
    second_number = row.find('td', class_='table-warning').text
    third_number = row.find_all('td', class_='table-warning')[2].text

    # Find the city and date of draw
    city = row.find_all('td')[-2].text
    date = row.find_all('td')[-1].text

    # Append the data to the list
    data.append([first_number, second_number, third_number, city, date])

# Save the data to a CSV file
with open('prize_bond_data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['First Number', 'Second Number', 'Third Number', 'City', 'Date'])
    writer.writerows(data)
