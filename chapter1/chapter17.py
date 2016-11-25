import re

#1-17
pattern = '(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
statistics = dict(Mon=0, Tue=0, Wed=0, Thu=0, Fri=0, Sat=0, Sun=0)
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(pattern, line)
        if match:
            statistics[match.group(1)] += 1
print statistics

#1-18
pattern = '(Mon|Tue|Wed|Thu|Fri|Sat|Sun)\s\w{3}\s(?:(?:[0-2][0-9])|3[0-1])\s(([01][0-9])|[2][0-3])'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(pattern, line)
        if match:
            print line
        else:
            print "error"

#1-19
pattern = '.+?(\d{2}:\d{2}:\d{2})'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(pattern, line)
        if match:
            print match.groups(1)
        else:
            print "error"

#1-20
pattern = '.+?::(.*)::'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(pattern, line)
        if match:
            print match.groups(1)
        else:
            print "error"

#1-21
pattern = '.+?\s(\w{3})'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(pattern, line)
        if match:
            print match.groups(1)
        else:
            print "error"

#1-22
pattern = '.+?\s\w{3}\s(\d{2})'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(pattern, line)
        if match:
            print match.groups(1)
        else:
            print "error"

#1-23
patternTime = '.+?(\d{2}:\d{2}:\d{2})'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(patternTime, line)
        if match:
            print match.groups(1)
        else:
            print "error"

#1-24
patternDomain = '.+?@(.*)::'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(patternDomain, line)
        if match:
            print match.groups(1)
        else:
            print "error"

#1-25
patternEachDomain = '.+?@(\w+)\.(\w+)::'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(patternEachDomain, line)
        if match:
            print match.groups(1)
        else:
            print "error"

#1-26
patternMail = '(?<=::)(.*)(?=::)'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.sub(patternMail, 'fengbobao@163.com', line)
        if match:
            print match
        else:
            print "error"

#1-27
print "1-27"
patternDate = '^\w{3}\s(\w{3})\s(\d{2}).+?\s(\d{4})::'
#patternDate = '^\w{3}\s(\w{3})\s(\d2).+?'
with open('redata.txt', 'r') as rf:
    for line in rf:
        match = re.match(patternDate, line)
        if match:
            print '%s, %s, %s' %(match.group(1), match.group(2), match.group(3))
        else:
            print "error"









