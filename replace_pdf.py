from fillpdf import fillpdfs
from os import walk, path, makedirs
from pathlib import Path

import sys, getopt

source_name = sys.argv[0]


def extract_file(source, template, target):
   data_dict = fillpdfs.get_form_fields(source)
   
   fillpdfs.write_fillable_pdf(template, target, data_dict)
   print(source, target)


def main(argv):
   sourcefolder = 'pdf'
   targetfile = 'target.pdf'
   targetfolder = ''
   try:
      opts, args = getopt.getopt(argv,"hi:s:t:f:",["sourcefolder=","targetfile=","targetfolder="])
   except getopt.GetoptError:
      print ('replace_pdf.exe -s <sourcefolder> -t <targetfile> -f <targetfolder>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ('replace_pdf.py -s <sourcefolder> -t <targetfile> -f <targetfolder>')
         sys.exit()
      elif opt in ("-s", "--source"):
         sourcefolder = arg
      elif opt in ("-t", "--target"):
         targetfile = arg
      elif opt in ("-f", "--targetfolder"):
         targetfolder = arg
   if targetfolder == '':
      targetfolder = sourcefolder + '_new'
   print ('Source folder is "' + sourcefolder + '"')
   print ('Target file is "' + targetfile + '"')
   print ('Target folder is "' + targetfolder + '"')
   
   f = [path.join(dirpath,f) for (dirpath, dirnames, filenames) in walk(sourcefolder) for f in filenames]
   for (sourcepath, dirnames, filenames) in walk(sourcefolder):
      for file in filenames:
         targetpath = sourcepath.replace(sourcefolder, targetfolder, 1)
         if not path.exists(targetpath):
            makedirs(targetpath)
         extract_file(path.join(sourcepath, file), targetfile, path.join(targetpath, file))

if __name__ == "__main__":
   main(sys.argv[1:])

