# Fastnetmon API Client

Making bulk changes with FastNetMon is not "hard" but requires some work.

This client allows some basic changes to objects using a more programmatic
pyhton way. Initially it was written to allow modifications to the Hostgroup
object.

You should set some environment variables to allow this to work. For simplicity
sake, we'll try and load these from a .env file using python-dotenv.

Expected environment variables:

```
API_USERNAME=<api username>
API_PASSWORD=<super secret password>
FNM_URL=<url>
```

