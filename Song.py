#!/usr/bin/env python

from mutagen.id3 import ID3
from mutagen.id3 import ID3NoHeaderError

class Song:
    """ A simple object representing a song, to be used to store ID3 tag values in objects. """
    def __init__(self, fileLoc):
        self.id = ""
        self.artist = ""
        self.title = ""
        self.album = ""
        self.fileLoc = fileLoc

    def hasID3(self):
        try:
            test = ID3(self.fileLoc)
            return True
        except ID3NoHeaderError:
            return False
