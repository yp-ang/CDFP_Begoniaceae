from urllib.request import Request, urlopen
from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def find_start(lines, substring):
    for i in range(0, fileLength):
        line = lines[i]
        if substring in line:
            break
    return i
def write_line(filepath, content):
    with open(filepath, 'a', encoding="utf-8") as f:
        f.write(content)


if __name__ == '__main__':

    url = "https://www.philippineplants.org/Families/Begoniaceae.html"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    Genus = "Begonia"
    filepath = r"C:\Users\angyu\Desktop\Begaoniaceae.txt"

    web_byte = urlopen(req).read()
    webpage = strip_tags(web_byte.decode('latin-1'))
    lines = webpage.split("\n")
    fileLength = len(lines)

    with open(filepath, 'w') as f:
        f.write(" ")
        f.close()


    start_index = find_start(lines, Genus+" ")
    for i in range(start_index, fileLength):
        line = lines[i]
        if (line.strip() != ""):
            if Genus + " Resource" in line:
                break
            elif Genus +" " in line:
                write_line(filepath, "\n"+ line.lstrip() + "\n")
                print("\n"+ line + "\n")
            else:
                write_line(filepath, line.lstrip().rstrip() )








