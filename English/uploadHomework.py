import urllib.request
import json
import shutil

files = [{ 
	'url' : 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%3D&path=%2Fhomework%2Frevision%2Fvocabulary%2Fpractice-and-check.html',
	'path': '/usr/share/nginx/html/vocabulary.html'
}, 
{
	'url' : 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%3D&path=%2Fhomework%2Frevision%2Fpronunciation%2FDasha%2Fpractice-and-check.html',
	'path': '/usr/share/nginx/html/dasha/pronunciation.html'
},
{
	'url': 'https://cloud-api.yandex.net:443/v1/disk/public/resources/download?public_key=jDY08AP3zoSUx80EWqOBhduCV9KPdOMM41xsUOmKI7o%3D&path=%2Fhomework%2Frevision%2Fpronunciation%2FSlava%2Fpractice-and-check.html',
	'path': '/usr/share/nginx/html/slava/pronunciation.html'
}]

for f in files: 
	download_url = json.loads(urllib.request.urlopen(f['url']).read().decode('utf-8'))
	with urllib.request.urlopen(download_url['href']) as response, open(f['path'], 'wb') as out_file:
		shutil.copyfileobj(response, out_file)

