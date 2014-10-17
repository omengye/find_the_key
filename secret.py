# -*- coding: utf-8 -*-

def find_key(key):
    secret = []
    with open('cipher1.txt', 'r') as f:
        for line in f:
            secret.append(map(int, line.split(',')))
    secret = secret[0]
    # print ''.join(map(chr, secret))

    l = len(key)
    jiemi = [v ^ ord(key[i % l]) for i, v in enumerate(secret)]
    print(''.join(map(chr, jiemi)))

find_key('god')