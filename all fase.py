import subprocess

def change_dns(server):
    subprocess.run(['sudo', 'bash', '-c', 'echo "nameserver {0}" > /etc/resolv.conf'.format(server)])

#example change dns to 8.8.8.8
change_dns('8.8.8.8')

#change hostname 
import subprocess
def change_hostname(hostname):
    subprocess.run(['sudo', 'hostnamectl', 'set-hostname', hostname])

#change hostname to example 
change_hostname('example')


#determine the static ip interface
import subprocess

def set_static_ip(interface, ip, netmask):
    subprocess.run(['sudo', 'ifconfig', interface, ip, 'netmask', netmask])

# تعیین IP ثابت برای اینترفیس eth0 با IP 192.168.1.10 و Netmask 255.255.255.0
set_static_ip('eth0', '192.168.1.10', '255.255.255.0')



#use dhcp to determine the ip of an interface
import subprocess

def set_dhcp(interface):
    subprocess.run(['sudo', 'dhclient', interface])

# استفاده از DHCP برای اینترفیس eth0
set_dhcp('eth0')

#permanent add root
import subprocess

def add_permanent_route(destination, gateway):
    subprocess.run(['sudo', 'ip', 'route', 'add', destination, 'via', gateway])

# افزودن روت دائمی برای شبکه 192.168.2.0/24 با دروازه 192.168.1.1
add_permanent_route('192.168.2.0/24', '192.168.1.1')


#remove permanent root
import subprocess

def delete_permanent_route(destination):
    subprocess.run(['sudo', 'ip', 'route', 'del', destination])

#remove permanent root fo example 192.168.2.0/24
delete_permanent_route('192.168.2.0/24')


#remove temporary root
import subprocess

def delete_temp_routes():
    subprocess.run(['sudo', 'ip', 'route', 'flush', 'cache'])

#remove all temporaryroot
delete_temp_routes()


#clear firewall rules
import subprocess

def clear_firewall_rules():
    subprocess.run(['sudo', 'iptables', '-F'])

# پاک کردن قوانین فایروال
clear_firewall_rules()

#forwarding packets to a new destination address
import subprocess

def forward_packets(destination):
    subprocess.run(['sudo', 'iptables', '-t', 'nat', '-A', 'PREROUTING', '-p', 'udp', '--dport', '53', '-j', 'DNAT', '--to-destination', destination])

# انتقال بسته‌ها با مقصد 4.2.2.4:53 به 1.1.1.1:53
forward_packets('1.1.1.1:53')

#disconnecting the internet while maintaining access to the internal network
import subprocess

def disable_internet():
    subprocess.run(['sudo', 'iptables', '-A', 'OUTPUT', '-p', 'tcp', '--dport', '80', '-j', 'REJECT'])

# قطع اتصال اینترنت
disable_internet()

#close the communication of a specific user
import subprocess

def block_user(user):
    subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-p', 'tcp', '-m', 'owner', '--uid-owner', user, '-j', 'REJECT'])

# بستن ارتباطات یوزر با UID 1000
block_user('1000')

#create table
import subprocess

def create_table(table):
    subprocess.run(['sudo', 'nftables', '-t', table, '-N', table])

#create new table 
create_table('mytable')

#create chain
import subprocess

def create_chain(table, chain):
    subprocess.run(['sudo', 'nftables', '-t', table, '-N', chain])

# ایجاد چین با نام mychain در جدول mytable
create_chain('mytable', 'mychain')

#create access-restricting roles
import subprocess

def create_rule(table, chain, rule):
    subprocess.run(['sudo', 'iptables', '-t', table, '-A', chain] + rule)

# ایجاد قاعده جدید در جدول mytable و چین mychain با رول "-p tcp --dport 22 -j ACCEPT"
create_rule('mytable', 'mychain', ['-p', 'tcp', '--dport', '22', '-j', 'ACCEPT'])