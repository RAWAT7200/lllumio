
import csv
"""
SURAJ RAWAT
rawat7200@gmail.com

Greetings .Please Find my implementation of Firewall Class
Line 83-92:Asks for input file.If input file/path is incorrect exception is generated.
Line 34 - 43 :checks for input size first .input size must satisfy size>1  and  <=2 constraint.
              then checks for port numbers if in range.
              If input can't be casted to int or overflows aa exception is generated.False is returned.
Line 50-82:checks for ip_address of length either one or two(for range).They are further splitted and checked for constraints.
"""
class Firewall:
  file_p=None
  readFile=None
  def __init__(self,pathname):
    self.file_p=open(pathname)
    self.readFile=csv.reader(self.file_p,delimiter=',')

     
  def accept_packet(self,direction,protocol,port,ip_address):
 	  result=self.checkProtocol(protocol) and self.checkPort(port) and self.checkIpAddress(ip_address) and self.checkDirection(direction)
 	  print(result)


  def checkDirection(self,direction):
    if direction=='inbound' or direction=='outbound':
      return True
    return False


  def checkProtocol(self,protocol):
    if protocol=='tcp' or protocol=='udp':
      return True
    return False


  def checkPort(self,port):
    try:
      n_input=port.split('-')
      if len(n_input)==1:
        if int(n_input[0])>=1 and int(n_input[0])<=65535:
          return True
        return False
      elif len(n_input)==2:
        return (int(n_input[0])>=1 and int(n_input[0])) and (int(n_input[1])>=1 and int(n_input[1])<=65535)
    except :
      return False


  def checkIpAddress(self,ip_address):
    try:
       n_input=ip_address.split('-')
       if len(n_input)==1:
          st1=n_input[0].split('.')
          if len(st1)==4:
          	for subnet in st1:
          		if not(int(subnet)>=0 and int(subnet)<=255):
          			return False

          	return True

          return False
       elif len(n_input)==2:
       	  st1=n_input[0].split('.')
       	  st2=n_input[1].split('.')
       	  check1=True
       	  check2=True
          if len(st1)==4:
          	for subnet in st1:
          		if not(int(subnet)>=0 and int(subnet)<=255):
          			check1=False

          if len(st1)==4:
          	for subnet in st1:
          		if not(int(subnet)>=0 and int(subnet)<=255):
          			check2=False

          return check1 and check2
    except :
    	return False

    return False

try:
  pl=Firewall('fs.csv')
  for row in pl.readFile:
    direction=str(row[0])
    protocol=str(row[1])
    port=str(row[2])
    ip_address=str(row[3])
    pl.accept_packet(direction,protocol,port,ip_address)
except :
   print('Error Reading File') 
 
		


                         	
   

		

