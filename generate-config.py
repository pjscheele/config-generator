# -- coding: utf-8 --

#get current directory
import os
path = os.path.dirname(os.path.abspath(__file__))

#load customizations
hostname = "RTEM00000FW001"


#open template
template = open('%s/template.cfg' % path,'r')
workingtemplate = template.read()
template.close()

#customize template
workingtemplate = workingtemplate.replace("!!IP!!", '127.0.0.1')
workingtemplate = workingtemplate.replace('! !IP! !', '!!IP!!')

#write config file
config = open('%s/%s.cfg' % (path, hostname) ,'w')
config.write("%s" % workingtemplate)
config.close()

#done
print "done, your config %s.cfg is in %s" % (hostname, path)