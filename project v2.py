import sys
#print(sys.argv[1])

def convertAddress(address, subnetMask):
    #octets = address.split(".")
    octets = [int(o) for o in address.split(".")]
    subnetOctets = [int(o) for o in subnetMask.split(".")]
    print(octets)
    
    binaryAddress = ""
    for octet in octets:
        binaryAddress += f'{octet:08b}' + "." 

    subnetMaskBinary = ""
    for octet in subnetOctets:
        subnetMaskBinary += f'{octet:08b}' + "."
    subnetMaskBinary = subnetMaskBinary[:-1]
    
    binaryAddress = binaryAddress[:-1]
    print(binaryAddress)

    networkClass = ""
    defaultMask = ""
    numberOfSubnets = 0
    numberOfHosts = 0

    if  octets[0] > 0 and octets[0] <= 127:
        print("Class A Default Subnet Mask: 255.0.0.0")
        networkClass = "A"
        defaultMask = "255.0.0.0"
        for octet in subnetOctets[1:]:
            binaryOctet = f'{octet:08b}'
            numberOfSubnets = 2 ** binaryOctet.count('1')
            numberOfHosts = (2 ** binaryOctet.count('0')) - 2
        
    elif octets[0] >= 128 and octets[0] <= 191:
        print("Class B Default Subnet Mask: 255.255.0.0")
        networkClass = "B"
        defaultMask = "255.255.0.0"
        for octet in subnetOctets[2:]:
            binaryOctet = f'{octet:08b}'
            numberOfSubnets = 2 ** binaryOctet.count('1')
            numberOfHosts = (2 ** binaryOctet.count('0')) - 2
            
    elif octets[0] >= 192 and octets[0] <= 223:
        print("Class C Default Subnet Mask: 255.255.255.0")
        networkClass = "C"
        defaultMask = "255.255.255.0"
        for octet in subnetOctets[3:]:
            binaryOctet = f'{octet:08b}'
            numberOfSubnets = 2 ** binaryOctet.count('1')
            numberOfHosts = (2 ** binaryOctet.count('0')) - 2
            
    elif octets[0] >= 224 and octets[0] <= 239:
        print("Class D")
        networkClass = "D"
    else:
        print("Class E")
        networkClass = "E"
        
    print(numberOfSubnets, numberOfHosts)

    defaultMaskOctets = [int(o) for o in defaultMask.split(".")]
    defaultMaskBinary = ""
    for octet in defaultMaskOctets:
        defaultMaskBinary += f'{octet:08b}' + "."
    defaultMaskBinary = defaultMaskBinary[:-1]

    return (networkClass, defaultMask, defaultMaskBinary, subnetMaskBinary, numberOfSubnets, numberOfHosts)

convertAddress(sys.argv[1])

   



