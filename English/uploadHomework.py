import urllib.request
import json
import shutil
import os
import datetime

rootpath = os.environ['$ENGLISH_PATH']
files = [
	{
		'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%3D&path=%2Fhomework%2Frevision%2Fvocabulary%2Fpractice-and-check.html',
		'path': '',
		'filename': 'vocabulary.html'
	},
	{
		'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%3D&path=%2Fhomework%2Frevision%2Fpronunciation%2FDasha%2Fpractice-and-check.html',
		'path': 'dasha/',
		'filename': 'pronunciation.html'
	},
	{
		'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%3D&path=%2Fhomework%2Frevision%2Fpronunciation%2FSlava%2Fpractice-and-check.html',
		'path': 'slava/',
		'filename': 'pronunciation.html'
	}
]
checkUrl = 'https://cloud-api.yandex.net:443/v1/disk/public/resources?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%3D&fields=modified&path=%2Fhomework%2Frevision%2Fvocabulary%2Fpractice-and-check.html'

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

def isFileUpdated():
	printlog('Check for updates')

	modified = json.loads(urllib.request.urlopen(checkUrl).read().decode('utf-8'))['modified'];
	printlog('Modified server date = ' + modified)
	last_modified = ''
	if os.path.exists('modified.date'):
		f = open('modified.date', 'r')
		last_modified = f.read()
		f.close
	printlog('Modified local date = ' + last_modified)
	if (modified == last_modified):
		printlog('Files not modified')
		return False
	else:
		f = open('modified.date', 'w')
		f.write(modified)
		f.close()
		printlog('Files were modified')
		return True

if (isFileUpdated()):
	download()