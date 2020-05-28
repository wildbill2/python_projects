# Importing requests module
import requests

# Retrieving NVD page code and writing it to a file named nvd_html.txt
nvd_page_code = requests.get('https://nvd.nist.gov/vuln/data-feeds#JSON_FEED')
with open("nvd_html.txt", "w") as write_nvdt:
    write_nvdt.write(nvd_page_code.text)


