#!/usr/bin/env python
#*-* coding: utf-8 *-*
import os.path
import sys



def remove_line(fileName):
    word = 'skipped'
    phrase ='RINEX FILE SPLICE '
    phrase_fullday = "COGO code"
    fileName_split = fileName.split(os.sep)
    newFile = rinex_files_path + 'MODIFIED_' + fileName_split[-1]
    
    with open(fileName, 'r+') as RINEXfile:
        contents = RINEXfile.readlines()
        RINEXfile.close()
        modifiedRINEXfile = open(newFile, 'w')

        for lineNumber, line in enumerate(contents):
            if phrase in line:
                del contents[lineNumber -1: lineNumber +3]  
            elif phrase_fullday in line:
                del contents[lineNumber -1: lineNumber +5]  
                      
        modifiedRINEXfile.writelines(contents)
        modifiedRINEXfile.close()
    
    print "Editing finished."

workspacePath = os.getcwd()
pathList = workspacePath.split(os.sep)
RINEX_filename = 'wgtn3180_GPS.16o' 


if 'iMac' in pathList:
    rinex_files_path = '<your_path>' 
else:
    rinex_files_path = '<your_path>'

selected_rinex = rinex_files_path + RINEX_filename
remove_line(selected_rinex)  

