ifconfig eth1 192.168.232.1
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
dnsmasq
python3 app.py
