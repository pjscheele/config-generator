# -- coding: utf-8 --

### fix ChangeTemplate

#imports
import os
import re

#define variables
CUSTOMIZATION = []
path = os.path.dirname(os.path.abspath(__file__)) #get current directory

#Define functions
#load template
def LoadTemplate(location, name):
	f = open('%s/%s' % (location,name),'r')
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

def WriteConfig(configwr, filename, location):
	#write config file
	config = open('%s/%s.cfg' % (location,filename) ,'w')
	config.write("%s" % configwr)
	config.close()

	return 1

#Main program
os.system('clear')	#Clear screen

print("Loading templates...")
TEMPLATESRX = LoadTemplate(path, "template-srx.cfg")
TEMPLATESW = LoadTemplate(path, "template-sw.cfg")

print("Loading customizations...")
CUSTOMIZATION = LoadCustomizations()

print("Creating srx config...")
CONFIGSRX = ChangeTemplate( TEMPLATESRX, CUSTOMIZATION )

print("Creating switch config...")
CONFIGSW = ChangeTemplate( TEMPLATESW, CUSTOMIZATION )

print("writing config-srx.cfg...\n")
WriteConfig(CONFIGSRX,"config-srx", path)

print("writing config-switch.cfg...\n")
WriteConfig(CONFIGSW,"config-switch", path)

#done
print("done, your configs are in %s" % path)