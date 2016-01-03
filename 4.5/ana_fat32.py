from struct import *
import sys

class pbr():

    binary = []

    def __init__(self):
        f = open(sys.argv[1])
        self.binary = map(lambda x: int(ord(x)), f.read())

    def getbin(self, length, valtype = None):
        r = self.binary[0:length]
        self.binary = self.binary[length:]

        if valtype == 'string':
            return ''.join(map(chr, r))
        elif valtype == 'int':
            return self.makeBin(r)
        else:
            return ' '.join(map(hex, r))

    def makeBin(self, li):
        b = 0
        for h in reversed(li):
            b = b << 8 | h

        return b

p = pbr()
print "BS_jmpBoot:      %s" % p.getbin(3)
print "BS_OEMName:      '%s'" % p.getbin(8, 'string')
print "BPB_BytsPerSec:  %s" % p.getbin(2, 'int')
print "BPB_SecPerClus:  %s" % p.getbin(1)
print "BPB_RsvdSecCnt:  %s" % p.getbin(2, 'int')
print "BPB_NumFATs:     %s" % p.getbin(1, 'int')
print "BPB_RootEntCnt:  %s" % p.getbin(2, 'int')
print "BPB_TotSec16:    %s" % p.getbin(2, 'int')
print "BPB_Media:       %s" % p.getbin(1)
print "BPB_FATsz16:     %s" % p.getbin(2, 'int')
print "BPB_SecPerTrk:   %s" % p.getbin(2, 'int')
print "BPB_NumHeads:    %s" % p.getbin(2, 'int')
print "BPB_HiddSec:     %s" % p.getbin(4, 'int')
print "BPB_TotSec32:    %s" % p.getbin(4, 'int')
print "BPB_FATSz32:     %s" % p.getbin(4, 'int')
print "BPB_ExtFlags:    %s" % p.getbin(2)
print "BPB_FSVer:       %s" % p.getbin(2)
print "BPB_RootClus:    %s" % p.getbin(4, 'int')
print "BPB_FSInfo:      %s" % p.getbin(2, 'int')
print "BPB_BkBootSec:   %s" % p.getbin(2, 'int')
print "BPB_Reserved:    %s" % p.getbin(12)
print "BPB_DrvNum:      %s" % p.getbin(1, 'int')
print "BPB_Reserved1:   %s" % p.getbin(1)
print "BPB_BootSig      %s" % p.getbin(1)
print "BPB_VolID:       %s" % p.getbin(4)
print "BPB_VolLab:      '%s'" % p.getbin(11, 'string')
print "BPB_FileSysType: '%s'" % p.getbin(8, 'string')
