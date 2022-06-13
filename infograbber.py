# • Machine name
# • List of all users and the group they are associated
# with
# • From /proc/cpuinfo get the following
# o Processor
# o Vendor_id
# o Model
# o Model name
# o Cache
# • All services on machine and their current status
# • This data needs to be collected and formatted in a
# text file for easy readability.

import os # to get machine name
import pwd, grp # for users and group
import subprocess # for services



w = open("info.txt","w") # opening the file in write mode as data needs to be formatted in txt file

# hostname
# uname returns multiple infomation and we just need the machine name
# or nodename so we use [1] element in the list
# writing the machine name to a file 
w.write("MACHINE_NAME: " + os.uname()[1] + "\n")

# user and group
# pwd.getpwall() is used to get all the users
# grp.getgrgid(gid) is used to lookup their group name
w.write("\nUSER GROUP: \n")
for p in pwd.getpwall():
	user_group = p[0], grp.getgrgid(p[3])[0]
	w.write(str(user_group)+'\n')

# processor
# we open the /proc/cpuinfo and read all the lines
w.write("\n\nProcessor: \n")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

# o Processor
# o Vendor_id
# o Model
# o Model name
# o Cache

#cpu information 

def cpuinfo():
	for line in info[:9]:  # using [:9] so that i dont need to go through all the line and only print information about processor 0
			if "processor" in line:
				w.write(line)
			if "vendor_id" in line:
				w.write(line)
			if "model" in line: # this will both print model and model name and it matches the string "model"
				w.write(line)
			if "cache size" in line:
				w.write(line)
cpuinfo()		
# here i used subprocess to execute the program
# as i could not find any python library to get such information
# subprocess allows you to spawn a new process and execute the shell command and stores the output in services
# then i can print each line in services
# and store output in file
w.write("\nSERVICES: \n")
command = "systemctl list-units --type=service"
services = subprocess.check_output(command, shell=True).decode().strip()
for line in services.split('\n'):
		w.write(line+"\n")
