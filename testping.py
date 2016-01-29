from python-ping import ping
p = ping.Ping('google.com', timeout=3000, quiet=False, silent=False, ipv6=False)
stats = p.run(1) 