import requests
import os
from pprint import pprint
from fastnetmonapi.client import FastNetMonAPI

try:
	from dotenv import load_dotenv
	load_dotenv()
except:
	pass

def main():
	auth_data = (os.getenv('API_USERNAME'), os.getenv('API_PASSWORD'))
	url = os.getenv('FNM_URL')

	client = FastNetMonAPI(url, auth_data)
	hostgroups = client.hostgroups
	low_mbps_pps = int(client.bandwidth_to_pps(200)*1.4)
	for group in hostgroups:
		hostgroup = hostgroups[group]
		if hostgroup.threshold_mbps > 5000:
			print("We would change %s to have a lower threshold" % hostgroup.name)
			hostgroup.threshold_mbps = 5000
		if hostgroup.threshold_pps > 0 and hostgroup.threshold_pps < low_mbps_pps:
			old_pps = hostgroup.threshold_pps
			hostgroup.threshold_pps = low_mbps_pps
			print("We lifted %s to %s pps from %s pps" % (hostgroup.name, low_mbps_pps, old_pps))
		if hostgroup.threshold_mbps < 200:
			hostgroup.threshold_mbps = 200
			print("Lifted threshold to 200Mbps for %s" % hostgroup.name)
		if hostgroup.threshold_pps == 0:
			print("Hmm. Hostgroup %s does not have a pps threshold. Should it exist?" % hostgroup.name)
	client.commit()


if __name__ == '__main__':
	main()