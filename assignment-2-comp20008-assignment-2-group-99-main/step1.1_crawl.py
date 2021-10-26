from bs4 import BeautifulSoup
import urllib.request
from urllib import request


def download_file(url, index):
    local_filename = index + "-" + url.split('/')[-1]
    local_filename = local_filename.split(".pdf")[0] + ".pdf"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    f = urllib.request.urlopen(req)
    data = f.read()
    # location of storage
    with open(local_filename, 'wb') as code:
        code.write(data)

    return local_filename


def downloadFile(root_link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=root_link, headers=headers)
    response = request.urlopen(req)  # get the response

    if response.status == 200:
        soup = BeautifulSoup(response.read())
        index = 1
        for link in soup.find_all('a'):
            new_link = root_link + link.get('href')
            if new_link.endswith(".pdf.aspx?inline=true"):
                # downlown url
                download_url = "https://www.aihw.gov.au/getmedia" + new_link.split("getmedia")[1]

                file_path = download_file(download_url, str(index))
                print("downloading:" + new_link + " -> " + file_path)
                index += 1
        print("all download finished")
    else:
        print("errors occur.")


if __name__ == '__main__':
    urls = [
        "https://www.aihw.gov.au/reports/hospitals/ahs-2004-05/contents/table-of-contents",
        "https://www.aihw.gov.au/reports/hospitals/ahs-2005-06/contents/table-of-contents"
    ]

    for url in urls:
        downloadFile(url)

# there are a lot URL to use which would not be shown here
# please view all urls in "urls.txt".