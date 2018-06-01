#! usr/bin/python3

import requests
url_file = 'https://gayway.zhonganonline.com/download/?host=10.139.97.231&path=/home/zhaoyiwei/za-telecom-business/20180507.tar.gz&user=zhaoyiwei&id_rsa=false'
mycookie = {"session":".eJxNkD1uwzAMhe_C2Sj0T8lT1y49gRbGohsDtR3EEdI6yN1DBW3RhQAfH79H8AZ14zP0Nxjqdnkr0BuVtLKug8InOl9mXp6yiFH_F99pZughV2815uqYhlyTLjrXiLHkGkxUUtGMuSIPDjrgmaZPWdqPtH5PV55e9-O6fNDyMqyzzCcJ0ioo7TtYfvmxoJdqkIRjicW3rDK57krZpIz0J6E0s5ZbtEvJqpa28dcTgN5iaxsdgh9DcI5ToOQw8sGR9Sb56HBMhawY20d-0v8Ohfv9ASpEWKs.DeaRSA.NCwTUPyzSn-Ci9sxHk2zA8FmfzU"}
r = requests.get(url_file,cookies = mycookie) 
with open("20180507.tar.gz", "wb") as code:
     code.write(r.content)
	 