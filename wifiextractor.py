import subprocess as sp
from xml.dom import minidom

def extract_all():
    sp.run("netsh wlan export profile key=clear", stdout=sp.PIPE, stderr=sp.PIPE)
    xmls = []
    for file in os.listdir():
        if file.endswith(".xml") and file.startswith("Wi-Fi"):
            xmls.append(file)

    for xml in xmls:
        file = minidom.parse(xml)
        psw = file.getElementsByTagName("keyMaterial")[0].firstChild.data
        name = file.getElementsByTagName("name")[0].firstChild.data

        print(name+" : "+psw)

    for file in xmls:
        os.remove(file)



if __name__ == "__main__":
    extract_all()
