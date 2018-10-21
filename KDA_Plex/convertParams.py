__author__ = 'plex'

import math


class convertclass():

    def freq_kolenval(self, freq_hex):
        if freq_hex > 0xF0:
            freq_hex = 0xF0
        #table from addr 0x4500
        Table_RazbivkaChastot = [0x94D, 0xA48, 0xB7D, 0xD05, 0xF38, 0x10FC, 0x129A, 0x1434, 0x1A0B, 0x1D4C, 0x2278, 0x2710, 0x32F3, 0x493E, 0x61A8, 0x7A12]
        #Table_RazbivkaChastot = [0x0850, 0x094D, 0x0A48, 0x0B7D, 0x0D05, 0x0F38, 0x129A, 0x1434, 0x1A0B, 0x1D4C, 0x2278, 0x2710, 0x32F3, 0x493E, 0x61A8, 0x7A12]

        table_rpm = []
        for i in Table_RazbivkaChastot:
            table_rpm.append(15000000.0 / i)
        p = freq_hex / 16
        if freq_hex != 0xF0:
            interpolation = (0.0 + table_rpm[p + 1] - table_rpm[p]) * (freq_hex % 16) / 16
        else:
            interpolation = 0
        x = int(table_rpm[p] + interpolation)
        #print "//Table_RazbivkaChastot = [%s]" % ", ".join(str(int(i)) for i in table_rpm)
        #print "convertFreqKolenval('%s') = %s rpm" % (hex(freq_hex), x)
        return x

    def freq_raspredval(self, freq_hex):
        if freq_hex > 0xF0:
            freq_hex = 0xF0
        #table from addr 0x4733
        Table_IdleRazbivkaChastot = [0x4940, 0x4CC0, 0x50A0, 0x54F0, 0x59A8, 0x5F08, 0x6508, 0x6BD0, 0x73B0, 0x7CA8, 0x8728, 0x93C8, 0xA2C0, 0xB520, 0xCC88, 0xEA60]

        table_idle_rpm = []
        for i in Table_IdleRazbivkaChastot:
            table_idle_rpm.append(30000000.0 / i)

        p = freq_hex / 16
        if freq_hex != 0xF0:
            interpolation = (0.0 + table_idle_rpm[p + 1] - table_idle_rpm[p]) * (freq_hex % 16) / 16
        else:
            interpolation = 0
        x = int(table_idle_rpm[p] + interpolation)
        print "//Table_IdleRazbivkaChastot = [%s]" % ", ".join(str(int(i)) for i in table_idle_rpm)
        print "convertFreqRaspredval('%s') = %s rpm" % (hex(freq_hex), x)
        return x

    def press(self, press_hex):
        tair = float(press_hex)
        bar = 1.95 * (tair/255 + 0.04)
        #bar = 1.95 * (tair/255)
        #print "convertPress('%s') = %s bar (abs)" % (hex(press_hex), bar)
        return bar

    def tcol(self, tcol_hex):
        tcol = tcol_hex

        #checks
        if tcol > 0xFE:
            tcol = 0xFE
        elif tcol < 1:
            tcol = 1

        #convert
        value = float(tcol)

        #termistor resistance
        Rtcol = 11000.0 * value / (255.0 - value)

        #ln R
        p = math.log(Rtcol)

        #modified Steinhart-Hart equation
        x_Kelvin = 1.0 / (0.000002787383950483 * (p*p*p) - 0.000055038753003273 * (p*p) + 0.000643078560461730 * p + 0.000411613636451733)
        x_Celsius = x_Kelvin - 273.13

        print "convertTcol('%s') = %s C (R = %s Ohms)" % (hex(tcol_hex), x_Celsius, int(Rtcol))
        return x_Celsius
    def tcol_old(self, tcol_hex):
        tcol = tcol_hex

        #checks
        if tcol > 0xF5:
            tcol = 0xFE
        elif tcol < 4:
            tcol = 4

        #convert
        value = float(tcol)

        #modified steinhart-hart conversion
        Rtcol = 11000.0 * (value/51) / (5.0 - (value/51))
        p = math.log(Rtcol/2200)
        x_Kelvin = 1.0 / (0.00000006752780000000001 * (p*p*p) + 0.000002626311 * (p*p) + 0.0002569355 * p + 0.003354016)
        x_Celsius = x_Kelvin - 273.13

        print "convertTcol('%s') = %s C (R = %s Ohms)" % (hex(tcol_hex), x_Celsius, int(Rtcol))
        return x_Celsius

    def tair(self, tair_hex):
        tair = tair_hex

        #checks
        if tair > 0xFE:
            tair = 0xFE
        elif tair < 1:
            tair = 1

        #convert
        value = float(tair)

        print 'U = %s' % (value/51.0)

        #termistor resistance
        Rtair = 1300.0 * value / (255.0 - value)

        #ln R
        p = math.log(Rtair)

        #modified Steinhart-Hart equation
        x_Kelvin = 1.0 / (0.000002787383950483 * (p*p*p) - 0.000055038753003273 * (p*p) + 0.000643078560461730 * p + 0.000411613636451733)
        x_Celsius = x_Kelvin - 273.13

        print "convertTair('%s') = %s C (R = %s Ohms)" % (hex(tair_hex), x_Celsius, int(Rtair))
        return x_Celsius
    def tair_old(self, tair_hex):
        tair = tair_hex

        #checks
        if tair > 0xF5:
            tair = 0xFE
        elif tair < 4:
            tair = 4

        #convert
        value = float(tair)
        Rtair = 1300.0 * (value/51) / (5.0 - (value/51))
        p = math.log(Rtair/2200)
        x_Kelvin = 1.0 / (0.00000006752780000000001 * (p*p*p) + 0.000002626311 * (p*p) + 0.0002569355 * p + 0.003354016)
        x_Celsius = x_Kelvin - 273.13

        print "convertTair('%s') = %s C (R = %s Ohms)" % (hex(tair_hex), x_Celsius, int(Rtair))
        return x_Celsius

    def tinj(self, tinj_hex):
        tinj = float(tinj_hex)

        x = tinj/500
        if x > 15.0:
            x = 15.0
        if x < 0.0:
            x = 0.0

        #print "convertTinj('%s') = %s ms" % (hex(tinj_hex), x)
        return x

    def uoz(self, uoz_hex):
        uoz = float(uoz_hex)

        #KDA version
        #x = (193 - uoz) * 0.5

        #from TunerPro
        x = 78 - 90 * (uoz/256)

        """
        if x > 40.0:
            x = 40.0
        if x < 0.0:
            x = 0.0
        """

        #print "convertUOZ('%s') = %s deg." % (hex(uoz_hex), x)
        return x
    def otkat_uoz(self, uoz_hex):
        uoz = float(uoz_hex)
        x = 90 * (uoz/256)
        print "otkat_UOZ('%s') = %s deg." % (hex(uoz_hex), x)
        return x

    def co(self, co_hex):
        #convert
        u_adc = float(co_hex)/51
        r_co = 1000.0 * u_adc / (5.0 - u_adc)

        print "convertCO('%s') = %s Ohms" % (hex(co_hex), r_co)
        return r_co


    def Lambda(self, lambda_hex):
        x = float(lambda_hex)/100
        print "convertLambda('%s') = %s V" % (hex(lambda_hex), x)
        return x

    def tinjlambda(self, tinjlambda_hex):
        tinjlambda = float(tinjlambda_hex)
        if tinjlambda <= 0x7F:
           x = tinjlambda / 4
        else:
           x = - (0x100 - tinjlambda) / 4

        print "convertTinjLambda('%s') = %s %%" % (hex(tinjlambda_hex), x)
        return x

    def otkatuoz(self, knock_hex):
        x = float(knock_hex)/36 * 100
        print "convertOtkatUOZ('%s') = %s %%" % (hex(knock_hex), x)
        return x

    def xxopenvalve(self, xxopenvalve_hex):
        x = float(xxopenvalve_hex)/255 * 100
        print "convertXXopenValve('%s') = %s %%" % (hex(xxopenvalve_hex), x)
        return x

    def idle_LC1(self, bIdle_hex):
        bIdle = float(bIdle_hex)
        x = (bIdle + 2) * 0.0040117142054800014402 + 0.5
        print "convertIdle_LC1('%s') = %s Alpha" % (hex(bIdle_hex), x)
        return x

    def ubat(self, ubat_hex):
        x = float(ubat_hex)*24/255
        #print "convertUbat('%s') = %s V" % (hex(ubat_hex), x)
        return x

    def FperiodRaspredval(self, FperiodRaspr_hex):
        FperiodRaspr = float(FperiodRaspr_hex)
        x = 30000000 / FperiodRaspr_hex
        print "FperiodRaspredval('%s') = %s rpm kolenvala" % (hex(FperiodRaspr_hex), x)
        return x

    def FperiodKolenval(self, FperiodKolen_hex):
        FperiodKolen = float(FperiodKolen_hex)
        x = 15000000 / FperiodKolen_hex
        print "FperiodKolenval('%s') = %s rpm kolenvala" % (hex(FperiodKolen_hex), x)
        return x

class Tables():

    def __init__(self):
        self.convert = convertclass()

        # ---------- TABLES ----------
        #0x462E
        self.Table_TinjAdjustmentByUbat = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0x80, 0x48, 0x32, 0x20, 0x15, 0xC, 5, 0, 0, 0, 0]
        #0x460C
        self.Table_DobavkaByTcol_First32cycles = [0x10, 0x25, 0x25, 0x27, 0x29, 0x3A, 0x53, 0x63, 0x78, 0x8D, 0xA2, 0xB8, 0xC9, 0xD2, 0xD9, 0xE2, 0x64]
        #0x461D
        self.Table_TinjAdjustmentByTcol_ExtraLowRPM = [0, 0, 0xD, 0x15, 0x1C, 0x2B, 0x3B, 0x43, 0x54, 0x6C, 0x88, 0xA1, 0xB5, 0xBB, 0xC3, 0xCB, 0x58]

    def _interpolation(self, t_i, t_i_1, p):
        return (t_i * (16 - p) + (t_i_1 * p) + 8) / 16

    def ReadByteFromT16_interp(self, table, B):
        if len(table) != 16 and len(table) != 17:
            raise Exception('Table must be 16-17 bytes!')
        for i in table:
            if i > 255:
                raise Exception('Item size must be 1 byte!')
        if B > 255:
            raise Exception('B must be 1 byte!')

        b3__0 = B % 16
        b7__4 = B / 16

        return self._interpolation(table[b7__4], table[b7__4 + 1], b3__0) % 256

    def TinjAdjustmentByUbat(self, B=-1, step=16):
        #injector lag
        if B == -1:
            #print table
            for ubat in xrange(0,256,16):
                value = self.ReadByteFromT16_interp(self.Table_TinjAdjustmentByUbat, ubat)
                adjust = 8*value + 0xE
                print "%.2f V  \t%sms" % (self.convert.ubat(ubat), self.convert.tinj(adjust))
        else:
            #calc adjust
            value = self.ReadByteFromT16_interp(self.Table_TinjAdjustmentByUbat, B)
            adjust = 8*value + 0xE
            return self.convert.tinj(adjust)

    def StartInjPlusCount(self, B=-1, step=16):
        if B == -1:
            for tcol in xrange(0,256,16):
                bStartInjPlus = self.ReadByteFromT16_interp(self.Table_DobavkaByTcol_First32cycles, tcol)
                adjust = 8*bStartInjPlus
                print "%.2f C  \t%sms" % (self.convert.tcol(tcol), self.convert.tinj(adjust))
        else:
            bStartInjPlus = self.ReadByteFromT16_interp(self.Table_DobavkaByTcol_First32cycles, B)
            adjust = 8*bStartInjPlus
            return self.convert.tinj(adjust)

    def TinjAdjustmentByTcol_ExtraLowRPM(self, B=-1, step=16):
        if B == -1:
            for tcol in xrange(0,256,16):
                value = self.ReadByteFromT16_interp(self.Table_TinjAdjustmentByTcol_ExtraLowRPM, tcol)
                adjust = 8*value
                print "%.2f C  \t%sms" % (self.convert.tcol(tcol), self.convert.tinj(adjust))
        else:
            value = self.ReadByteFromT16_interp(self.Table_TinjAdjustmentByTcol_ExtraLowRPM, B)
            adjust = 8*value
            return self.convert.tinj(adjust)

    def Antilog(self, wTinj):
        Table_AntiLog = [0x80, 0x86, 0x8C, 0x92, 0x98, 0x9F, 0xA6, 0xAD, 0xB5, 0xBD, 0xC5, 0xCE, 0xD7, 0xE1, 0xEB, 0xF5, 0xFF]
        value = wTinj

        if value > 0x9FF:
            value = 0x9FF

        B = self.ReadByteFromT16_interp(Table_AntiLog, value & 0xFF)
        stepen = value/0x100 - 1

        return int(B*pow(2, stepen))


conv = convertclass()
tables = Tables()
print conv.press(0xB0)

exit(1)
