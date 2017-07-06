#!/usr/bin/python
import ConfigParser
 
def config(filename='/home/j1axs01/jc/test.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser.ConfigParser()
    # read config file
    parser.read(filename)
    print( parser.sections())
if __name__ == '__main__':
  config()
