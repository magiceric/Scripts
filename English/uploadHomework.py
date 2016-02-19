import urllib.request
import json
import shutil
import os
import datetime

rootpath = os.environ['ENGLISH_PATH']
files = [
	{
		'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%253D&path=%2Fhomework%2Fvocabulary.html',
		'path': 'div/',
		'filename': 'vocabulary.html'
	},
	{
		'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%253D&path=%2Fhomework%2Fpronunciation%2FDasha%2Fpractice-and-check.html',
		'path': 'div/',
		'filename': 'daria.html'
	},
	{
		'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%253D&path=%2Fhomework%2Fpronunciation%2FSlava%2Fpractice-and-check.html',
		'path': 'div/',
		'filename': 'slava.html'
	},
	{
		'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=DhLa7f6nRVrD8AZj9EGmFkyE8goTvQr0vPDb6WsdgtQ%3D&path=%2Fhomework%2Fvocabulary%2Fen-ru.html',
		'path': 'aiy/',
		'filename': 'vocabulary.html'
	},
	{
		'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=DhLa7f6nRVrD8AZj9EGmFkyE8goTvQr0vPDb6WsdgtQ%3D&path=%2Fhomework%2Fpronunciation%2FYuliya%2Fpronunciation.pdf',
		'path': 'aiy/',
		'filename': 'yulia.pdf'
	},
	{
		'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=DhLa7f6nRVrD8AZj9EGmFkyE8goTvQr0vPDb6WsdgtQ%3D&path=%2Fhomework%2Fpronunciation%2FAydar%2Fpronunciation.pdf',
		'path': 'aiy/',
		'filename': 'aydar.pdf'
	}
]

def printlog(message):
	message = "%s " + message
	print (message % datetime.datetime.now())

def download():
	printlog('Start downloading')
	for f in files:
		download_url = json.loads(urllib.request.urlopen(f['url']).read().decode('utf-8'))
		path = rootpath + f['path']
		printlog('Get ' + path + f['filename'])
		if not os.path.exists(path):
			os.makedirs(path)
		with urllib.request.urlopen(download_url['href']) as response, open(path + f['filename'], 'wb') as out_file:
			shutil.copyfileobj(response, out_file)
		printlog('File downloaded ' + path + f['filename'])

download()
