import urllib2
from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(urllib2.urlopen('http://in.priceprice.com/mobilephones/').read())
#print soup
print type(soup)

a1=0
arra=[]
a2=0
arr1=[]
for i in soup.findAll('div', {"class":'itemBoxIn'}):
	#print i.a
	if i!=None:
		print i.h3.text
		a1 = a1 + 1
		arra.append(i.h3.text)
	

for i in soup.findAll('div', {"class":'itmPrice'}):
	#print i.a
	#if i!=None:
	print i.a.text
	a2 = a2 + 1
	arr1.append(i.a.text)


print arra ,arr1

for i in range(a2):
	print "Name is :",arra[i] , arr1[i]
