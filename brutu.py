import mechanize
import itertools
import sys
import signal
import time  # for sleep

"""**************************************
*        Information for program        *
**************************************"""
__version__ = "0.0.1 (Beta)"
__author__ = "InfiniteRegen"
__maintainer__ = "InfiniteRegen"
__email__ = "zeroback10@ajou.ac.kr"
__status__ = "Beta"


"""**************************************
*     print out useage of this program  *
**************************************"""
def howToUse():
    print '\n' + '*' * 20 + '[USAGE]' + '*' * 20 + '\n'
    print 'python ' + sys.argv[0] + " -t '[target URL]' -r [# of loop] -s [time to sleep]" + '\n'
    print '-t: target address \t__> [necessary]'
    print '-r: # of repeat \t__> [default: 1000 times]'
    print '-s: sleeping time(sec) \t__> [default: 60 secs]'
    print '*' * 47 + '\n'
    print 'e.g) python ' + sys.argv[0] + " -t 'www.example.com/1.jsp' -r 1000" + '\n'
    return


"""**************************************
*        Define 'CTRL + C' action       *
**************************************"""
def sig_handler(signal, frame):
    print "You have entered CTRL+C"
    print "Thanks for using this program :)"
    br.close()
    sys.exit(0)
    return
signal.signal(signal.SIGINT, sig_handler)  # Registering


"""**************************************
*              Main function            *
**************************************"""

requiredArgument = 0
repeat = 1000
myUrl = ""
sleepingTime = 60 # second


if len(sys.argv) > 1:
    for x in range(1, len(sys.argv)):
        if str.lower(sys.argv[x]) == '-t': # 't' stand for 'target'
            myUrl = sys.argv[x + 1]
            if not str.startswith(myUrl, "http://") and not str.startswith(myUrl, "https://"):
                print "[*WARN] You must forget prefix like 'http://' or 'https://' !!"
                print "[*WARN] 'http://' is attached automatically...."
                myUrl = "http://" + myUrl
            requiredArgument += 1
        elif str.lower(sys.argv[x]) == '-r': # 'r' stand for 'repeat'
            repeat = int(sys.argv[x + 1])
        elif str.lower(sys.argv[x]) == '-s': # 's' stand for 'sleeping Time'
            sleepingTime = int(sys.argv[x + 1])
        elif "/?" in str.lower(sys.argv[x]) or "-help" in str.lower(sys.argv[x]):
            howToUse()
            sys.exit(0)
else:
    howToUse()
    sys.exit(0)

if requiredArgument < 1:
    print '*'*38
    print "** [ERROR] '-t' option is required. **"
    print '*'*38
    howToUse()
    sys.exit(0)

br = mechanize.Browser()
br.set_handle_equiv(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

print "The target address is [%s]" % myUrl
for x in range(1, repeat+1):
    if (x % 1000) == 0:
        print "it's going to sleep..... for %d seconds" % (sleepingTime)
        time.sleep(sleepingTime) # To pretend to normal access, not web bot.
    if (x % 100) == 0:
        print "The Target Address is [%s]" % myUrl
    print str(x) + "th iterations"

    try:
        br.open(myUrl)
    except Exception as e:
        if "can't fetch relative" in e[0]:
            print "The prefix 'http://' doesn't exist."
        sys.exit(0)
