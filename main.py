
import subprocess as x
def shell():
    try:
        a=int(input("enter ur choice \n1)bash\n2)pws\n3-n)cmd\n"))
        if(a==1):
            print("starting bash")

            x.call("bash", shell=True)
            x.call("/bin/bash", shell=True)
            print("exiting bash"*10)
        elif(a==2):
            print("starting the powershell")
            x.call(" C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe", shell=True)
        else:
            print ("this choice is for cmd")
            x.call("cmd", shell="True")
    except:
        print("error occoured")
shell()
