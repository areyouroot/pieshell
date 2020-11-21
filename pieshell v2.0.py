import subprocess
import os
import threading
import getpass
'''these are the different modules which i imported to avoid bulk coading
get user prints the current user '''
print(getpass.getuser())
print('#################\nPIESHELL\n###########')
'''this is a simple banner for the program '''
def d():#function decelatration
    while True:#infinite loop
        a = input("\"*PieShell*\"-----------| \n#[" + os.getcwd() + "]#%---#:")
#this line gets command from the user
        if a == 'exit':
            break
#if user inputs exit the program will be ended
        if a == 'powershell':
            subprocess.call(["C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe"])
#this used to intiate powershell wich is bult in windows
        if a == 'help':
            print('''hello this is help this pie shell is made by abdul faheem a from malware india
            start= to start an application
            eg start chrome
            others all commands are based on the os thank u''')
#this is a simple help with my name and in bult help is also displayed
        try:
#i have used try method to avoid errors
            if a[:5]=='start':
                print('starting'+a[5:])
                t2=threading.Thread(subprocess.run(a,shell=True))
#if a users starts a outside program this will start that new program in a new thread so that
#the shell does not get stuck
            b = subprocess.run(a, capture_output=True, shell=True, text=True)
#this is the in bult function which runs the shell commands
#i havetested this in multible os it does work in unix also and windows too
            if a[:3] == 'cd ':
                if a[3:] == '..':
                    a, b = os.path.split(os.getcwd())
                    del b
                    os.chdir(a)
                    continue
                else:
                    os.chdir(a[3:])
                    continue
#some times cd is not able to access out side the given scope because the sub prosss module does not
#have a in bult file path so os command is used here
            # if b.returncode == 1:
            #     print("invalid command")
            #     continue
#the above commands are my trial and error commands which is commented out
            print(b.stdout)#this print output
            print(b.stderr)#this error
        except:
            if a[:6]=='start ':
                print("checking the program status")
                print('b.stderr')
                continue #in starting an application we get some prosses error because the tread is over loaded
                #so i have this pice of code here
            else:
                print("## check the input ##")
                continue
#if any internal error occur then this will end up
t1=threading.Thread(d())#this command intiate the program
