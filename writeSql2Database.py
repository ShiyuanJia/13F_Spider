# import requests
import os
import time
import pymysql
import sys
# content = requests.get('https://www.sec.gov/Archives/edgar/data/1584087/000158408715000001/0001584087-15-000001.txt').text
# content = str(content)
# # content.replace('\n', "")
# print(content)

def run(start, end):
	#依次从文件中获取每个xml文件，并将xml文件转换成SQL文件

	# infoFilePrefix = "/Users/apple/Desktop/sinaSpider/DongKe/"
	# companyName = open(infoFilePrefix + "companyName.txt", 'r+')
	# urlFile = open(infoFilePrefix + "html.txt", 'r+')
	# infoPeriod = open(infoFilePrefix + "infoPeriod.txt", 'r+')
	# filingDate = open(infoFilePrefix + "timeResult.txt", 'r+')

	count = start;
	file = "/Users/apple/Desktop/Sina/testResult/"
	
	suffix = "sqlResultRetry/"
	while (count < end):
		# fileName = file + str(count) + "_xml.xml"
		sqlName = file + suffix + str(count) + "_sql.sql"
		# company = companyName.readline()
		# date = filingDate.readline()
		# period = infoPeriod.readline()
		# url = urlFile.readline()
		# convertCommand = "java -jar xml2sql.jar " + fileName + " " + sqlName
		#add the time information in to the sql file 
		if (not os.path.exists(sqlName)):
			count = count + 1
			continue
		sf = open(sqlName, 'a')
		# INSERT INTO 目标表 SELECT * FROM 来源表;
		insertSql = "insert into infoTableFinish(`cusip`,`Sole`,`sshPrnamtType`,`investmentDiscretion`,`votingAuthority`,`Shared`,`nameOfIssuer`,`value`,`shrsOrPrnAmt`,`None`,`sshPrnamt`,`titleOfClass`,`company`,`filing_date`,`period`,`url`) select `cusip`,`Sole`,`sshPrnamtType`,`investmentDiscretion`,`votingAuthority`,`Shared`,`nameOfIssuer`,`value`,`shrsOrPrnAmt`,`None`,`sshPrnamt`,`titleOfClass`,`company`,`filing_date`,`period`,`url` from infoTable;"
		deleteSql = "truncate table infoTable;"
		# updateSql = "update infoTable set company = '" + company + "', filing_date = '" + date + "', period = '" + period + "',url = '" + url + "';"
		sf.write('\n')
		sf.write(insertSql)
		sf.write('\n')
		sf.write(deleteSql)
		sf.flush()
		sf.close()
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
		count = count + 1



if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    run(start, end)
