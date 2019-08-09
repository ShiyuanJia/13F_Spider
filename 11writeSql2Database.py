# import requests
import os
import time
import pymysql
import sys
# content = requests.get('https://www.sec.gov/Archives/edgar/data/1584087/000158408715000001/0001584087-15-000001.txt').text
# content = str(content)
# # content.replace('\n', "")
# print(content)

def save_mysqldb(db,sql):
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit()
        print('commit successfully')
    except Exception as err:
        db.rollback()
        print('commit error ******')
        print(err)

def run(start, end):
	#依次从文件中获取每个xml文件，并将xml文件转换成SQL文件

	# infoFilePrefix = "/Users/apple/Desktop/sinaSpider/DongKe/"
	# companyName = open(infoFilePrefix + "companyName.txt", 'r+')
	# urlFile = open(infoFilePrefix + "html.txt", 'r+')
	# infoPeriod = open(infoFilePrefix + "infoPeriod.txt", 'r+')
	# filingDate = open(infoFilePrefix + "timeResult.txt", 'r+')

	# # 打开数据库连接
	# db = pymysql.connect("localhost","root","jiajia123","database")
	# # 使用cursor()方法获取操作游标
	# cursor = db.cursor()

	errorFile = "/Users/apple/Desktop/errFile.txt"
	eFile = open(errorFile, 'r+')
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
		# # convertCommand = "java -jar xml2sql.jar " + fileName + " " + sqlName
		# #add the time information in to the sql file 
		# sf = open(sqlName, 'a')
		# updateSql = "update infoTable_copy set company = '" + company + "', filing_date = '" + date + "', period = '" + period + "',url = '" + url + "';"
		# sf.write(updateSql)
		# sf.flush()
		# sf.close()
		# sf = open()
		if (not os.path.exists(sqlName)):
			count = count + 1
			continue

		sql = "truncate table infortable;"


		# time.sleep(0.5)

		# os.system(convertCommand)
		
		# time.sleep(0.5)
		# cursor.execute("source " + sqlName)
		# db = pymysql.connect("localhost", "root", "jiajia123","database")
		# cursor = db.cursor()
		# cursor.execute("source " + sqlName)
		# print(intoDataBaseCommand)

		intoDataBaseCommand =  "mysql -uroot -pjiajia123 database -e 'source " + sqlName + "'" + "> /Users/apple/desktop/test.txt 2>&1 "
		# try:
		os.system(intoDataBaseCommand)

		# except Exception as err:
		# 	save_mysqldb(db,sql)
		# 	eFile.write(sqlName)
		# 	eFile.write('\n')
		# 	print("hello")
		# 	print(err)

		logfile = "/Users/apple/desktop/test.txt"
		# with open(logfile, 'r') as f:
		# 	print(f.readlines())
		num = open(logfile, 'r')
		list = num.readlines()

		# print("count is " + str(count))

	
		# for i in list:
		# 	num.write(i)
		
		num.flush()
		num.close()
		# os.system("")
		# print(list)
		# print(len(list))
		# print("-----")
		# list = lFile.readlines()
		truncateSql = "mysql -uroot -pjiajia123 database  -e 'truncate table infotable;'"
		if len(list) > 1:
			# print(list)
			print(str(count))


			eFile.write(str(count))
			eFile.write('\n')
			eFile.flush()
			os.system(truncateSql)
			# print("***deal with error")

		count = count + 1



if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    run(start, end)
