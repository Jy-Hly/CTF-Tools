#!/usr/bin/python
#Send request with a payload. Tailor the behaviour to your needs.
import requests
import sys, getopt
import random
import string

HELP_STRING = 'sql_injection.py -u <url> [-p <payload>] [-o <output_file>]'

#proxies = {"http": "127.0.0.1:8080"}

def main(argv):
    payload = ''
    filePath = ''
    url = ''
    try:
        opts, args = getopt.getopt(argv, 'hu:p:o:')
    except getopt.GetoptError:
        print(HELP_STRING)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(HELP_STRING)
            sys.exit()
        elif opt == '-o':
            filePath = arg
        elif opt == '-p':
            payload = arg
        elif opt == '-u':
            url = arg
    if url == '':
        print(HELP_STRING)
        sys.exit(2)
    
    s = requests.Session()
    cred = get_random_cred()
    if payload == '':
        payload = input('Payload : ')
    
    ####### CUSTOMIZE THIS PART
    #s.post(url, data = data, proxies = proxies)

    data = {'username': payload, 'password': cred}
    x = s.post(url, data = data)

    #######

    if filePath == '':
        print(x.text)
    else:
         f = open(filePath, "w")
         f.write(x.text)
         f.close() 

    s.close()

def get_random_cred():
    letters = string.ascii_lowercase
    cred = ''.join(random.choice(letters) for i in range(16))
    return cred

if __name__ == "__main__":
    main(sys.argv[1:])