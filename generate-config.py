# -- coding: utf-8 --

#sort out regexes in replacements!!!


#get current directory
import os
import re
path = os.path.dirname(os.path.abspath(__file__))

#load customizations
hostname = "RTEM00000FW001"


#open template
template = open('%s/template.cfg' % path,'r')
workingtemplate = template.read()
template.close()

#load customizations


i=0
customization = []
customizations = open('%s/customizations.cfg' % path, 'r')
for line in customizations:
	temp = [line.replace("\n", "")]
	customization.append(temp)
	print customization[i]
	i +=1


customizations.close()

#customize template

i=0
reg_before = "(=.*$|\[\')"
reg_after = "(^.*=|\'\])"
for replace in customization:
	temp = "%s" % customization[i]
	print "translate %s  to %s" % (re.sub('%s' % reg_before,'', temp), re.sub('%s' % reg_after,'', temp))
	workingtemplate = workingtemplate.replace(re.sub('%s' % reg_before,'', temp), re.sub('%s' % reg_after,'', temp))
	i +=1

#write config file
config = open('%s/%s.cfg' % (path, hostname) ,'w')
config.write("%s" % workingtemplate)
config.close()

#done
print "done, your config %s.cfg is in %s" % (hostname, path)