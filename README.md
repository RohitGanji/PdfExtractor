# PDF Extractor

The urls are first extracted from the Google Spreadsheet. The links to the pdfs that are not readily pdf downloadable are then extracted from the url. The content of the pdf is then scraped and saved in a JSON file. 
```zsh

python3 pdf_extractor.py

```
<br>
<img src="/output.png"/, width=100%>
<br>
Due to time constraints, multiprocessing couldn't be implemented.
