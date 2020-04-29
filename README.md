# unifiClientBlocker

This is a simple project that uses the Unifi python api to block and unblock clients.

Input is json configuration file and a command line argument.
Update the configuration file with the Unifi Controller IP address, password and mac addresses of the devices.

Example
```
{
  "controller":"192.168.1.7"
 ,"user":"admin"
 ,"password":"password"
 ,"clients":  [
   { "device" : "Iphone"   , "mac" : "00:00:00:00:00:00"}
  ,{ "device" : "XBoxOne"  , "mac" : "00:00:00:00:00:00"}
  ,{ "device" : "kidsPC"   , "mac" : "00:00:00:00:00:00"}     
 ]
}
```


```bash
python3 block_unblocker.py block
Blocking : Iphone : 00:00:00:00:00:00
Blocking : XBoxOne : 00:00:00:00:00:00
Blocking : kidsPC : 00:00:00:00:00:00
```

```bash
python3 block_unblocker.py unblock
Unblocking : Iphone : 00:00:00:00:00:00
Unblocking : XBoxOne : 00:00:00:00:00:00
Unblocking : kidsPC : 00:00:00:00:00:00
```
