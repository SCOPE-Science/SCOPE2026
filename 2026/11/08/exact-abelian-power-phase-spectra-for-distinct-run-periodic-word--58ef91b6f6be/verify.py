#!/usr/bin/env python3
"""Independent finite tests of an exact abelian-power phase formula.

This program is finite corroboration, not a substitute for the proof.
Run: python3 verify.py
No third-party modules or external inputs are required.
"""
from collections import Counter
from itertools import product
from random import Random


def theoretical(run_lengths, period, exponent):
    length = sum(run_lengths)
    r = period % length
    if r == 0:
        return length, length
    t = min(r, length-r)
    n = sum(max(0, a-exponent*t+1) for a in run_lengths)
    if exponent*period < length:
        distinct = sum(a >= exponent*period for a in run_lengths)
    else:
        distinct = n
    return n, distinct


def predicted_phases(run_lengths, period, exponent):
    period_word=''.join(chr(65+i)*a for i,a in enumerate(run_lengths))
    L=len(period_word)
    r=period%L
    if r == 0:
        return set(range(L))
    t=min(r,L-r)
    result=set()
    for s in range(L):
        start=s if r <= L//2 else s-exponent*t
        fragment=''.join(period_word[(start+j)%L] for j in range(exponent*t))
        if len(set(fragment))==1:
            result.add(s)
    return result


def brute(run_lengths, period, exponent):
    q = len(run_lengths)
    pword = ''.join(chr(65+i)*a for i, a in enumerate(run_lengths))
    L = len(pword)
    target = exponent*period
    host = pword * ((target+L-1)//L+2)
    phases = []
    factors = set()
    for phase in range(L):
        pieces = [host[phase+j*period:phase+(j+1)*period]
                  for j in range(exponent)]
        parikhs = [tuple(piece.count(chr(65+i)) for i in range(q))
                   for piece in pieces]
        if all(v == parikhs[0] for v in parikhs):
            phases.append(phase)
            factors.add(''.join(pieces))
    return len(phases), len(factors), set(phases)


def run():
    cases = 0
    for q in (3,4,5):
        for lens in product(range(1,5), repeat=q):
            L = sum(lens)
            for p in range(1,L+3):
                for e in (2,3,4,5):
                    got = brute(lens,p,e)
                    expected = theoretical(lens,p,e)
                    assert got[:2] == expected,(lens,p,e,got,expected)
                    assert got[2] == predicted_phases(lens,p,e),(lens,p,e,got[2],predicted_phases(lens,p,e))
                    cases += 1
    rng = Random(2026)
    random_cases=0
    for _ in range(800):
        q = rng.randint(3,8)
        lens = tuple(rng.randint(1,12) for _ in range(q))
        L = sum(lens)
        p = rng.randint(1,3*L+7)
        e = rng.randint(2,8)
        got=brute(lens,p,e)
        expected=theoretical(lens,p,e)
        assert got[:2]==expected,(lens,p,e,got,expected)
        assert got[2]==predicted_phases(lens,p,e),(lens,p,e,got[2],predicted_phases(lens,p,e))
        random_cases+=1
    # Q=2 is excluded: 0011 has two abelian squares of half-length 2.
    assert brute((2,2),2,2)[:2] == (2,2)
    assert theoretical((2,2),2,2) == (0,0)
    print('PASS exhaustive:', cases)
    print('PASS independent large randomized:', random_cases)
    print('PASS sharp two-letter exclusion')


if __name__=='__main__': run()
