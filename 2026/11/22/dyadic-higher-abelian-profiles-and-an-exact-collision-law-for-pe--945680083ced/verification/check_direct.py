#!/usr/bin/env python3
"""Independent explicit-factor check of dyadic three-Abelian predictions."""
from collections import Counter
from fractions import Fraction
from itertools import product


def images(k):
    a, b = '0', '1'
    for _ in range(k):
        a, b = (''.join('01' if x == '0' else '00' for x in w)
                for w in (a, b))
    return a, b


def signature(word, ell):
    # All overlapping length-1,...,ell factor counts, not str.count.
    return tuple(sum(word[j:j+r] == ''.join(w)
                     for j in range(len(word)-r+1))
                 for r in range(1, ell+1)
                 for w in product('01', repeat=r))


def main():
    for k in range(4, 10):
        L = 1 << k
        words = images(k)
        profile = {}
        for a in (0, 1):
            for r in range(L):
                word = words[a][r:] + words[a][:r]
                profile[(a, r)] = signature(word, 3)
        classes = set(profile.values())
        assert len(classes) == 12, (k, len(classes))
        expected = Counter()
        measured = Counter()
        for a in (0, 1):
            for r in range(L):
                w = words[a]
                local = (w+w+w)[L+r-2:L+r+2]
                expected[(a, local)] += 1
                measured[profile[(a,r)]] += 1
        assert len(expected) == len(classes)
        assert sorted(measured.values()) == sorted(expected.values())
        # Every label corresponds to exactly one full 3-Abelian profile.
        classes_to_labels = {}
        for key, value in profile.items():
            a,r=key
            w=words[a]
            local=(w+w+w)[L+r-2:L+r+2]
            old=classes_to_labels.setdefault(value,(a,local))
            assert old == (a,local)
        delta = (-1)**k
        B0,C0=(L+2*delta)//6,(L-4*delta)//6
        B1,C1=(L-4*delta)//6,(L+8*delta)//6
        for a,(B,C) in enumerate(((B0,C0),(B1,C1))):
            for v in ('0001','0010','0100','1000'):
                assert expected[(a,v)] == B,(k,a,v,expected[(a,v)],B)
            for v in ('0101','1010'):
                assert expected[(a,v)] == C,(k,a,v,expected[(a,v)],C)
        pi=(Fraction(2,3),Fraction(1,3))
        collision=sum((pi[a]*count/L)**2 for (a,v),count in expected.items())
        formula=Fraction(5,54)+Fraction(32,27*L**2)
        assert collision == formula,(k,collision,formula)
        print('k=',k,'length=',L,'classes=',len(classes),
              'collision=',str(collision))
    print('DIRECT_OK')

if __name__=='__main__': main()
