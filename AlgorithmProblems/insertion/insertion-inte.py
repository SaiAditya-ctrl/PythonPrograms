

import sys
sys.path.append("/Users/Aditya/Desktop/functinal/utility")
import utility


l=[10,90,21,1,2,34,56]
s=['sai','aditya','ede','a','abc','zoo','az','boo']
print(l)
print(s)
print('before')
s1=utility.insertion_sort(l)
s2=utility.insertion_sort(s)
print(s1)
print(s2)
