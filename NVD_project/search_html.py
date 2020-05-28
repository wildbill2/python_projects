# Opening nvd_html.txt as read only
with open("nvd_html.txt", "r") as read_file:
    textdata=read_file.read()

# Variables for extracting json strings
x = 0
y = 0
boundaries = []
text_length = len(textdata)

try:
    while True:
        x = textdata.index('https://nvd.nist.gov/feeds/json/cve/1.1/nvdcve-1.1', y, text_length)
        y = textdata.index('/a', x, text_length)
        boundaries.append((x, y))
        print('x', x, 'y', y)
except ValueError:
    print("No more data")
except:
    print("error or no more data")


refs = []
files = []

for atuple in boundaries:
    jsfile = textdata[atuple[0]:atuple[1]]
    if jsfile.count('zip') > 0:
        jsfile = jsfile[:jsfile.index('"')]
        files.append(jsfile[jsfile.index('nvdcve'):])
        refs.append(jsfile)


print(files)


