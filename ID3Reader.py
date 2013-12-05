#!/usr/bin/env python

from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.id3 import ID3
from mutagen.id3 import ID3NoHeaderError

import Song
import sys

class ID3Reader:
    """ A simple class to return requested ID3 tag values. """
    def __init__(self, fileLocs):
        self.fileLocs = fileLocs

    def readID3(self):
        retList = []
        
        for file in self.fileLocs:
            ret = Song.Song(file)
            
            if ret.hasID3() == True:
                temp = ID3(ret.fileLoc)
            else:
                continue
            
            if not ('TIT' in temp.pprint()):
                continue
            if 'TPE1' in temp.pprint():
                ret.artist = str(temp.getall('TPE1')[0]).split("\'")[0].replace("'","''")
            if 'TIT1' in temp.pprint():
                ret.title = str(temp.getall('TIT1')[0]).split("\'")[0].replace("'","''")
            if 'TIT2' in temp.pprint():
                ret.title = str(temp.getall('TIT2')[0]).split("\'")[0].replace("'","''")
            if 'TALB' in temp.pprint():
                ret.album = str(temp.getall('TALB')[0]).split("\'")[0].replace("'","''")
                               
            retList.append(ret)
        
        return retList
