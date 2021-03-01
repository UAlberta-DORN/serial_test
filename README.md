# serial_test
 
## Sample Result
This is a sample of what will come out:
```yaml
{'header': {'DEVICE_TYPE': 0, 'POWER_SOURCE': 0, 'DEVICE_ID': '7C:9E:BD:F4:2A:BC', 'LOCAL_TIME': 81305}, 'peers': {'hub': ''}, 'data': {'temp': -273.15, 'light': -273.15}, 'command': 'Callback', 'children': {'7C:9E:BD:F4:06:68': {'header': {'DEVICE_TYPE': 1, 'DEVICE_ID': '7C:9E:BD:F4:06:68', 'POWER_SOURCE': '1'}, 'data': {'temp': -273.15, 'light': -273.15, 'timestamp': 81305}}}}
```

Beautified:
```yaml
{
   "header":{
      "DEVICE_TYPE":0,
      "POWER_SOURCE":0,
      "DEVICE_ID":"7C:9E:BD:F4:2A:BC",
      "LOCAL_TIME":81305
   },
   "peers":{
      "hub":""
   },
   "data":{
      "temp":-273.15,
      "light":-273.15
   },
   "command":"Callback",
   "children":{
      "7C:9E:BD:F4:06:68":{
         "header":{
            "DEVICE_TYPE":1,
            "DEVICE_ID":"7C:9E:BD:F4:06:68",
            "POWER_SOURCE":"1"
         },
         "data":{
            "temp":-273.15,
            "light":-273.15,
            "timestamp":81305
         }
      }
   }
}
```
