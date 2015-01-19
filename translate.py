encIP = raw_input("Input Encrypted IP : ")

"""
.line 617
.local v14, "l":J
const-wide/32 v24, 0x3a700e3

xor-long v14, v14, v24
"""
l = 0x3a700e3 ^ long(encIP, 32)

"""
.line 618
const-wide/32 v24, -0x1000000

and-long v24, v24, v14

const/16 v23, 0x18

ushr-long v6, v24, v23
"""
i0 = (-0x1000000 & l) >> 0x18

"""
.line 619
.local v6, "i1":J
const-wide/32 v24, 0xff0000

and-long v24, v24, v14

const/16 v23, 0x10

ushr-long v8, v24, v23
"""
i1 = (0xff0000 & l) >> 0x10

"""
.line 620
.local v8, "i2":J
const-wide/32 v24, 0xff00

and-long v24, v24, v14

const/16 v23, 0x8

ushr-long v10, v24, v23
"""
i2 = (0xff00 & l) >> 0x8

"""
.line 621
.local v10, "i3":J
const-wide/16 v24, 0xff

and-long v12, v14, v24
"""
i3 = l & 0xff

"""
.line 623
.local v12, "i4":J
new-instance v23, Ljava/lang/StringBuilder;

invoke-direct/range {v23 .. v23}, Ljava/lang/StringBuilder;-><init>()V

const-string v24, ""

invoke-virtual/range {v23 .. v24}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

move-result-object v23

move-object/from16 v0, v23

invoke-virtual {v0, v12, v13}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

move-result-object v23

const-string v24, "."

invoke-virtual/range {v23 .. v24}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

move-result-object v23

move-object/from16 v0, v23

invoke-virtual {v0, v10, v11}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

move-result-object v23

const-string v24, "."

invoke-virtual/range {v23 .. v24}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

move-result-object v23

move-object/from16 v0, v23

invoke-virtual {v0, v8, v9}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

move-result-object v23

const-string v24, "."

invoke-virtual/range {v23 .. v24}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;

move-result-object v23

move-object/from16 v0, v23

invoke-virtual {v0, v6, v7}, Ljava/lang/StringBuilder;->append(J)Ljava/lang/StringBuilder;

move-result-object v23

invoke-virtual/range {v23 .. v23}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;
:try_end_152
.catch Ljava/lang/Exception; {:try_start_cc .. :try_end_152} :catch_155

move-result-object v4

goto/16 :goto_a1
"""
originIP = str(i3) + "." + str(i2) + "." + str(i1) + "." + str(i0)

print "Original IP is " + originIP
