# -- coding: utf-8 --

### fix ChangeTemplate

#imports
import os
import re

#define variables
CUSTOMIZATION = []
TEMPLATE = ''
CONFIG = ""
path = os.path.dirname(os.path.abspath(__file__)) #get current directory

#Define functions
#load template
def LoadTemplate():
	f = open('%s/template.cfg' % path,'r')
	template = f.read()
	f.close()
	return template

#load customizations
def LoadCustomizations():
	i=0
	customization = []
	customizations = open('%s/customizations.cfg' % path, 'r')
	for line in customizations:
		temp = [line.replace("\n", "")]
		customization.append(temp)
		i +=1

	customizations.close()
	return customization

#change template
def ChangeTemplate(template1, array1):
	i=0
	reg_before = "(=.*$|\[\')"
	reg_after = "(^.*=|\'\])"
	for custom in array1:
		temp = "%s" % array1[i]
		template1 = template1.replace(re.sub( reg_before,'', temp), re.sub( reg_after,'', temp))
		i +=1

	return template1

def WriteConfig(string1,string2):
	#write config file
	config = open('%s/output.cfg' % string2 ,'w')
	config.write("%s" % string1)
	config.close()

	return 1

#Main program
os.system('clear')	#Clear screen

print "Loading template..."
TEMPLATE = LoadTemplate()

print "Loading customizations..."
CUSTOMIZATION = LoadCustomizations()

print "Creating config..."
CONFIG = ChangeTemplate( TEMPLATE, CUSTOMIZATION )

print "writing config...\n"
WriteConfig(CONFIG, path)

#done
print "done, your config output.cfg is in %s" % path