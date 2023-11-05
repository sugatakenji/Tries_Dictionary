import lxml
from bs4 import BeautifulSoup



def dictXML():
    myDict = []
    xml = open("gcide_b.xml","r")
    xml = xml.read()
    xml = "<root>"+xml+"</root>"
    parser = BeautifulSoup(markup=xml, features="lxml-xml")
    p_list = parser.find_all("p")
    p_groups = []
    for p in p_list:
        if p.find("ent") is not None:
            p_group = [p]
            p_groups.append(p_group)
        elif p_groups.__len__() < 1:
            pass
        else:
            p_groups[p_groups.__len__() - 1].append(p)

    for p_group in p_groups:
        entry = p_group[0].find("ent") #Palavra
        
        index = 1
        wordDef = ""
        for p in p_group:
            definitions = p.find_all("def")
            definitions = map(lambda d: d.text, definitions)
            definitions = list(definitions)    
            wordDef += str(index)+"-"+"".join(definitions)
            index +=1

        myDict.append([entry.text, wordDef])
        
    return myDict