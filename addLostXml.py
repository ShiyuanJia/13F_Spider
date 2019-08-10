# import requests
import os
import time
import pymysql
import sys
import linecache
import requests
import re
# content = requests.get('https://www.sec.gov/Archives/edgar/data/1584087/000158408715000001/0001584087-15-000001.txt').text
# content = str(content)
# # content.replace('\n', "")
# print(content)

def run(start, end):
	#依次从文件中获取每个xml文件，并将xml文件转换成SQL文件

	infoFilePrefix = "/Users/apple/Desktop/sinaSpider/DongKe/"
	# companyName = open(infoFilePrefix + "companyName.txt", 'r+')
	# urlFile = open(infoFilePrefix + "html.txt", 'r+')
	# infoPeriod = open(infoFilePrefix + "infoPeriod.txt", 'r+')
	# filingDate = open(infoFilePrefix + "timeResult.txt", 'r+')
	noList = infoFilePrefix + "notExistXmlList.txt"
	htmlFile = infoFilePrefix + "newResult.txt"
	errFile = open(noList, 'r+')

	count = int(errFile.readline())
	# file = "/Users/apple/Desktop/Sina/testResult/"
	
	# suffix = "sqlResultRecovery/"
	while (count < end):
		# companyName.flush()
		# urlFile.flush()
		# infoPeriod.flush()
		# filingDate.flush()

		url = linecache.getline(htmlFile, count + 1).strip()
	


	# #抓包27万+个txt文件
	# urlFile = '/Users/apple/Desktop/sinaSpider/DongKe/newResult.txt'
	# fileUrl = open(urlFile, 'r+');
	# url = fileUrl.readline()
	# url = url.strip('\n')

	# print(urls)
	# count = 0
	# while (len(url) != 0):
		file = "/Users/apple/Desktop/sinaSpider/DongKe/lostXml/" + str(count) + "_xml.xml"
		# 对每一个txt进行操作
		w1 = '<informationTable '
		w2 = '</informationTable>'

		w3 = '<ns1:informationTable '
		w4 = '</ns1:informationTable>'
		f = open(file, 'w+')
		try:
			buff = str(requests.get(url).text)
		except Exception:
			print("request error :" + str(count))
			f.flush()
			f.close()
			# url = fileUrl.readline()
			# url = url.strip('\n')
			count = count + 1
			continue
		# buff = buff.replace('\\r', '')

		# print(buff)

		# print(type(buff))
		pat = re.compile("(?=" + w1 + ')(.*?)(?=' + w2 + ")", re.S)
		result = pat.findall(buff)
		# # # print(len(result))
		# result = result[0]
		if (len(result) == 0):
			pat = re.compile("(?=" + w3 + ')(.*?)(?=' + w4 + ")", re.S)
			result = pat.findall(buff)
			if (len(result) == 0):
				f.flush()
				f.close()
				# url = fileUrl.readline()
				# url = url.strip('\n')
				count = count + 1
				continue
			result = result[0] + '</ns1:informationTable>'
			f.write(result)
			f.flush()
			f.close
			count = count + 1
			continue

		result = result[0] + ' </informationTable>'
		# # f.seek(0)
		# # f.truncate()
		f.write(result)
		f.flush()
		f.close
		# print(result)
		#
		# url = fileUrl.readline()
		# url = url.strip('\n')
		count = count + 1


		# print(result)
		# f.seek(0)
		# f.truncate()
		# f.write(result)

		'''
		linecache.getline(companyName, count + 1).strip()
		# fileName = file + str(count) + "_xml.xml"
		sqlName = file + suffix + str(count) + "_sql.sql"
		company = linecache.getline(companyName, count + 1).strip()
		date = linecache.getline(filingDate, count + 1).strip()
		period = linecache.getline(infoPeriod, count + 1).strip()
		url = linecache.getline(urlFile, count + 1).strip()
		# convertCommand = "java -jar xml2sql.jar " + fileName + " " + sqlName
		#add the time information in to the sql file 
		if (not os.path.exists(sqlName)):
			count = int(errFile.readline())
			continue
		# print(count)
		# print(company)
		# print(date)
		# print(period)
		# print(url)
		# print("----")

		sf = open(sqlName, 'a')
		updateSql = "update infoTable set company = '" + company + "', filing_date = '" + date + "', period = '" + period + "',url = '" + url + "';"
		sf.write(updateSql)

		insertSql = "insert into infoTableFinish(`cusip`,`Sole`,`sshPrnamtType`,`investmentDiscretion`,`votingAuthority`,`Shared`,`nameOfIssuer`,`value`,`shrsOrPrnAmt`,`None`,`sshPrnamt`,`titleOfClass`,`company`,`filing_date`,`period`,`url`) select `cusip`,`Sole`,`sshPrnamtType`,`investmentDiscretion`,`votingAuthority`,`Shared`,`nameOfIssuer`,`value`,`shrsOrPrnAmt`,`None`,`sshPrnamt`,`titleOfClass`,`company`,`filing_date`,`period`,`url` from infoTable;"
		deleteSql = "truncate table infoTable;"
		# updateSql = "update infoTable set company = '" + company + "', filing_date = '" + date + "', period = '" + period + "',url = '" + url + "';"
		sf.write('\n')
		sf.write(insertSql)
		sf.write('\n')
		sf.write(deleteSql)
		sf.flush()
		sf.close()

		'''
		# sf = open()

		# intoDataBaseCommand =  "mysql -uroot -pjiajia123 database -e 'source " + sqlName + "'"
		# time.sleep(0.5)

		# os.system(convertCommand)
		
		# time.sleep(0.5)
		# cursor.execute("source " + sqlName)
		# db = pymysql.connect("localhost", "root", "jiajia123","database")
		# cursor = db.cursor()
		# cursor.execute("source " + sqlName)

		# os.system(intoDataBaseCommand)



if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    run(start, end)
