
minimum = 5 
# disk space variation (in GB) threshhold. 'delta GB have been consumed between the last two checks'.
delta = 1

import commands
import pickle

try:
    f = open('/root/scripts/diskfree.dat', 'r')
    before = pickle.load(f)
    f.close()
except IOError: # ie. file not found
    before = None

r = commands.getstatusoutput('df')
if r[0] == 0:
    lines = r[1].split('\n')
    del lines[0]
    for line in lines:
        fs, size, used, available, percent, mp = line.split()
        if mp != '/':
            continue
        available = int(available)
        f = open('/root/scripts/diskfree.dat', 'w')
        pickle.dump(available, f)
        f.close()
        if available < (1048576 * minimum):
            print ("Less tham %sGB of free space left!" % minimum)
            if before is not None:
                variation = available - before
                if variation > (1048576 * delta):
                    vgb = variation / 1048576.0
                    print ("In the period between the last two checks, disk usage has grown in %sGB" %vgb)