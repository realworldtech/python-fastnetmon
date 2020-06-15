import requests
from urllib.parse import urljoin, quote_plus

class Hostgroup:
	_hostgroup = None
	_client = None
	_pathname = None

	def __init__(self, client, hostgroup):
		self._hostgroup = hostgroup
		self._client = client
		self._pathname = self._client.encode_name(hostgroup['name'])

	def __getattr__(self, item):
		return self._hostgroup[item]

	def __setattr__(self, item, value):
		if item[0] == "_":
			super().__setattr__(item, value)
		else:
			try:
				self._client.put(("hostgroup/%s" % self._pathname), item, value)
				self._hostgroup[item] = value
			except Exception as e:
				raise e

	def __repr__(self):
		return str(self._hostgroup)


class FastNetMonAPI:
	client = None
	auth = None
	url = None
	debug = False
	def __init__(self, url, auth_data):
		self.url = url
		self.auth_data = auth_data
		self.client = requests.Session()
		self.client.auth = self.auth_data
		self.debug = False

	def get(self, path):
		url = urljoin(self.url, path)
		result = self.client.get(url).json()
		if result['success']:
			return result['values']
		else:
			raise Exception("An error occured %s while retrieving %s" % (
				result['error_text'],
				url))

	def put(self, path, key=None, value=None):
		if key is not None:
			if value is True or value is False:
				value = "enable" if value else "disable"
			parts = "/".join([path, key, str(value)])
			url = urljoin(self.url, parts)
		else:
			url = urljoin(self.url, path)
		if self.debug:
			print(url)
		result = self.client.put(url).json()
		if result['success']:
			return result
		else:
			raise Exception("An error occured %s while retrieving %s" % (
				result['error_text'],
				url))

	def commit(self):
		self.put("commit")

	@property
	def networks(self):
		networks = client.get("main/networks_list")
		results = {}
		for network in networks:
			network_id = self.encode_name(network)
			results[network_id] = network
		return results

	def encode_name(self, network):
		return quote_plus(network)

	@property
	def hostgroups(self):
		groups = {}
		for hostgroup in self.get("hostgroup"):
			groups[hostgroup['name']] = (Hostgroup(self, hostgroup))
		return groups

	def bandwidth_to_pps(self, bandwidth_mbps=0, packet_size=1500):
		return int((bandwidth_mbps*1024*1024)/(packet_size+20))