from urllib.request import Request, urlopen
from io import StringIO
from html.parser import HTMLParser
import xlsxwriter

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

#def function(filepath, line):



if __name__ == '__main__':

    url = "https://www.philippineplants.org/Families/Begoniaceae.html"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    Genus = "Begonia"
    filepath = r"C:\Users\angyu\Desktop\Begoniaceae.txt"

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
            elif line.split()[0] == "Begonia":
                edited_line = "\n" + line.lstrip() + " "
                write_line(filepath, edited_line)

            else:
                edited_line = line.lstrip().rstrip()
                write_line(filepath, edited_line )

    excel = xlsxwriter.Workbook(r"C:\Users\angyu\Desktop\Begoniaceae.xlsx")
    excelsheet = excel.add_worksheet("Begonias")



    row = 0

    textfile = open(filepath, 'r',  encoding='utf-8')
    all_lines = textfile.readlines()
    for species in all_lines:
        components = species.split(" ")


        bracket_index = 0
        multiple_author = 0
        author_index = 0
        first_author_index = 0
        for words in components:
            if words == "×":
                components[1:3] = [' '.join(components[1:3])]

            if "(1" in words or "(2" in words:
                bracket_index = components.index(words)
                break
        excelsheet.write(row, 0, components[1])

        for i in range(2, bracket_index):
            if components[i] == "&":
                multiple_author = 1
                author_index = i

        for j in range(author_index,bracket_index):
            if "," in components[j]:
                author_index = j

        for k in range(2, bracket_index):
            if "," in components[k]:
                first_author_index = k
                break

        species_authority = ""
        if multiple_author == 1:
            for i in range(2,author_index+1):
                species_authority += (" " + components[i])

        else: #single author
            for i in range(2,first_author_index+1):
                species_authority += (" " + components[i])

        species_authority = species_authority.rstrip(",")
        excelsheet.write(row, 1, species_authority)

        row += 1

    excelsheet.write(0, 0, "Epithet")
    excelsheet.write(0, 1, "Authority")
    excel.close()










