import requests
from bs4 import BeautifulSoup


def numinfo(number):
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://freshsimdatabases.com/"}
    data = {
        'numberCnic': number,
        'searchNumber': ''}
    response = requests.post('https://freshsimdatabases.com/numberDetails.php', headers=headers, data=data)
    soup = BeautifulSoup(response.text, "html.parser")
    if (soup.find("div", class_="table-responsive")) != None:
        name = numb = cnic = address = operator = gender = "N/A"
        tds = soup.find_all("td")
        if "Telenor.png" in str(tds[0]):
            operator = "Telenor"
        elif "Zong.png" in str(tds[0]):
            operator = "Zong"
        elif "Jazz.png" in str(tds[0]):
            operator = "Jazz"
        for i, td in enumerate(tds):
            text = td.get_text(strip=True)
            if text == "MSISDN":numb = tds[i+1].get_text(strip=True)
            elif "CNIC" in text:cnic = tds[i+1].get_text(strip=True)
            elif "deducted/collected from" in text:address = tds[i+1].get_text(strip=True)
            elif "income tax has been" in text:name = tds[i+1].get_text(strip=True)
        gender_digit = int(cnic[-1])
        if int(gender_digit) % 2 == 0:gender = "Female"
        else:gender = "Male"
        num_data = {
            "status":"success",
            "name":name,
            "number":numb,
            "gender":gender,
            "operator":operator,
            "cnic":cnic,
            "address":address}
    else:
        num_data = {
            "status":"error"}
    return num_data