import requests
from bs4 import BeautifulSoup

URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
response = requests.get(URL)
data = response.content

soup = BeautifulSoup(data, "html.parser")

all_majors = soup.find_all(class_="data-table__cell csr-col--school-name")
majors = [x.getText().strip("Major:") for x in all_majors]

for x in majors:
    print(x)