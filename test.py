import requests
import json
from bs4 import BeautifulSoup

dep = input("Enter department code in 2 letters. e.g. MA/CS/GG ")
filename = dep+'.csv'
f=open(filename,'w')
for yr in range(15,10,-1):
    for stu in range(1,61):
        j = str(stu).rjust(2, '0')
        k = str(yr)
        rollno = k+dep+"200"+j
        url = "https://erp.iitkgp.ernet.in/StudentPerformance/view_performance.jsp?rollno="+rollno
        content = requests.get(url)
        soup = BeautifulSoup(content.text, 'lxml')

        sgpa = soup.find_all("b",string = "SGPA")
        cgpa = soup.find_all("b",string = " CGPA")
        sgpa.reverse()
        cgpa.reverse()
        #print(cgpa)
        for i,j in zip(sgpa,cgpa):
            i = i.find_parent("td")
            i = i.find_next_sibling("td")
            i = i.string
            j = j.find_parent("td")
            j = j.find_next_sibling("td")
            j = j.string
            #print(type(i))
            #print(i+' '+j+',')
            f.write(i+' '+j+',')
            #f.write('done,')
        f.write('\n') 
        if(stu%5==0):
            print(stu,'done')
    print(yr,' year done')
f.close()
print('Done!')
