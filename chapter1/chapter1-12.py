import re
#1-1
pattern = '([bh][aiu]t)'
match =  re.match(pattern, 'bita')
print match.groups()

#1-2
pattern = '(\w+ \w+)'
match =  re.match(pattern, 'I am waiting for you')
print match.groups()

#1-13
pattern = '^<type \'([\w\d_]+)\'>'
match = re.match(pattern, str(type(dir)))
if match:
    print match.groups()

#1-14
pattern = '((?:0?[1-9])|(?:1[012]))$'
#pattern = '(1[012])'
months = ['01', '02', '03','04', '05','06','07','08','09','10','11','12','13','00','20','21','1']
for m in months:
    match = re.match(pattern, m)
    if match:
        print match.groups()

#1-15
pattern = '(^\d{4}-\d{6}-\d{4}$)|^(\d{4}-\d{4}-\d{4}-\d{4})$'
data = ('1111-111111-1111', '1111-2222-1111-2222', '11211-111111-1111', '1111-2222-3333-44444')
for line in data:
#    print line
    m = re.match(pattern, line)
    if m:
        print m.groups()