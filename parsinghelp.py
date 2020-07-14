import re
with open ("index.html", "r") as myfile:
    data=myfile.read()


nameregex = re.compile('data-name=".*"')
namelist = re.findall(nameregex ,data)
with open('country names', 'w') as filehandle:
    for listitem in namelist:
        filehandle.write('%s\n' % listitem)
print(namelist)


idregex = re.compile('data-id=".*"')
idlist = re.findall(idregex ,data)
with open('country ids', 'w') as filehandle:
    for listitem in idlist:
        filehandle.write('%s\n' % listitem)