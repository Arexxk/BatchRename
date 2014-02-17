#!/usr/bin/python
import os
import sys

def main(argv):
  if(len(argv) != 3):
    print 'usage: renameBatch \"path\" \"search_exp\" \"replacement_string\"'

  path = argv[0]
  if(path[len(path) - 1] != '\/'):
    path = path + '\/'
  srch = argv[1]
  rplc = argv[2]
  file_str = ''
  file_str = os.popen('ls ./' + path + '|grep ' + srch).read().split('\n')
  file_list = file_str[:len(file_str) - 1]

  #CORRECTION LOOP -START-
  while(1):
    i = 0
    for filename in file_list:
      print '[' + str(i) + '] ' + filename + ' ---> ' + filename.replace(srch, rplc)
      i += 1
    
    corrections = raw_input('Enter the entries that are incorrect (if applicable): ')

    if(not corrections):
      break

    correction_list = corrections.split(" ")
    correction_list.sort()
    
    proceed = str(raw_input('Proceed with correcting ' + str(corrections) + '?[y/n]'))

    while len(correction_list):
      if(proceed == 'y'):
        file_list.remove(file_list[int(correction_list.pop())])
  #CORRECTION LOOP -END-

  #RENAME LOOP -START-
  for filename in file_list:
    os.system('mv ' + path + filename + ' ' + path + filename.replace(srch, rplc) )
  #RENAME LOOP -END-
  

if __name__ == "__main__":
  main(sys.argv[1:])
