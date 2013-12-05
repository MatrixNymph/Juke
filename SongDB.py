#!/usr/bin/env python

from mutagen.flac import FLAC
from mutagen.mp3 import MP3

import sys
import os
import fnmatch
import pickle

import ID3Reader
import CFGReader
import Song

class SongDB:
    
    def __init__(self, rootDir):
        self.root = rootDir

    def build(self):
        
        # Enumerate MP3s and FLACs in music_folder
        idList = []
        matches = []

        for filetype in ("mp3", "flac"):
            for root, dirnames, filenames in os.walk(self.root):
                for filename in fnmatch.filter(filenames, '*.' + filetype):
                    matches.append(os.path.join(root, filename))

        # Read ID3 tags
        tagged = ID3Reader.ID3Reader(matches).readID3()

        # Assign an id # to each song
        for song in tagged:
            id = len(idList) + 1
            song.id = id
   
        # Write list to a file
        outFile = open('juke.pkl', 'wb')
        pklList = []
        for song in tagged:
            pklList.append(song)
        pickle.dump(pklList, outFile)
        outFile.close()
