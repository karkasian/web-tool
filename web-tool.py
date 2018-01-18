#!usr/bin/python
import os,time,sys,platform,urllib
def funstr():
                print """Select Your Tool ...

1) Admin Page Finder
2) Shell Finder
3) Uploader Finder
4) phpMyAdmin Finder
5) Directory Finder
0) Exit
                """
                var1 = 0
                var2 = 0
                qu = int(raw_input("Pentest_tools ==> "))
                if qu == 1:
                                os.system(y)
                                print "Enter Url For Scanning...\n"
                                qu2 = raw_input('Pentest_tools ==> ')
                                fr = open('admins.txt','r').readlines()
                                for admins in fr:
                                                if urllib.urlopen(qu2+'/'+admins.replace('\n','')).code == 200:
                                                                
                                                                print "\n\n                      Page Finded! "+ qu2+'/'+admins.replace('\n','') +"\n\n"
                                                                os.system("echo "+str(qu2+'/'+admins.replace('\n',''))+" is code 200"+" >> autosave.txt")
                                                                print "\nPress Enter to Continue ...\n"
                                                                raw_input('pentest_tools ==> ')
                                                                var1 += 1
                                                elif urllib.urlopen(qu2+'/'+admins.replace('\n','')).code == 302:
                                                                
                                                                print "\n\n                      Possible admin page (302 - Redirect) "+ admins +"\n\n"
                                                                os.system("echo "+str(qu2+'/'+admins.replace('\n',''))+" code is 302 "+" >> autosave.txt")
                                                                print "\nPress Enter to Continue ...\n"
                                                                raw_input('pentest_tools ==> ')
                                                                var2 += 1
                                                else:
                                                                
                                                                print"Testing Url ==> "+qu2+'/'+admins.replace('\n','')
                                                
                                print "Ended ! Finded "+str(var1)+" and Redirect "+str(var2)+" and total checked "+str(len(fr))+".saved to autosave.txt"
                                time.sleep(10)
                                exit()
                elif qu ==2:
                                os.system(y)
                                print "Enter Url For Scanning...\n"
                                qu2 = raw_input('Pentest_tools ==> ')
                                fr = open('shells.txt','r').readlines()
                                for shells in fr:
                                                if urllib.urlopen(qu2+'/'+shells.replace('\n','')).code == 200:
                                                                
                                                                print "\n\n                      shell Finded! "+ qu2+'/'+shells.replace('\n','') +"\n\n"
                                                                os.system("echo "+str(qu2+'/'+shell.replace('\n',''))+" is code 200"+" >> autosave.txt")
                                                                print "\nPress Enter to Continue ...\n"
                                                                raw_input('pentest_tools ==> ')
                                                                var1 += 1
                                                else:
                                                                
                                                                print"Testing Url ==> "+qu2+'/'+shells.replace('\n','')
                                                
                                print "Ended ! Finded "+str(var1)+" and total checked "+str(len(fr))+".saved to autosave.txt"
                                time.sleep(10)
                                exit()
                elif qu == 3:
                                os.system(y)
                                print "Enter Url For Scanning...\n"
                                qu2 = raw_input('Pentest_tools ==> ')
                                fr = open('uploaders.txt','r').readlines()
                                for uploaders in fr:
                                                if urllib.urlopen(qu2+'/'+uploaders.replace('\n','')).code == 200:
                                                                
                                                                print "\n\n                      Uploader Finded! "+ qu2+'/'+uploaders.replace('\n','') +"\n\n"
                                                                os.system("echo "+str(qu2+'/'+uploaders.replace('\n',''))+" is code 200"+" >> autosave.txt")
                                                                print "\nPress Enter to Continue ...\n"
                                                                raw_input('pentest_tools ==> ')
                                                                var1 += 1
                                                else:
                                                                
                                                                print"Testing Url ==> "+qu2+'/'+uploaders.replace('\n','')
                                                
                                print "Ended ! Finded "+str(var1)+" and total checked "+str(len(fr))+".saved to autosave.txt"
                                time.sleep(10)
                                exit()
                elif qu == 4:
                                os.system(y)
                                print "Enter Url For Scanning...\n"
                                qu2 = raw_input('Pentest_tools ==> ')
                                fr = open('phpMyAdmin.txt','r').readlines()
                                for phpMyAdmin in fr:
                                                if urllib.urlopen(qu2+'/'+phpMyAdmin.replace('\n','')).code == 200:
                                                                
                                                                print "\n\n                      phpMyAdmin Finded! "+ qu2+'/'+phpMyAdmin.replace('\n','') +"\n\n"
                                                                os.system("echo "+str(qu2+'/'+phpMyAdmin.replace('\n',''))+" is code 200"+" >> autosave.txt")
                                                                print "\nPress Enter to Continue ...\n"
                                                                raw_input('pentest_tools ==> ')
                                                                var1 += 1
                                                elif urllib.urlopen(qu2+'/'+phpMyAdmin.replace('\n','')).code == 302:
                                                                
                                                                print "\n\n                      Possible phpMyAdmin page (302 - Redirect) "+ phpMyAdmin +"\n\n"
                                                                os.system("echo "+str(qu2+'/'+phpMyAdmin.replace('\n',''))+" code is 302 "+" >> autosave.txt")
                                                                print "\nPress Enter to Continue ...\n"
                                                                raw_input('pentest_tools ==> ')
                                                                var2 += 1
                                                else:
                                                                
                                                                print"Testing Url ==> "+qu2+'/'+phpMyAdmin.replace('\n','')
                                                os.system(y)
                                print "Ended ! Finded "+str(var1)+" and Redirect "+str(var2)+" and total checked "+str(len(fr))+".saved to autosave.txt"
                                time.sleep(10)
                                exit()
                elif qu == 5:
                                os.system(y)
                                print "Enter Url For Scanning...\n"
                                qu2 = raw_input('Pentest_tools ==> ')
                                fr = open('directory.txt','r').readlines()
                                counter = 0
                                for directory in fr:
                                                if urllib.urlopen(qu2+'/'+directory.replace('\n','')).code == 200:
                                                                
                                                                print "\n\n                      directory Finded! "+ qu2+'/'+directory.replace('\n','') +"\n\n"
                                                                os.system("echo "+str(qu2+'/'+directory.replace('\n',''))+" is code 200"+" >> autosave.txt")
                                                                var1 += 1
                                                elif urllib.urlopen(qu2+'/'+directory.replace('\n','')).code == 302:
                                                                os.system(y)
                                                                print "\n\n                      Possible directory page (302 - Redirect) "+ directory +"\n\n"
                                                                os.system("echo "+str(qu2+'/'+directory.replace('\n',''))+" code is 302 "+" >> autosave.txt")
                                                                var2 += 1
                                                else:
                                                                counter +=1
                                                                print"%"+str(counter*100//len(fr))+" Testing Url ==> "+qu2+'/'+directory.replace('\n','')
                                                
                                print "Ended ! Finded "+str(var1)+" and Redirect "+str(var2)+" and total checked "+str(len(fr))+".saved to autosave.txt"
                                time.sleep(10)
                                exit()
                elif qu == 0:
                                os.system(y)
                                print "Good Bye ..."
                                time.sleep(1)
                                exit()
                else:
                                os.system(y)
                                print "Error! Select number as Menu."
                                time.sleep(2)
                                funstr()
if platform.uname()[0] == "Windows":
                x = 'color a'
                y = 'cls'
elif platform.uname()[0] == "linux":
                x = ''
                y = 'clear'
else :
                print "platform not found!"
                time.sleep(2)
                exit()
os.system(x)
os.system(y)
print """
#########################################
         in the name of allah      
              Web Tools                  
                author:                   
           MOHAMMAD8500        
      version: 1.0(for windows and linux)  
#########################################
"""
time.sleep(5)
os.system(y)
funstr()
