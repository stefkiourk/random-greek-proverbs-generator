# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from sys import exit
from random import choice
from urllib2 import urlopen

def random_proverbs():
    proverbs = []
    url = "<url to .xml>"

    tree = ET.parse( urlopen( url ) )
    root = tree.getroot()

    for proverb in root.findall( 'proverb' ):
        proverbs.append( proverb.text )
 
    return ( choice(proverbs).split(",")[0], choice(proverbs).split(",")[1] )
 
def main():
    print "\"%s, %s\"" % random_proverbs()
    return 0

if __name__ == "__main__":
    exit( main() )
