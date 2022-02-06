import requests
import re
import json
import pytesseract as tess
import pandas as pd
from pdf2image import convert_from_bytes
from bs4 import BeautifulSoup as bs

pdfs = []
df = pd.read_csv('https://docs.google.com/spreadsheets/d/1I7hziCQGd0uKzh4RMnZtpkTspaE-1_bIL0FcGU_Y1DU/gviz/tq?tqx=out:csv', header=None)

def convert(link):
    text = ""
    count = 0
    r = requests.get(link, stream=True)
    pages = convert_from_bytes(r.raw.read())
    for page in pages:
        count += 1
        text += (tess.image_to_string(page, lang="hin+eng")+"\n")
        print(f"Pages Converted: {count}", end='\r')
    return text

if __name__ == "__main__":
    for link in list(df[0])[:1]:
        print("\n"+link)
        if link[-3:] != "pdf":
            r = requests.get(link)
            soup = bs(r.content, "html.parser")
            for i in soup.find_all('a'):
                try:
                    if str(i['href'])[-4:] == ".pdf":
                        pdf_url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', link)[0]+i['href']
                except:
                    pass
        else:
            pdf_url = link
            pdfs.append({
                "page-url": link,
                "pdf-url": pdf_url,
                "pdf-content": convert(pdf_url)
            })
    with open('pdf_extract.json', 'w') as jsonfile:
            json.dump(pdfs, jsonfile)
