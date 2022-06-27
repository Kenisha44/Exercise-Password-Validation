import re 
#regular expressions good for 
 
import re
pattern = re.compile(	
r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)") #for email validation
string = 'b@b.com'
pattern2 = re.compile(r"[A-Za-z0-9%#@]{8,}\d")
password = "fklsdgk%8"

a = pattern.search(string)
check = pattern2.fullmatch(password)

b = pattern.findall(string) # gives instances of this 
c = pattern.fullmatch(string) #none it has to be the exact string. 
d = pattern.match(string) 
print(check)

