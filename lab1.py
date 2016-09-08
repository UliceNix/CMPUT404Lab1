import requests

# Question 2, 3, 4
print requests.__version__

# Question 6
r = requests.get('http://google.com')
print 'Question 6: ' + str(r.status_code)

# Question 7
r = requests.post('http://ccid-eddieantonio.rhcloud.com/mingxun')
print 'Question 7: ' + str(r.status_code)

# Question 8
r = requests.get('https://raw.githubusercontent.com/UliceNix/CMPUT404Lab1/master/lab1.py')
print 'Question 8: \n' + str(r.content)


#import os
#os.system('curl -iLX GET http://google.com')
#os.system('curl -iX POST http://ccid-eddieantonio.rhcloud.com/mingxun')
#os.system('curl https://raw.githubusercontent.com/UliceNix/CMPUT404Lab1/master/lab1.py')
