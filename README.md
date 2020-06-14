# Fastnetmon API Client

Making bulk changes with FastNetMon is not "hard" but requires some work.

This client allows some basic changes to objects using a more programmatic
Python way, with less need to pay attention to exactly what's going on under
the hood with FNM. Initially it was written to allow modifications to the
Hostgroup object and show you some networks. 

You can enable the FNM API using the guide available at https://fastnetmon.com/docs-fnm-advanced/advanced-api/

> **_NOTE:_** This API implementation is definitely not feature complete. If you
want to do more than read and modify hostgroups.

## Using the example fixup.py code
You should set some environment variables to allow this to work. For simplicity
sake, we'll try and load these from a .env file using python-dotenv.

Expected environment variables:

```
API_USERNAME=<api username>
API_PASSWORD=<super secret password>
FNM_URL=<url>
```

## General usage
```
import pprint
from fastnetmonapi.client import FastNetMonAPI
url = "http://localhost:10007"
auth = ("username", "password")
client = FastNetMonAPI(url, auth)
pprint.pprint(client.hostgroups)
pprint.pprint(client.networks)
```