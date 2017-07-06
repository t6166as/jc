#!/usr/bin/python
import argparse as a
import math
## Create parser
parser = a.ArgumentParser(description="Calculate the volume of a Cylinder")
## Add Arguments to the parser
parser.add_argument('-r','--radius',type=int,help='radius of the cylinder')
parser.add_argument('-H','--height',type=int,help='height of the cylinder')
## parse the arguments
args=parser.parse_args()
## define function
def cylinder_volume(radius, height):
 vol=(math.pi)*(radius**2)*(height)
 return vol
## if this file is run then its name is main and then go ahead and execute following steps. 
if __name__ == '__main__': 
 volume=cylinder_volume(args.radius, args.height)
 print volume
