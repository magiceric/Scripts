"""
This simple script just find a first movie id on http://kinopoisk.ru
"""
__author__ = 'nektodev'

import urllib.request
import xml.etree.ElementTree as ET

HOST = 'http://rating.kinopoisk.ru/'


def requestURL(url):
    response = urllib.request.urlopen(url).read()
    return response.decode('utf-8')


def getRating(string):
    xml = ET.fromstring(string)
    rating = xml.find('kp_rating').text
    return rating


def main():
    for id in range(1, 1000):
        url = HOST + repr(id) + ".xml"
        rating = getRating(requestURL(url))
        if rating != '0':
            print("CONGRATULATION! First KP movie is: " + repr(id) + ", rating = " + rating)
            print("http://kinopoisk.ru/film/" + repr(id))
            break


main()