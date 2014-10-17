# -*- coding: utf-8 -*-
secret = []
with open('cipher1.txt', 'r') as f:
    for line in f:
        secret.append(map(int, line.split(',')))
secret = secret[0]

secret0 = []
for i in xrange(0, 1200):
    if i % 3 == 0:
        secret0.append(secret[i])

secret1 = []
for i in xrange(0, 1200):
    if i % 3 == 1:
        secret1.append(secret[i])

secret2 = []
for i in xrange(0, 1200):
    if i % 3 == 2:
        secret2.append(secret[i])

import re

def try_test(secretid):
    def jiemi(key):
        test = [v ^ ord(key) for i, v in enumerate(secretid)]
        return ''.join(map(chr, test))

    words = [chr(i) for i in range(97,123)]

    dicts = {}
    for word in words:
        str = jiemi(word)
        dicts[word] = len(str) - len(re.findall('[A-Za-z]',str))

    print(sorted(dicts.items(), key=lambda d: d[1]))

try_test(secret0)
try_test(secret1)
try_test(secret2)