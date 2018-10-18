# PoloG40Digifant
Binary Decompilation of the Polo G40 Digifant-1 Controller


- G40 Chip Info 
- G40 Tuning Info
- Digifant Modders
- Technical Documentation
- Troubleshooting
  - Fuel pump primes but no spark when cranking - fried TC1 Transistor
  - Digifant Error Codes
  - VCDS Reading Groups
- Data Logging
  - K-line
  - KDA's Logging tools
- G40 ECU Binary Decompiling
  - Map Locations
  - Ignition
  - RPM Limiter
  - RPM Scalar map
  - Load
  - Boost reduction by ISV
  - G60 Triple Timing Maps Mods -Digilag, OpenLoop Lambda, ISV Disable
  - SNS G60 Digilag removal analysis
  - SNS G40 Digilag custom code


G40 ECU Info 
 - G40 Stock ecu's uses 27C256 Eprom 28 pin DIP. 
 - It can only be erased by shining UV light on its glass window (that should be covered by a sticker) on top of the chip. 
 - The eprom connects to two other chips that are motorolas the're model numbers are: MC68HC11A1 and MC68HC25
 - Original Bin File 
    - http://www.chip-tuner.hu/original_ecu_files/files/VW/VW%20Polo%20G40%20022c-0261.200.330-ori.rar
 - I use a TL866II programmer via usb connection to a laptop to read the eproms available cheaply from online retailers


G40 Tuning Info

- A nice document describing how to use TunerPro for mapping.
  - https://datenpdf.com/download/custom-mapping-digifant-1-throttle-fuel-injection_pdf
- To use TunerPro effectively, you need to create a definition file. There is one available here for free the Polo G40 (but you will need to be signed into the forum to download)
  - http://www.ecuconnections.com/forum/viewtopic.php?f=25&t=83
 - Live Eprom Emulation via Moates Ostrich v2.0
   - available via h-tune in the uk for £199 
   - https://h-tune.co.uk/moates-ostrich-2-0-emulator-honda-obd1-ecu-p28-p30-civic-integra/
   - This will plug directly into the 28 pin chip socket on the g40 ecu and allow to you connect to your laptop via USB and emulates the G40 eprom, allowing you to tune on the fly. 
   - When you open a particular table ie fuelling or ignition, which are mapped via load sites ( rpm vs map value ), you can set address tracing and see which lookup value the ecu is referencing at any point.. Once you are happy with a map, you save the bin file and write it to a chip and voila one home mapped G40.


Twin Maps / Map Switching

- Twin maps can be written to a 27SF512 chip, and referenced on the fly using a Moates TwoTimer
   - https://h-tune.co.uk/moates-2timer/
   - TwoTimer: 27SF512 (00000/0FFFF), 2x256kbit/32kbyte slots, idles in “high position”
   - 8000/FFFF (initial position)
   - 0000/7FFF (when switch is grounded)



Digifant Modders
 - KDA, a Russian guy who has written his own protocol and software which loads of different features but as it’s in Russian, it’s nails to understand - see KDA logging section for more info.
 - Dominik Gummel from digifant -onlineabstuning. This also includes an Android app as well as pc/Linux flavours. This is tasty as it shows map values, knock flag etc.
   - Link - http://gummel.net/bofh-ng/en/digifant-1-en/digifant-1-read-live-data-over-serial-k-line
   - Open source logger supporting k-line with Dominik's modified ecu code  https://github.com/designer2k2/multidisplay
 - DigifantTool by Rafal M. He has built a Bluetooth emulator and also has modified code to output ecu values to tunerpro via an ADX file and a modified bin
   - Link - https://m.facebook.com/tuningtool/


Technical Documentation

- Near full list of Volkswagen Self Study Programs - http://www.volkspage.net/technik/ssp/index1_eng.php 
- G40 supercharger - http://www.volkspage.net/technik/ssp/ssp/SSP_79.PDF
- G60 supercharger - http://www.volkspage.net/technik/ssp/ssp/SSP_103.PDF
- Digifant  - http://www.volkspage.net/technik/ssp/ssp/SSP_87.PDF
- Lambda probe and map sensor with digifant control and function - http://www.volkspage.net/technik/ssp/ssp/SSP_110.PDF


Troubleshooting

- Common G40 ECU Fault - No start
   - https://www.clubpolo.co.uk/topic/110223-g40-ecu-problem/?tab=comments#comment-1053151
```
The ECU primes the fuel pump when it is first powered up so that means the processor and 'chip' are working OK. (It also means that both relays associated with the ECU are OK). 
There are various drive transistors and interface chips for the sensors inside the ECU. The only things that should stop the ignition firing are a problem with the connection/interface from the hall sensor or the drive to the coil/amp. I think it would still run if any of the other sensors have problems as the ECU can detect that. The hall sensor triggers the ECU to fire the injectors and fire the ignition. To check the hall sensor is OK see if the injectors are opening when you crank the engine over - easiest to see if there is fuel in the cylinders after you've cranked it over for a while. If that works it's hopefully just the drive transistor for the coil/amp unit.

The transistor to change is marked TC1 on the circuit board (it's a D shaped black thing with 3 wires). The transistor type is BC337.
```

 - Digifant Error Codes
```


0523   Intake air temp sensor
0521   CO Fuel Trim Pot
0522   Engine coolant Temp sender
0519   Manfold absolute pressure sensor
0537   Oxygen sensor regulation
0525   Oxygen sensor
0524   Knock sensor

```

 - VCDS Reading Groups
```


display group 01
1 coolant temp (blue temp sensor)
2 engine speed (RPM, from the hall sensor)
3 lambda signal
4 injection period

02

1 coolant temp (blue temp sensor)
2 engine speed (RPM, from the hall sensor)
3 not for service dept (seems to be ignition advance, units in BTDC anyway)
4 engine load (map sensor)

03

coolant temp (blue temp sensor)
engine speed (RPM, from the hall sensor)
not for service dept (this appears to be inlet temp)
c0 pot voltage

04 the same as 03
coolant temp
not for service dept (seems to be inlet temp)
not for service dept (seems to be a temperature but not sure what)
not for service dept (seems to be battery voltage)

```

Data Logging
 - K-Line / TTL translation ICs ( ST L9636 http://www.st.com/internet/automotive/product/75181.jsp ) and SOIC / DIP adapter sockets at RS Components. 
   - https://www.st.com/en/automotive-analog-and-power/l9637.html
 - KDA's Logging tools
   - https://github.com/AYastrebov/VW_G60
   - http://nefariousmotorsports.com/forum/index.php?topic=11719.0title=
   - file list
     - VW6636_eng.rar=fully decompiled IDA pro IDB file with its matching 3 timing BIN file.
     - VW6636+usb.rar=modified 3 timing map file that will allow input of innovative LC-1 and live USB data logging
     - the TOOLS.rar=software created by a russian guy known as KDA for live data logging the ECU and tuning BIN files. (software is in russian though so best of luck with using it.)
     - images.rar=pictures of how to modify the ECU hardware for live data logging and add the ability to use LC-1 for lambda input.(picture comments are originally in russian and converted them to english with google translate)
     - TunerPro RT v5 - G60 3 Ignition Map (Marc G60T 2014).xdf=3 timing map XDF from a user on ecuconnections forum


G40/G60 ECU Binary Decompiling


It uses a Motorola MC68HC11A1 cpu which according to Motorola specs this cpu has disabled built in ROM, so I suspect that 100% of program resides on EPROM along with all maps.
Use IDAPro to disassemble, format and comment the code. 
You can then create an asm file, and use MiniIDE to re-assemble the code into a binary. This will allow you add or modify the code to suit.


You have to tell IDApro where the code sections are (interrupt vectors in 68HC11 architecture): the starting addresses are located at the end of the binary. For example, the reset irq vector address is @7FFE: 54AA. 



With the D key, you can switch between 8 and 16 bit data. 

```


RESERVED:7FFE                 fcb $54
RESERVED:7FFF                 fcb $AA ; ¬

```

Change address 7FFE to 16bit value and press Enter.

```


RESERVED:7FFE                 fdb $54AA

```

IDA should now jump to address 54AA. 

Press C to tell IDA that this is code and it will be exposed.

```


RESERVED:54AA ; ---------------------------------------------------------------------------
RESERVED:54AA                 lds     #$1FF
RESERVED:54AD                 ldaa    #$B
RESERVED:54AF                 staa    INIT            ; RAM and I_O Mapping Register
RESERVED:54B2                 ldaa    #8
RESERVED:54B4                 staa    byte_B000
RESERVED:54B7                 ldaa    #$C1 ; '-'
RESERVED:54B9                 staa    byte_B024
RESERVED:54BC                 ldaa    #$90 ; 'É'
RESERVED:54BE                 staa    byte_B039
RESERVED:54C1                 ldaa    #$10
RESERVED:54C3                 staa    byte_B035
RESERVED:54C6                 ldy     #$B000
RESERVED:54CA                 ldaa    #0
RESERVED:54CC                 staa    byte_207
RESERVED:54CF                 ldab    #$F8 ; '°'
RESERVED:54D1                 stab    byte_203
RESERVED:54D4                 ldaa    #$A
RESERVED:54D6                 staa    byte_B008
RESERVED:54D9                 ldaa    #$A
RESERVED:54DB                 staa    byte_B009
RESERVED:54DE                 ldaa    byte_57
RESERVED:54E0                 cmpa    #$16
RESERVED:54E2                 beq     loc_54F5
RESERVED:54E4                 ldx     #$6A4

```

Repeat this for all IRQ vectors. IRQ vectors are located starting from address 7FD6 (in standard 1 ignition file) and are written on 16bit values

```


RESERVED:7FD6                 fdb $4C85
RESERVED:7FD8                 fdb $76DB
RESERVED:7FDA                 fdb $76DB
RESERVED:7FDC                 fdb $76DB
RESERVED:7FDE                 fdb $637E
RESERVED:7FE0                 fdb $76DB
RESERVED:7FE2                 fdb $5CD4
RESERVED:7FE4                 fdb $63A1
RESERVED:7FE6                 fdb $5E52
RESERVED:7FE8                 fdb $76DB
RESERVED:7FEA                 fdb $57C0
RESERVED:7FEC                 fdb $622A
RESERVED:7FEE                 fdb $7E17
RESERVED:7FF0                 fdb $61A1
RESERVED:7FF2                 fdb $76DB
RESERVED:7FF4                 fdb $76DB
RESERVED:7FF6                 fdb $76DB
RESERVED:7FF8                 fdb $76DB
RESERVED:7FFA                 fdb $76DB
RESERVED:7FFC                 fdb $76DB
RESERVED:7FFE                 fdb $54AA

```



Map Locations

```

Ignition x4004->x4103 (16x16)
Fuel x4104->x4203 256 x 8 (16x16)
RPM Scalar x420C->x422B 16 x 1 (16 bit words, hi byte first) rpm =  15000000 / value
Coil Dwell Time x422C->x423B
Knock Multiplier x424C->x425B
Knock Retard Rate x425C->x426B
Knock Decay Rate x426C->x427B
Minimum MAP for Knock Retard x427C->x428B
Advance vs Coolant Temp x428C->x429B
Idle Advance Time x429D->x42AC (wrong)
Idle Ignition Low Limit  x429F->x42AE (wrong)
Idle Ignition High Limit x42A5->x42B4 (wrong)
Choke x42CD->x42DC (wrong)
ECT Temperature Compensation 1 x42DD->x42EC
IAT Temperature Compensation x42EE->x42FD
ECT Temperature Compensation 2 x42FF->x430E
Startup Enrichment x4310->x431F
Startup Enrichment vs ECT x4332->x4341
Battery Compensation x4343->x4352
Antilog table? x4344->x4353
Accel Enrichment Minimum Delta Map x4365->x4374
Accel Enrichment vs ECT x4375->x4384
Accel Enrichment Adder vs ECT x4386->x4395
Lambda Upswing x43DA->x4319
Lambda Downswing x441A->x4459
Startup ISV vs ECT x4434->x4443
Coolant Temperature vs Idle x443B->x445A
Lambda Decay x445A->x4469
Boost Cut (No Knock) x44D9->x44E8
Boost Cut (Knock) x44EE->x44FD
ISV Boost Control x44FF->x450E 
WOT Initial Enrichment x450B->x451B
Idle Ignition x4520->x452F
CO Adjustment vs MAP x4562->x4571
Rev Limit x5BC2->x5BC3

```

Ignition

A PG engine has 6.0 deg btdc at idle, VW sources state greatest advance angle is 32 degrees.

```

This gives us the following hex values
C1h at idle which means 6 deg btdc
77h at maximum which is 32deg btdc
giving us 74 hex values for 26 degrees
so one value in map means around 2.86 degrees.
one zero point is C1h - 6*2.86 approximately D2h or 210 in decimal
So approximate formula is : Advance in degrees btdc = (210 - value in map)/2.86

```

RPM Limiter
```
This is a 16-bit word, hi byte first (first change byte than search 4bf2)
formula: rpm = 30000000 / value
```

RPM Scalar Map
```
0x420C

1x16 table, reverse order, 16bit words, hi-byte first.
formula: rpm = 15000000 / value


In older DF1 versions without detection by the knocking map there are only 2 limiters (one for testing procedure of the the G-Lader - in case of deconnected air-temp and water-temp sensors and one for the normal cycle). 
In newer Software versions there is at least one more limiter.
If the rev limit is raised, the rpm scalar map must be updated as this is referenced by several other tables to provide an rpm-axis.
```

Load
```
Load is taken as a percentage from the load sensor.
0..5V range of output from sensor is divided in 16 equal slices.
So you just divide 200kPa by 16 and get values in kPa.
If you change the map sensor i.e. to an 250kpa one, the ecu still reads boost values from 0 to 255. But now a boost value of 255 means 1,5 bar of boost instead 1 bar. :)
So you have to adjust all maps which are indexed by boost.
The most important ones are the WOT and main fuel maps.
```

Boost reduction by ISV
```
The ISV allows the ability to bleed off boost, at lower RPM.
In triple map file 636 it lives at x481C. It is RPM vs MAP signal and controls the allowed boost with knock (There is also a map for boost cut with knock at x482D). There is also additional ISV boost control stored at x483E, I still need to work out what this is for.
Apparantly in 3 map versions of the software, boost is reduced as at high-rpms along with fuel reduction to help the G-lader from destruction as the air oscillates.
```

G60 Triple Timing Maps Mods - Digilag, OpenLoop Lambda, ISV Disable


disable digilag g60 triple timing map :-

```
x4433 change 01 00 to 00 00
x4435 change 03 00 to 00 00
```

Code excerpt - these two operations will be turned in nop (no operation)

```
RESERVED:4433 const_DelayWOT_lt3149rpm:fdb $100       ; DATA XREF: WOTInitialEnrichment+88r
RESERVED:4433                                         ; Delayed entry into full power mode at speeds <3149rpm
RESERVED:4435 const_DelayWOT_gt3149rpm:fdb $300       ; DATA XREF: WOTInitialEnrichment:loc_63C3r
RESERVED:4435                                         ; Delayed entry into the full-power mode when speed> 3149rpm
```

disable lambda sensor for open loop tuning g60 triple map
```
x6269 change BD 6D 07 to 01 01 01
```

disable isv - (possibly for boost control)
```
x6287 change BD 66 0C to 01 01 01
```

SNS G60 Digilag removal analysis
You use the load pressure to skip the switch query. take a look at this jump table: 
```
RESERVED: 624E jsr sub_6336 
RESERVED: 6251 jsr sub_4E01 
RESERVED: 6254 jsr sub_69C6 
RESERVED: 6257 jsr sub_6981 
RESERVED: 625A jsr sub_6916 
RESERVED: 625D jsr sub_6A06 
RESERVED: 6260 jsr sub_6141 
RESERVED: 6263 jsr sub_6A4F 
RESERVED: 6266 jsr sub_579F 
RESERVED: 6269 jsr sub_6D07; here is where the code will be inserted, a seperate branch will be called, and then will return to 6D07 when complete allowing the code to continue 
RESERVED: 626C jsr nullsub_1 
RESERVED: 626F jsr sub_6B28 
RESERVED: 6272 jsr sub_6EAF 
RESERVED: 6275 jsr sub_6A55 
RESERVED: 6278 jsr sub_6B65 
RESERVED: 627B jsr sub_6B84 
RESERVED: 627E ldd byte_54 
RESERVED: 6280 std byte_48 
RESERVED: 6282 bsr sub_628E 
RESERVED: 6284 jsr sub_6C39 
RESERVED: 6287 jsr sub_660C 
RESERVED: 628A jsr sub_62B6 
RESERVED: 628D rts 
```
Updated code:
```
RESERVED: 624B jsr sub_690E 
RESERVED: 624E jsr sub_6336 
RESERVED: 6251 jsr sub_4E01 
RESERVED: 6254 jsr sub_69C6 
RESERVED: 6257 jsr sub_6981 
RESERVED: 625A jsr sub_6916 
RESERVED: 625D jsr sub_6A06 
RESERVED: 6260 jsr sub_6141 
RESERVED: 6263 jsr sub_6A4F 
RESERVED: 6266 jsr sub_579F 
RESERVED: 6269 jsr sub_5D00 change made here 
RESERVED: 626C jsr nullsub_1 
RESERVED: 626F jsr sub_6B28 
RESERVED: 6272 jsr sub_6EAF 
RESERVED: 6275 jsr sub_6A55 
RESERVED: 6278 jsr sub_6B65 
RESERVED: 627B jsr sub_6B84 
RESERVED: 627B jsr sub_6B84 
RESERVED: 627E ldd byte_54 
RESERVED: 6280 std byte_48 
RESERVED: 6282 bsr sub_628E 
RESERVED: 6284 jsr sub_6C39 
RESERVED: 6287 jsr sub_660C 
RESERVED: 628A jsr sub_62B6 
RESERVED: 628D rts
```
jumped out DA: 
```
ldaa byte_1 (charge pressure query) 
cmpa # $ 75; 'u' (comparative) 
bcc locret_5D0C 
jmp loc_6D07; jump to the original routine 
; -------------------------------------------------- ------------------------- 
fcb $ 39; 9 
fcb $ 39; 9; only filling material 
fcb $ 39; 9 
; -------------------------------------------------- --------------------RESERVED: 5D0C rts; CODE XREF: sub_5D00 + 4 j; 'abbreviation' 
```

with cmpa # $ XX you can set the starting MAP pressure from which the lambda is skipped. or with another mapsensor you have to change accordingly. 


SNS G40 Digilag custom code

The same principle used in the G60 code, is used on the G40.

The digi-lag feature will delay the activation of the WOT switch for a random amount of time (around 4 seconds) before switching to the WOT fuelling maps. The code below will skip this check and instead allow the activation of the WOT fuelling map by MAP sensor value. 
```
x593D 59(stock) 77(tuned) 
x593E A7(stock) 50(tuned)
x59E5 25(stock) 01(tuned)
x59E6 05(stock) 01(tuned)
x6470 6A(stock) 77(tuned)
x6471 20(stock) 01(tuned)
x6515 03(stock) 01(tuned)
x651A 03(stock) 01(tuned)
x7F01 73(stock) 64(tuned)
x7F07 62(stock) 63(tuned)
x771F-x772D (stock all 41's)
x772E-x774F (stock all 41s)
x7750-x775c (stock all 41s)
x771f-x775c - Custom code in hex - 9601817424087E6A20736E7339393939393939636F707972696768742032303033
20736E7374756E696E672E41414141419601817424047E59A7017E59AC
```

WOT Intial Enrichment table is modified :-
```
x450B-4516 - address location
3A 40 6C 88 B0 B3 B6 BC C8 D0 D6 DE E9 FB FF FF (stock)
3A 40 8C E6 EB EE F1 F4 F7 FA FC FE FF FF FF FF (greater enrichment than stock from 2900rpm)
```

stock code branches to 59A7 (Switches_XX_and_FT), think this is to check that the idle switch isn't pressed (check!)

tuned code branches to 7750(sns digi code) to compare MAP sensor value with a pre-defined value (allows WOT enrichment at user set pressure level) :-
```
593D 59(stock)  / 77(tuned) 
593E A7(stock) / 50(tuned)
```

stock goes to loc_59EC, a loop which makes the ecu wait for a pre-determined amount of time before setting the full throttle switch closed byte, this code will bypass the loop and set the full throttle closed switch straight away.
```
59E5 25(stock) 01(tuned)
59E6 05(stock) 01(tuned)
```

stock code branches to subroutine   sub_6A20

tuned code branches to subroutine   sub_771F (custom code), to provide a comparison against map sensor vs pre-defined value before jumping to sub_6A20.
```
6470 6A(stock) 77(tuned)
6471 20(stock) 01(tuned)
```

Reads from MAP sensor instead of Idle Switch
```
6515 03(stock) 01(tuned) 
ldd     #byte 3 ;idle switch (stock)
ldd     #byte_1 ;map sensor (tuned)
```

Not entirely sure what the above does, believe these to either be a set of 16 bit values, as 7F00 is called in the code, may just be for diagnostics. 
``````
7F01 73(stock) 64(tuned)
7F07 62(stock) 63(tuned)
```

Custom code to provide comparison checks against MAP pressure.
```
771F-772D ( digilag branch code ) - compare $74 against MAP sensor value and jump to loc_6A20 when MAP value is greater
774E (copyright mark SNS)
7750-775A (Digilag branch code) -  compare $74 against MAP sensor value and jump to loc_59A7 when MAP value is greater
```

Decompiled code
```
RESERVED:771F sub_771F:                               ; CODE XREF: sub_643F+30P
RESERVED:771F                 ldaa    byte_1 (Get MAP sensor value)
RESERVED:7721                 cmpa    #$74 ; 't' (Compare MAP sensor value with specified)
RESERVED:7723                 bcc     locret_772D (if its not equal or above, got the 772D)
RESERVED:7725                 jmp     loc_6A20 (calls 6A20 which was originally invoked in the stock code)
RESERVED:772D locret_772D:                            ; CODE XREF: sub_771F+4j
RESERVED:772D                 rts (return back to the calling function )
RESERVED:772D ; End of function sub_771F

RESERVED:7750 sub_7750:                               ; CODE XREF: sub_5841:loc_593CP
RESERVED:7750
RESERVED:7750                 ldaa    byte_1  (Get MAP sensor value)
RESERVED:7752                 cmpa    #$74 ; 't' (Compare MAP sensor value with specified)
RESERVED:7754                 bcc     loc_775A
RESERVED:7756                 jmp     loc_59A7 (calls 59A7 which was originally invoked in the stock code, to check idle switch?)
RESERVED:775A loc_775A:                               ; CODE XREF: sub_7750+4j
RESERVED:775A                 jmp     loc_59AC (need to check what 59AC does, i assume it will just jump back to the original routine, as we havent met the required pressure)
RESERVED:775A ; End of function sub_7750
```
