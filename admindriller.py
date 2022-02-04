import requests 
import threading 
import argparse 

parser = argparse.ArgumentParser() 


parser.add_argument("-u", help="target url", dest='target')
parser.add_argument("--path", help="custom path prefix", dest='prefix')
parser.add_argument("--type", help="set the type i.e. html, asp, php", dest='type')
parser.add_argument("--fast", help="uses multithreading", dest='fast', action="store_true")
args = parser.parse_args() 

target = args.target 


print ('''\033[1;34m

                                         ./shdmmdhy+-
                                      `/dMMMMMMMMMMMMmo`
                                     .dMMMMMMMMMMMMMMMMN/
                                    .NMMMMMMMMMMMMMMMMMMM+
                                    yMMMMMMMMMMMMMMMMMMMMM.
                                    NMMMMMMMMMMMMMMMMMMMMM:
                                    dMMMMMMMMMMMMMMMMMMMMM.
                                    :MMMMMMMMMMMMMMMMMMMMs
                                     :NMMMMMMMMMMMMMMMMMs`
                                      `sNMMMMMMMMMMMMMh-
                                        `:dMMMMMMMMM+.
                                      .:osmMMMMMMMMMyo/-`    oNNy
                                   -smMMMMMMMMMMMh+/+ys-   `-yMMd-`
                                 -hMMMMMMMMMMMMM/  `    :smMMMMMMMMmy/`   `
                                +MMMMMMMMMMMMMM:  :Ndo+mMMNy+:--:+smMMN+odN/
                               +MMMMMMMMMMMMMMm`  +hMMMMm/`         :dMMMMdo`
                              .MMMMMMMMMMMMMMMMd/   oMMm`            `hMMh
                              yMMMMMMMMMMMMMMMMMm   NMM:              .MMM.
                             `NMMMMMMMMMMMMMMMMMm   NMM:              `MMM.
                             .MMMMMMMMMMMMMMMMMNs`  yMMh`             oMMd
                             -MMMMMMMMMMMMMMMMN`  -odMMMh.          .yMMMms:`
                             :MMMMMMMMMMMMMMMMN.  +MMhyMMMh+-````-/yMMMyhNMs`
                             .mMMMMMMMMMMMMMMMMN-  -`  .odMMMMMMMMMMms.  `-
                              `/hNMMMMMMMMMMMMMMNo:.-o/`  `:+hMMm+:.
                                  .:/osyhdmmNNNNNNmmddhs:    oMMh
                                                             `...



                          ___      _           _        ______      _ _ _
                         / _ \    | |         (_)       |  _  \    (_) | |
                        / /_\ \ __| |_ __ ___  _ _ __   | | | |_ __ _| | | ___ _ __
                        |  _  |/ _` | '_ ` _ \| | '_ \  | | | | '__| | | |/ _ \ '__|
                        | | | | (_| | | | | | | | | | | | |/ /| |  | | | |  __/ |
                        \_| |_/\__,_|_| |_| |_|_|_| |_| |___/ |_|  |_|_|_|\___|_|

                          It's a Simple Python  script to find admin login pages

						[Version: 2.1-Stable]
                               [Tools Desingned By  Nixie_Bytes Security Team] ''')


print ('\033[1;31m-------------------------------------------------------------------------------------------------------------\033[1;m\n')

try:
	target = target.replace('https://', '') 
except:
	print ('\033[1;31m[-]\033[1;m -u argument is not supplied. Enter Admindriller  -h for help')
	quit()

target = target.replace('http://', '') 
target = target.replace('/', '') 
target = 'http://' + target 
if args.prefix != None:
	target = target + args.prefix
try:
	r = requests.get(target + '/robots.txt') #
	if '<html>' in r.text:
		print ('  \033[1;31m[-]\033[1;m Robots.txt not found\n')
	else: 
		print ('  \033[1;32m[+]\033[0m Robots.txt found. Check for any interesting entry\n')
		print (r.text)
except: 
	print ('  \033[1;31m[-]\033[1;m Robots.txt not found\n')
print ('\033[1;31m--------------------------------------------------------------------------\033[1;m\n')

def scan(links):
	for link in links: 
		link = target + link 
		r = requests.get(link) 
		http = r.status_code 
		if http == 200: 
			print ('  \033[1;32m[+]\033[0m Admin panel found: %s'% link)
		elif http == 404: 
			print ('  \033[1;31m[-]\033[1;m %s'% link)
		elif http == 302: 
			print ('  \033[1;32m[+]\033[0m Potential EAR vulnerability found : ' + link)
		else:
			print ('  \033[1;31m[-]\033[1;m %s'% link)
paths = [] 
def get_paths(type):
    try:
        with open('adminlist.txt','r') as wordlist: 
            for path in wordlist: 
                path = str(path.replace("\n",""))
                try:
            		if 'asp' in type:
            			if 'html' in path or 'php' in path:
            				pass
                		else:
               	 			paths.append(path)
                	if 'php' in type:
                		if 'asp' in path or 'html' in path:
                			pass
                		else:
                			paths.append(path)
                	if 'html' in type:
                		if 'asp' in path or 'php' in path:
                			pass
                		else:
                			paths.append(path)
                except:
                	paths.append(path)
    except IOError:
        print ('\033[1;31m[-]\033[1;m Wordlist not found!')
        quit()

if args.fast == True: 
	type = args.type 
	get_paths(type) 
	paths1 = paths[:len(paths)/2] 
	paths2 = paths[len(paths)/2:] 
	def part1():
		links = paths1 
		scan(links) 
	def part2():
		links = paths2 
		scan(links) 
	t1 = threading.Thread(target=part1) 
	t2 = threading.Thread(target=part2) 
	t1.start() 
	t2.start() 
	t1.join()
	t2.join() 
else: 
	type = args.type
	get_paths(type)
	links = paths
	scan(links)
