# -- coding: utf-8 --

#imports
import os
import re
import sys


#define global variables
templates = []
customizations = []
configs = []
loadedTemplate = []
loadedCustomizations = []
path = os.path.dirname(os.path.abspath(__file__)) #get current directory


#Define functions
#load template
def LoadTemplate(location, name):
	f = open('%s/%s' % (location,name),'r')
	template = f.read()
	f.close()
	return template

#load customizations
def LoadCustomization(location, name):
	loadedCustomizations_array = []
	file=""
	f = open('%s/%s' % (location,name),'r')
	loadedCustomizations_array = f.read().split('\n')
	f.close()
	return loadedCustomizations_array

#change template
def ChangeTemplate(template, array):
	i=0
	reg_before = "(=.*$|\[\')"
	reg_after = "(^.*=|\'\])"
	for item in array:
		template = template.replace(re.sub( reg_before,'', item), re.sub( reg_after,'', item))
		i +=1

	return template

def WriteConfig(config, filename, location):
	#write config file
	f = open('%s/%s' % (location,filename) ,'w')
	f.write("%s" % config)
	f.close()
	return 1

def CheckOs():
	if os.name == "nt":
		return "windows"
	else:
		return "linux"

####################################################################
#Main program                                                      #
####################################################################

if CheckOs() == "windows":
	os.system('cls') #Clear screen
else:
	os.system('clear')	#Clear screen

#process arguments###############################################################################################
t=0
c=0
for line in sys.argv:
	if re.match('^--template=.*$', line):
		templates.append(re.sub('^--template=','',line))
		t +=1	
	if re.match('^--change=.*$', line):
		customizations.append(re.sub('^--change=','',line))
		c +=1
	if re.match('^--help', line):
		print("%s\n\t%s\n\t%s\n\t%s\n\n%s" %(
					"usage: generate-config.py [options]",
					"--template=[templatefile] \t tempaltes to use, should be located in the script directory.",
					"--change=[cusomization] \t changefile to use, file containing placeholders.",
					"--help \t Display this help",
					"the customization file needs to be in the following format: placeholder=final text . One replacement per line and it is precies (spaces are characters to)\n template files and customization files are combined in order, so for correct combining use: --template= --change= --template= --change="
					))
		exit()
	
if t == 0 :
	print("No template found, using default 'template.cfg' instead")
	templates.append("template.cfg")
elif c == 0 :
	print("No customization found, using default 'customization.cfg' instead")
	customizations.append("customization.cfg")

for line in templates:
	print("using template: %s" % line)
	
for line in customizations:
	print("using customization: %s" % line)
	
#Loading the templates#############################################################################################

print("Loading templates...")

for item in templates:
	loadedTemplate.append(LoadTemplate(path, item))
	print("loaded template: %s" % item)

#Loading the customizaiotns#########################################################################################
	
print("Loading customizations...")

for item in customizations:
	loadedCustomizations.append(LoadCustomization(path, item))
	print("loaded customization: %s" % item)

#Creating configs###################################################################################################
	
print("Creating configs...")
i=0
for item in templates:
	if i > len(loadedTemplate):
		print("no more tempaltes")
		break
	elif i > len(loadedCustomizations):
		print("no more customizations")
		break
	else:
		configs.append(ChangeTemplate( loadedTemplate[i], loadedCustomizations[i] ))
		print("created config for %s with customization-file %s" % (templates[i],customizations[i]))
	
	i +=1

#Writing configs#####################################################################################################
	
print("writing configs to file...")
i=0
for item in configs: 
	WriteConfig(item,"%s-config.cfg" % re.sub('.cfg','',templates[i]), path)
	print("writen file %s-config.cfg" % re.sub('.cfg','',templates[i]))

#done
print("done, your configs are in %s" % path)

if CheckOs() == "windows":
	os.system('pause') #Clear screen
else:
	os.system('pause')	#Clear screen