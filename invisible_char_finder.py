#!/usr/bin/python
#Look for invisible unicode char in a file, except for spaces and tabs.
import sys, getopt

def main(argv):
    filePath = ''
    try:
        opts, args = getopt.getopt(argv, 'hf:')
    except getopt.GetoptError:
        BadSyntaxError()
    for opt, arg in opts:
        if opt == '-h':
            print('invisible_char_finder.py -f <path_to_file>')
            sys.exit()
        elif opt == '-f':
            filePath = arg
    if filePath == '':
        BadSyntaxError()
    cpt = CheckFile(filePath)
    print('---------------')
    print(cpt, "invisible characters found.")
    print('---------------')
    sys.exit(0)
    

def CheckFile(filePath):
    f = open(filePath, 'r')
    n = 1
    flag = 0
    cpt = 0
    for line in f:
        l = ''
        for char in line:
            if IsInvisible(ord(char)) == 1:
                flag = 1
                cpt = cpt + 1
                l += '[' + hex(ord(char)) + ']'
            else:
                l += char
        if flag:
            print(n, ': ', l.strip())
            flag = 0
        n += 1
    f.close()
    return cpt

def IsInvisible(val):
    l = [0x1D159, 0x133FC, 0xFFFC, 0xFFA0, 0xFEFF, 0x3164, 0x3000, 0x2800, 0x1160, 0x115F, 0x061C, 0x034F, 0x00AD, 0x00A0]
    l = l + list(range(0x1D173,0x1D17A))
    l = l + list(range(0x17B4,0x17B5))
    l = l + list(range(0x108B,0x180E))
    l = l + list(range(0x2000,0x200F))
    l = l + list(range(0x202A,0x202F))
    l = l + list(range(0x205F,0x206F))
    l = l + list(range(0xFE00,0xFE0F))
    l = l + list(range(0xE0001,0xE01EF))
    if val in l :
        return 1
    else:
        return 0

def BadSyntaxError():
    print('invisible_char_finder.py -f <path_to_file>')
    sys.exit(2)
 

if __name__ == "__main__":
    main(sys.argv[1:])