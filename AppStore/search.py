import requests

msrdp_id_ios = "714464092" # RDP for iPhone
msrdp_id_mac = "715768417" # RDP for Mac
ctx_receiver_id = "363501921" # Citrix receiver for iOS
vmview_horizon_id = "417993697"

def search_by_id (id):
    _url = "https://itunes.apple.com/"
    _session = requests.Session()
    _by_id = "lookup?id=%s"
    url = _url + _by_id % id
    resp = _session.get(url, verify=False)
    return resp.json()

_json = search_by_id(msrdp_id_ios)
print _json['results'][0]['releaseDate'], "\t", _json['results'][0]['version'], "\t", _json['results'][0]['trackName']
_json = search_by_id(msrdp_id_mac)
print _json['results'][0]['releaseDate'], "\t", _json['results'][0]['version'], "\t", _json['results'][0]['trackName']
_json = search_by_id(ctx_receiver_id)
print _json['results'][0]['releaseDate'], "\t", _json['results'][0]['version'], "\t", _json['results'][0]['trackName']
_json = search_by_id(vmview_horizon_id)
print _json['results'][0]['releaseDate'], "\t", _json['results'][0]['version'], "\t", _json['results'][0]['trackName']
