#Final Project Script using the nmap library to quickly scan the entire network then return the open ports for the available IPs
#This script saves time by only enumerating ports on known 'up' endpoints
#Author: David Armstrong
#Revised: 12/15/2020

###Libraries###
import nmap

###Variables###
#Inintializng the nmap port scanner
scanner = nmap.PortScanner()
#The network to be scanned
network = input("Please enter a network address: ")
#List for compiling running endpoints
addresses = []

###Functions###
def network_info(network):
    #Find all end points which respond to ping
    print("Gathering 'Up' endpoints...")
    #Create dictionary of all nmap output
    a = scanner.scan(hosts=network, arguments='-sn')
    #Cut the dictionary down to just the scan info
    b = a['scan']
    #Append all ipv4 addresses to the addresses list
    for x in b.values():
        addresses.append(x['addresses']['ipv4'])
    print("The following devices are up:")
    for address in addresses:
        print(address)
    print("Enumerating endpoints...")
    #Scan for open ports
    for address in addresses:
        try:
            scanner.scan(address)
            print(address)
            print(scanner[address].all_protocols())
            print("Open Ports: ", scanner[address]['tcp'].keys())
        except:
            pass

###Main###
network_info(network)
###End###
