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
	# count = start;
	file = "/Users/apple/Desktop/Sina/testResult/"
	timeFile = ""
	suffix = "sqlResultRecovery/"
	err = open("/Users/apple/Desktop/errFile.txt", 'r+')
	count = int(err.readline())
	number_of_XML = 80634
	while (count < end):

		fileName = file + str(count) + "_xml.xml"
		sqlName = file + suffix + str(count) + "_sql.sql"
		convertCommand = "java -jar xml2sql.jar " + fileName + " " + sqlName
		#add the time information in to the sql file 
		# tf = open(timefile, 'r+')
		# sf = open()

		# intoDataBaseCommand =  "mysql -uroot -pjiajia123 database -e 'source " + sqlName + "'"
		# time.sleep(0.5)
		os.system(convertCommand)
		# time.sleep(0.5)
		# cursor.execute("source " + sqlName)
		# db = pymysql.connect("localhost", "root", "jiajia123","database")
		# cursor = db.cursor()
		# cursor.execute("source " + sqlName)

		# os.system(intoDataBaseCommand)

		count = int(err.readline())
		print(count)



if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    run(start, end)
