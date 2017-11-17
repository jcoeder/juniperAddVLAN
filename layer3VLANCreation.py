import pprint
import getpass
import jnpr.junos
from jnpr.junos.utils.config import *
from jnpr.junos.exception import *

from lxml import *

#Ask the user for the device they wish to connect to and username and password to access that device.
#ipAddressInput = input("Device IP Address: ")
#usernameInput = input("Username: ")
#passwordInput = getpass.getpass(prompt="Password: ")

#Supplied username and password for testing
ipAddressInput = '172.17.3.202'
usernameInput = 'admin'
passwordInput = 'admin123'

#Define the device using user input
device = jnpr.junos.Device(host=ipAddressInput, user=usernameInput, password=passwordInput)

#Set device open connection to timeout after 3 seconds
jnpr.junos.Device.auto_probe = 3

#Ask the user for the device needed VLAN information
#vlanId = input('VLAN Tag ID: ')
#vlanDescription = input('VLAN Description: ')

#Supplied VLAN information for testing
vlanID='2453'
vlanDescription='This is a testing VLAN'

#Different Juniper switches have different inteface naming
#switchType = ''
#if switchType == ex:
#	interfaceName = 'vlan'
#else:
#	interfaceName = 'irb'



#            <vlans>
#                <vlan>
#                    <name>VLAN3110</name>
#                    <description>DRAC-ILO</description>
#                    <vlan-id>3110</vlan-id>
#                    <l3-interface>vlan.3110</l3-interface>
xmlConfig = """
	<configuration>
		<vlan>
			<name>{0}</name>
			<description>{1}</description>
			<vlan-id>{2}</vlan-id>
		</vlan>
	</configuration>
""".format('VLAN'+vlanID, vlanDescription, vlanID,)
print (xmlConfig)

#Open connection to device and start a NETCONF session, else error

# try:
#     device.open()
# except ConnectError:
#     print ('Cannot connect to device. \nConnection Error. \n{0}'.format(ConnectError))
#
# #Get the softwre version from the device
# #deivceSoftwareVersion = device.rpc.get_software_information(normalize=True)
#
# #Print facts and software version for testing
# #pprint (device.facts)
# #pprint (etree.tostring(deivceSoftwareVersion))
#
# #Bind the config instance to the device instance
# device.bind(cu=Config)
#
# #Atttempt to lock the configuration to prevent others from making changes at the same time
# print ('Locking the configuration.')
# try:
# 	device.bind().lock()
# 	print ('Configuration successfully locked.')
# except LockError:
# 	print ('Unable to lock configuration: \n{0}'.format(LockError))
# 	device.close()
#
# #Attempt to apply configuraiton changes
# print ('Loading configuration changes.')
# #try:
# #	device.cu.load(path=conf_file, merge=True)
# #except (ConfigLoadError, Exception):
# #	print ('Unable to load configuration changes: \n{0}'.format(ConfigLoadError))
# #	print ('Unlocking the configuration.')
# #	try:
# #		device.cu.unlock()
# #		print ('Configuration successfully unlocked.')
# #	except UnlockError:
# #		print ('Unable to unlock configuration: \n{0}'.format(UnlockError))
# #	device.close()
#
# #Attempt to commit the configuration
# print ('Commiting the configuration')
# try:
# 	device.cu.commit(comment='Configuration changed by script.')
# 	print ('Configuration successfully commited.')
# except CommitError:
# 	print ('Unable to commit configuration: \n{0}'.format(CommitError))
# 	print ('Unlocking the configuration.')
# 	try:
# 		device.cu.unlock()
# 		print ('Configuration successfully unlocked.')
# 	except UnlockError:
# 		print ('Unable to unlock configuration: \n{0}'.format(UnlockError))
# 		device.close()
#
# #Unlock the configuration after successful commit
# print ('Unlocking the configuration.')
# try:
# 	jnpr.junos.Device.cu.unlock()
# 	print ('Configuration successfully unlocked.')
# except UnlockError:
# 	print ('Unable to unlock configuration: \n{0}'.format(UnlockError))
#
# #Close connection to device
# device.close()

