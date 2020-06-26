import urllib.request,os
links,dates = [],[]
# DEAFAULT OUTPUT FOLDER IS /out 
# DEFAULT DOWNLOADED FILE EXTENSION IN .mov
# DEFAULT FILENAME WILL BE THE SORTED ORDER + DATE
# DEFAULT .TXT FILE NAME IS Videos.txt
def download(link, name, ext='.mov',path='\\out\\'):
    try:
        print("\nDownloading...")
        name = name.split(' ')
        name = '_'.join(name).replace(':','-')
        urllib.request.urlretrieve(link, os.getcwd()+path + name + ext)
        print(name + " downloaded sucessfully!")
    except Exception as e:
        print('\nError Occured!',e)
    return

def main():
    print('\n====================================================================================')
    print('Tiktok Video Retriever from video.txt file from Account Data - [Ver - 1.0]         =')
    print('By Agnibesh Mukherjee [https://agnibesh.dev] [https://github.com/MightyPhoenix]    =')
    print('====================================================================================')
    start = str(input('\nStart the script? (Y/N) : '))
    if (start.upper() == 'Y'):
        file = open('Videos.txt', 'r').readlines()
        for line in file:
            if (line[0] == 'V'):
                links.append(line[12:-1])
        for date in file:
            if (date[0] == 'D'):
                dates.append(date[:-1])
        startDownload = str(input("Found "+str(len(links))+" Video links. Would you like to download? (Y/N): "))
        if (startDownload.upper() == 'Y'):
            for link in links:
                download(link, str(links.index(link) + 1) + " " + dates[links.index(link)])
        else:
            exit()
    else:
        exit()
main()
            