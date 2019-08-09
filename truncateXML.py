import re
import requests
import sys



def run(start, end):
	#抓包27万+个txt文件
	urlFile = '/Users/apple/Desktop/sinaSpider/DongKe/newResult.txt'
	fileUrl = open(urlFile, 'r+');
	#
	for i in range(0, start):
		fileUrl.readline()	

	url = fileUrl.readline()
	url = url.strip('\n')

	# print(urls)
	count = start
	while (len(url) != 0 and count < end):
		file = "/Users/apple/Desktop/Sina/testResult/" + str(count) + "_xml.xml"
		# 对每一个txt进行操作
		w1 = '<informationTable '
		w2 = '</informationTable>'
		f = open(file, 'w+')
		try:
			buff = str(requests.get(url).text)
		except Exception:
			print("request error :" + str(count))
			f.flush()
			f.close()
			url = fileUrl.readline()
			url = url.strip('\n')
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
			f.flush()
			f.close()
			url = fileUrl.readline()
			url = url.strip('\n')
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
		url = fileUrl.readline()
		url = url.strip('\n')
		count = count + 1


if __name__ == '__main__':
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    run(start, end)