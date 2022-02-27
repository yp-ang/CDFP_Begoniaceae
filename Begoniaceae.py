from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import xlsxwriter

def remove_all_tag(tag, soup):
    tags = soup.findAll(tag)
    for match in tags:
        match.decompose()

if __name__ == '__main__':

    url = "https://www.philippineplants.org/Families/Begoniaceae.html"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    Genus = "Begonia"
    filepath = r"C:\Users\angyu\Desktop\Begoniaceae.txt"

    excel = xlsxwriter.Workbook(r"C:\Users\angyu\Desktop\Begoniaceae.xlsx")
    excelsheet = excel.add_worksheet("Begonias")


    web_byte = urlopen(req).read()
    web_content  = BeautifulSoup(web_byte, "html.parser")
    species_content = web_content.find_all("li")

    #extracting species name
    species_list = []
    species_name = ""
    row = 0
    for species in species_content:
        if species != None:

            em = species.find("em")
            i = species.find("i")
            span = species.find("span")

            if species.find("em") != None:
                species_name = em.string
            elif species.find("i") != None:
                species_name = i.string
            elif species.find("span") != None:
                species_name = span.string

        if species_name != None:
            species_name.find("em")
            if species_name:
                species_name = species_name.string
            species_list.append(species_name)
            print(species_name)

    # extracting contents:
        if species != None:
            remove_all_tag("span", species)
            remove_all_tag("em", species)
            remove_all_tag("i", species)
            remove_all_tag("a", species)

            text = str(species.get_text())


            if "None" not in text:
                text = text.replace("\n", "")
                text = text.replace("\t", "")
                text = text.replace("   ", "")
                text = text.replace("  ", " ")
                text = text.lstrip(" ")

                components = list(map(str,text.split(" ")))

                bracket_index = 0
                multiple_author = 0
                author_index = 0
                first_author_index = 0
                author_index_t = 0
                mai = 0

                for words in components:
                    if "(1" in words or "(2" in words:
                            bracket_index = components.index(words)
                            break

                for i in range(0, bracket_index+1):
                    if components[i] == "&":
                        multiple_author = 1
                        and_index = i
                        break

                for j in range(mai, bracket_index):
                            if "," in components[j]:
                                author_index = j

                for k in range(0, bracket_index):
                    if "," in components[k]:
                        first_author_index = k
                        break

                species_authority = ""
                if multiple_author == 1:
                    for i in range(0,author_index+1):
                        species_authority += (" " + components[i])

                if multiple_author ==0:
                    for i in range(0,first_author_index+1):
                        species_authority += (" " + components[i])

                species_authority = species_authority.lstrip().rstrip(",")
                #print(author_index)
                print(species_authority)
                excelsheet.write(row, 0, species_name)
                excelsheet.write(row, 1, species_authority)
                row+=1



    excel.close()
    num_of_species = len(species_list)
    print(num_of_species)

