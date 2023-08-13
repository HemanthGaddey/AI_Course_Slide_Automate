import requests
import re
import os

url = "https://ds251.iitbh.repl.co/"
html = requests.get(url).text
pdf_links = re.findall(r'href="slides/([^"]+\.pdf)"', html)
path = r"." #Add your custom directory but DONT end this string with '\' as last character!
for link in pdf_links:
    pdf_path = path+"\\"+link
    pdf_url = url+"slides/"+link
    if(not os.path.exists(pdf_path)):
        response = requests.get(pdf_url, stream=True)
        if response.status_code == 200:
            with open(pdf_path, 'wb') as pdf_file:
                for chunk in response.iter_content(chunk_size=1024):
                    pdf_file.write(chunk)