import sys
import json
from pyunifi.controller import Controller

if len(sys.argv) <=1:
    print ("Missing action argument, block or unblock")

action = "unknown"
if sys.argv[1] == "block":
    action = "block"
if sys.argv[1] == "unblock":    
    action = "unblock"
if action == "unknown":
    print ("unknown action argument, " + sys.argv[1] + "; must be block or unblock") 
    
input_file = open ('config.json')
j = json.load(input_file)

controllerAddress=j["controller"]
controllerUser=j["user"]
controllerPassword=j["password"]

#print (j)

ctrl = Controller(controllerAddress, controllerUser, controllerPassword, 8443, version='v4', site_id="default",  ssl_verify=False)

for client in j["clients"]:
    mac = client['mac']
    device= client['device']
    
    if action == "block":
        print ("Blocking : %s : %s" %(device, mac))
        ctrl.block_client(mac)

    if action == "unblock":        
        print ("Unblocking : %s : %s" %(device, mac))
        ctrl.unblock_client(mac)    
       
    
