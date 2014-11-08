#!/usr/bin/python2
import os,random,string,re,sys

def rand_str(length=10):
    chars = string.ascii_letters + string.digits + ' -_'
    random.seed = (os.urandom(1024))
    return ''.join(random.choice(chars) for i in range(length))

if len(sys.argv) != 2:
    print(sys.argv[0] + " ~/.taskrc/pending.data")
    sys.exit()
projects={}

for line in open(sys.argv[1]):
    m=re.search(r'project:"(.*?)"',line)
    if m!= None:
        project=m.group(1)
        r_str=rand_str()
        p_name=projects.get(project,r_str)
        projects[project]=r_str
        line=re.sub(r'project:"(.*?)"','project:"' + p_name + '"',line)
    line=re.sub(r'description:".*?"','description:"' + rand_str() +'"',line)
    line=re.sub(r'annotation_(.*?):".*?"',r'annotation_\1:"' + rand_str() +'"',line)
    print line
