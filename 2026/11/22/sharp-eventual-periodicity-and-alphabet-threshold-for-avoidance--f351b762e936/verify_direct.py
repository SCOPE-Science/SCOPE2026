#!/usr/bin/env python3
"""Independent exhaustive substring tests for finite lengths and return-word witnesses."""
from itertools import product


def admissible(word, orders):
    for r in orders:
        for i in range(len(word) - 2*r + 1):
            if sorted(word[i:i+r]) == sorted(word[i+r:i+2*r]):
                return False
    return True


def counts_binary():
    counts=[]
    for n in range(14):
        words=[''.join(w) for w in product('01', repeat=n) if admissible(''.join(w),(2,3))]
        counts.append(len(words))
        if n>=8:
            p='000111' * ((n//6)+3)
            factors={''.join(p[(j+k)%6] for k in range(n)) for j in range(6)}
            assert set(words)==factors, (n, set(words)^factors)
    assert counts[:8]==[1,2,4,8,10,12,10,8],counts
    assert counts[8:]==[6]*6,counts
    return counts


def return_word_test(seed, options, orders, maxblocks=4):
    assert len({len(t) for t in options})==1
    assert all((seed+t).endswith(seed) and admissible(seed+t,orders) for t in options)
    for m in range(1,maxblocks+1):
        for choice in product(options,repeat=m):
            s=seed+''.join(choice)
            assert admissible(s,orders), (seed,options,orders,s)
    return len(options[0])

if __name__=='__main__':
    print('counts', counts_binary())
    print('ternary',return_word_test('00011',('100011','200011'),(2,3)))
    print('binary-order-2-only',return_word_test('000',('1000111000','1110001000'),(2,)))
    print('binary-order-3-only',return_word_test('00011',('10000011','11100011'),(3,)))
    print('PASS: finite brute force and independent concatenation checks')
