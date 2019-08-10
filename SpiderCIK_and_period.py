# -*- coding: utf-8 -*-
import requests
import re
from lxml import etree
count = 0


def run():
    html_file = "/Users/apple/Desktop/html.txt"
    f_html = open(html_file, 'r+')

    # id_file = "/Users/apple/Desktop/identify.txt"
    # f_id = open(id_file, 'r+')

    start_urls = []
    # count = -1
    period_file = "/Users/apple/Desktop/sinaSpider/DongKe/rightPeriod.txt"
    cik_file = "/Users/apple/Desktop/sinaSpider/DongKe/rightCIK.txt"

    f_period = open(period_file, 'r+')
    f_cik = open(cik_file, 'r+')

    for i in range(0, 100):
        url = f_html.readline()
        url = url.strip('\n')
        # identify = f_id.readline()
        # identify = identify.strip('\n')
        # url_map[url] = identify
    # print("^^^^^^")
    # print(map)
    # print("^^^^^^")

        # global count
        # print("****")
        # print('count is' + str(count))
        # print(self.start_urls[count])
        # print("****")
        # html = self.start_urls[count]
        # print("here")
        # html = str(response.url)
        # start = 0
        # end = 10

        # for i in range(0, start):
        #     # f_html.readline()
        #     f_id.readline()
        # while count < end:
        # html = f_html.readline()

        # identify = f_id.readline()

        # period = response.xpath("//div[@class='formGrouping'][2]/div[@class='info'][1]").extract()
        h = requests.get(url)
        res = etree.HTML(h.content)
        if (i % 10 == 0):
            print(i)
        try:
            period = res.xpath("//*[@id='formDiv']/div[2]/div[2]/div[2]/text()")[0]
            f_period.write(period)
            f_period.write('\n')
            f_period.flush()
        except Exception:
            print("period error ")
            print(url)
            print("------")
        # if response.status == 200:
        try:
            cik = res.xpath("//*[@id='filerDiv']/div[3]/span/a/text()")[0]
            cik = re.findall("[0-9]+", cik)[0]
            f_cik.write(cik)
            f_cik.write('\n')
            f_cik.flush()
        except Exception:
            print("cik error ")
            print(url)
            print("------")
        # else:
        #     f_cik.write('error')
        #     f_cik.write('\n')
        #     f_cik.flush()
        #     f_cik.close()

        '''
        cik = response.xpath("//*[@id='filerDiv']/div[3]/span/a/text()").extract()[0]
        cik = re.findall("[0-9]+", cik)[0]
        company = response.xpath("//*[@id='filerDiv']/div[3]/span/text()[1]").extract()[0]
        pos = company.index('(')
        company = company[0:pos]
        test_Id = company + "_" + cik
        '''
        # print(company)

        # print("^^^^^^")
        # print(type(cik))
        # print(cik)

        # print('----')
        # print(html)
        '''
        if html in url_map:
            identify = url_map[html]
        else:
            identify = -1
        # print(identify)
        # print(period)
        sql = "INSERT INtO PERIODINFO_COMPANY(URL, IDENTIFY, PERIOD, CIK, COMPANY, TEST_ID) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (
            html, str(identify), period, cik, company, test_Id)
        save_mysqldb(db, sql)
        # count = count + 1
        '''
if __name__ == '__main__':
    run()
