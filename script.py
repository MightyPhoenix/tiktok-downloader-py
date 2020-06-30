import urllib.request
import os
import re
links = []
dates = []
# DEFAULT OUTPUT FOLDER IS /out 
# DEFAULT DOWNLOADED FILE EXTENSION IN .mov
# DEFAULT FILENAME WILL BE THE SORTED ORDER + DATE
# DEFAULT .TXT FILE NAME IS Videos.txt

def progress(chunks,max_chunk,t_size):
    if(t_size!=-1):
        print(((float(chunks)*float(max_chunk))/float(t_size))*100+"%","done")
        print('\r')
    else:
        print('Unable to determine size of download, still downloading...')

def download(link, name, path='\\out\\', ext='.mov'):
    try:
        print("\nDownloading...")
        urllib.request.urlretrieve(link, os.getcwd()+path + name + ext,reporthook=progress)
        print(name + " downloaded sucessfully!")
    except Exception as e:
        print(os.getcwd())
        print('\nError Occured!',e)
    return

def main():
    print('\nTiktok Video Retriever from video.txt file from Account Data - [Ver - 1.1]')
    print('\nBy Agnibesh Mukherjee [https://agnibesh.dev] [https://github.com/MightyPhoenix]')
    print('\nAdditional Contributions By Nadeem Akhter [https://github.com/nadeemakhter0602]')
    start = str(input('\nStart the script? (Y/N) : '))
    if (start == 'Y' or start == 'y'):
        with open('Videos.txt', 'r') as f:
            contents = f.read()
        links=re.findall(r'https?://.*',contents)
        dates=re.findall(r'D.*',contents)   
        startDownload = str(input("Found "+str(len(links))+" Video links. Would you like to download? (Y/N): "))
        if (startDownload == 'Y' or startDownload == 'y'):
            for link in links:
                download(link, str(links.index(link) + 1) + "." + dates[links.index(link)].replace(' ','_').replace(':','-'))
        else:
            exit()
    else:
        exit()

main()
            
