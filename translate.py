encIP = raw_input("Input Encrypted IP : ")

l1 = 0x3a700e3 ^ long(encIP, 32)

i1 = (0xff000000 & l1) >> 24
i2 = (0xff0000 & l1) >> 16
i3 = (65280 & l1) >> 8
i4 = l1 & 255
originIP = str(i4) + "." + str(i3) + "." + str(i2) + "." + str(i1)

print "Original IP is " + originIP
