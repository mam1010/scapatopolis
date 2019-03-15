#username: dbirnie3
#password: RutgersMSE55$$
#1/1/2017 - 1/1/2018

import requests
import json

'''
Multi-line Comment Example
'''

'''
import httplib, urllib, base64

# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
parameters = {
  "id": 0,
  "feedId": "string",
  "name": "string",
  "displayName": "string",
  "description": "string",
  "category": "string",
  "firstAvailable": "string",
  "version": "string",
  "internalName": "string",
  "defaultSearchJson": "string",
  "fileLoadingMethod": "string",
  "postingFrequency": "string",
  "postingDay": "string",
  "retentionTime": "string",
  "lastDataLoad": "string",
  "lastDataLoadEst": "string",
  "isFrequentlyAccessed": true,
  "publishDate": "string",
  "created": "string",
  "updated": "string",
  "repostNotifications": [
    {
      "id": 0,
      "feedMetadataId": 0,
      "publishDate": "string",
      "content": "string",
      "created": "string",
      "updated": "string"
    }
  ],
  "columns": [
    {
      "id": 0,
      "feedMetadataId": 0,
      "dataType": "String",
      "filterType": "Input",
      "displayName": "string",
      "fieldName": "string",
      "enableFiltering": true,
      "enableSorting": true,
      "ordinalPosition": 0,
      "isVisible": true,
      "width": 0,
      "description": "string",
      "displayFormat": "string",
      "filterUiLocation": "Inline",
      "created": "string",
      "updated": "string",
      "isActive": true
    }
  ],
  "links": [
    {
      "rel": "string",
      "href": "string"
    }
  ],
  "timeDurationUnit": 0,
  "timeDurationIncrement": 0
}

# Make a get request with the parameters.
response = requests.get("https://api.pjm.com/api/v1/act_sch_interchange/metadata", params=parameters)

# Print the content of the response (the data the server returned)
print(response.content)

# This gets the same data as the command above
response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
print(response.content)
'''
'''
import httplib, urllib, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '{subscription key}',
}

params = urllib.urlencode({
})

try:
    conn = httplib.HTTPSConnection('api.pjm.com')
    conn.request("GET", "/api/v1/act_sch_interchange/metadata?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

'''
#Search Call
import httplib, urllib, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '7c81feeeded7405189fbb64057eee17f',
}

params = urllib.urlencode({
    # Request parameters
    'download': True,
    'rowCount': '{integer}',
    'sort': '{string}',
    'order': '{string}',
    'startRow': '{integer}',
    'isActiveMetadata': '{boolean}',
    'fields': '{string}',
    'effective_date_ept': '{string}',
    'terminate_date_ept': '{string}',
    'agg_pnode_id': '{number}',
    'agg_pnode_name': '{string}',
    'bus_pnode_id': '{number}',
    'bus_pnode_name': '{string}',
})

try:
    conn = httplib.HTTPSConnection('api.pjm.com')
    conn.request("GET", "/api/v1/agg_definitions?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
