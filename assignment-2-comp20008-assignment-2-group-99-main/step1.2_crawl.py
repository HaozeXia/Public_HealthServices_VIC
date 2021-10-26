import urllib.request


def download_file(url, index):
    local_filename = index + "-" + url.split('/')[-1]

    local_filename = local_filename.split(".xlsx.aspx")[0] + ".xlsx"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    f = urllib.request.urlopen(req)
    data = f.read()

    with open(local_filename, 'wb') as code:
        code.write(data)

    return local_filename


if __name__ == '__main__':
    urls = [
        "https://www.aihw.gov.au/getmedia/fb227d5e-0084-487d-b921-0ac5c6f65803/Hospital-resources-2019-20-data-tables-17-August-2021.xlsx.aspx",
        "https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

    ]
    for url in urls:
        download_file(url, "1")