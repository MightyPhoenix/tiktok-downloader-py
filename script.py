import urllib.request
import os

links = []
dates = []
# DEAFAULT OUTPUT FOLDER IS /out 
# DEFAULT DOWNLOADED FILE EXTENSION IN .mov
# DEFAULT FILENAME WILL BE THE SORTED ORDER + DATE
# DEFAULT .TXT FILE NAME IS Videos.txt
def download(link, name, ext='.mov',path='\\out\\'):
    try:
        print("\nDownloading...")
        name = name.split(' ')
        name = '_'.join(name)
        name = name.replace(':','-')
        urllib.request.urlretrieve(link, os.getcwd()+path + name + ext)
        print(name + " downloaded sucessfully!")
    except Exception as e:
        print(os.getcwd())
        print('\nError Occured!',e)
    return

def main():
    print('\nTiktok Video Retriever from video.txt file from Account Data - [Ver - 1.0]')
    print('\nBy Agnibesh Mukherjee [https://agnibesh.dev] [https://github.com/MightyPhoenix]')
    start = str(input('\nStart the script? (Y/N) : '))
    if (start == 'Y' or start == 'y'):
        file = open('Videos.txt', 'r')
        contents = file.readlines()
        for line in contents:
            if (line[0] == 'V'):
                temp = line
                links.append(temp[12:-1])
        for date in contents:
            if (date[0] == 'D'):
                dates.append(date[:-1])
        startDownload = str(input("Found "+str(len(links))+" Video links. Would you like to download? (Y/N): "))
        if (startDownload == 'Y' or startDownload == 'y'):
            for link in links:
                download(link, str(links.index(link) + 1) + " " + dates[links.index(link)])
        else:
            exit()
    else:
        exit()

main()
            