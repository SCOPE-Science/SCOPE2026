#!/usr/bin/env python3
"""Finite checks for an explicit binary shift defined by sparse forbidden words.

All infinite assertions require the accompanying mathematical proof.
"""
from itertools import product

def words(n):
    for symbols in product('01', repeat=n):
        yield ''.join(symbols)

def in_language(w):
    # Exact finite-factor criterion proved separately using two-sided extensions.
    return '1000' not in w and '1110' not in w and not ('000' in w and '111' in w)

def predicted_minimal(n):
    out = set()
    if n == 4:
        out.update(('1000', '1110'))
    if n == 6:
        out.add('000111')
    if n >= 8:
        for u in words(n-6):
            if u.startswith('1') and u.endswith('0') and '000' not in u and '111' not in u:
                out.add('000'+u+'111')
    return out

def fibonacci(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

def main():
    total=0
    for n in range(1,17):
        raw=list(words(n))
        lang={w for w in raw if in_language(w)}
        expected=2*fibonacci(n+2)-2
        assert len(lang)==expected,(n,len(lang),expected)
        actual={w for w in raw if w not in lang and in_language(w[1:]) and in_language(w[:-1])}
        assert actual==predicted_minimal(n),(n,actual^predicted_minimal(n))
        total+=len(raw)
    for m in range(0,12):
        family={'000'+u+'1'*(m*m+3) for u in words(m)}
        assert len(family)==2**m
        assert {len(w) for w in family}=={m*m+m+6}
        total+=len(family)
    print(f'PASS: {total} exact finite strings checked; lengths 1..16 and sparse-family levels 0..11.')
    print('These finite checks are not proofs of infinite-language, entropy, or novelty assertions.')
if __name__=='__main__':
    main()
