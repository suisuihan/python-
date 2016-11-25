import re

#1-28
pattern = '(\d{3}-)?\d{3}-\d{4}'
phoneNums = ['800-555-1212', '11-555-1212', '555-1212']
for phone in phoneNums:
    if re.match(pattern, phone):
        print "match"
    else:
        print "not match"

#1-29
print "1-29"
pattern = '(\(\d{3}\)-|(\d{3}-))?\d{3}-\d{4}'
phoneNums = ['800-555-1212', '(811)-555-1212', '555-1212']
for phone in phoneNums:
    if re.match(pattern, phone):
        print "match"
    else:
        print "not match"


