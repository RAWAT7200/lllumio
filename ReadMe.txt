Hello and Greetings,
My name is:SURAJ RAWAT/rawat7200@gmail.com

For implementation I have created a Firewall class and then initalised and based on file path connected the csv file with file_pointer and used csv reader to read files from it.
Second,To check for every possible scenarios I have thus created different fucntion by the name of 'checkIpAddres','checkPort' and so on for readability.
Thirdly,I did testing on my own for some test cases for which program could lead to bad behaviour.
To handle some bad scenarios I used Exception which handle this situation by returning a simple 'False' as output.

From my point exception or bad cases could be generated in following ways:
1)Filename not specified correctly.
2)Exception while casting string to int.
3)Wrong input type passed

Apart from these issues:
 #How to speedup this process of checking for each possible set of inputs?
 My idea:Use a mapping mechanism to store the ip address and port numbers of frequently arriving/dispatching packets.
         For instance,video streaming requires connection to be persistently established and same packets with same ip address and ports.We need to make entries for each only one time
         in this continious streaming.

Comments for Program
/*-------
Greetings .Please Find my implementation of Firewall Class
Line 83-92:Asks for input file.If input file/path is incorrect exception is generated.
Line 34 - 43 :checks for input size first .input size must satisfy size>1  and  <=2 constraint.
              then checks for port numbers if in range.
              If input can't be casted to int or overflows aa exception is generated.False is returned.
Line 50-82:checks for ip_address of length either one or two(for range).They are further splitted and checked for constraints.
------*/


/**-----------***/

I would definitely like to be a part of Platform team.As the work aligns with my past exeprience/project, which I did last semester on AWS cloud.
We used aws to manage server and used AWS for load balancing and monitoring server and generating health reports for server.
 