#!/usr/bin/env python3
"""Independent exhaustive input-block checks of Rule 126 image languages and minimal obstructions."""
from itertools import product
from pathlib import Path
import json

def step(a):
    return [int(not(a[i]==a[i+1]==a[i+2])) for i in range(len(a)-2)]

def image_words(t,n):
    out=set()
    for a in product((0,1),repeat=n+2*t):
        v=list(a)
        for _ in range(t):v=step(v)
        out.add(''.join(map(str,v)))
    return out

def main():
    basic=json.loads((Path(__file__).parent/'certificate.json').read_text())
    forbidden=json.loads((Path(__file__).parent/'forbidden_certificate.json').read_text())
    preceding={'',}
    for n in range(1,15):
        first=image_words(1,n);second=image_words(2,n)
        assert len(first)==basic['1']['counts'][n]
        assert len(second)==basic['2']['counts'][n]
        assert second<=first
        if n<=11:assert first==second
        if n==12:assert first-second=={'011101101110'}
        minimal={w for w in (set(map(''.join,product('01',repeat=n)))-second)
                 if n==1 or (w[:-1] in preceding and w[1:] in preceding)}
        assert len(minimal)==forbidden['minimal_forbidden_counts'][n], (n, len(minimal))
        preceding=second
    print('CROSSCHECK_OK: exhaustive independent image and first-offender counts through length 14')

if __name__=='__main__':main()
