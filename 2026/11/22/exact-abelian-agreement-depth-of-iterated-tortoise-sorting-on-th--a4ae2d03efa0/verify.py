#!/usr/bin/env python3
"""Reproducible finite checks for a Thue--Morse tortoise threshold theorem.

No third-party dependencies. Checks are illustrative; the accompanying proof
establishes the unbounded statement.
"""
from itertools import product


def mu(w):
    return b''.join((b'01' if a == 48 else b'10') for a in w)


def tortoise(w):
    q = w.find(b'1')
    return w if q < 0 else w[:q] + w[q+1:] + b'1'


def closed_form(w, k):
    ones = [j for j, x in enumerate(w) if x == 49]
    if len(ones) <= k:
        return b'0'*(len(w)-len(ones)) + b'1'*len(ones)
    j = ones[k-1]
    return b'0'*(j-k+1) + w[j+1:] + b'1'*k


def factors(n):
    m = (n-1).bit_length()
    x = b'0'
    y = b'1'
    for _ in range(m):
        x, y = mu(x), mu(y)
    return {p[i:i+n] for a,b in product((x,y),repeat=2)
            for p in [a+b] for i in range(len(p)-n+1)}


def t(j):
    return j.bit_count() % 2


def witness(k):
    r = max(2,(k+1).bit_length())
    while (r - (k-1).bit_count()) % 2:
        r += 1
    i = (1 << r) - k
    left = bytes(48+t(j) for j in range(2*i,2*i+2*k+1))
    right = bytes(48+t(j) for j in range(2*i+1,2*i+2*k+2))
    return i,left,right


def main():
    total = 0
    for n in range(1,12):
        for tpl in product((48,49),repeat=n):
            w = bytes(tpl)
            x = w
            for k in range(1,n+3):
                x = tortoise(x)
                assert x == closed_form(w,k), (w,k)
                total += 1
    assert total == 49150, total  # sum_{n=1}^{11} 2^n*(n+2)
    cases = 0
    for k in range(1,129):
        for n in (2*k,2*k+1):
            fs = factors(n)
            im = {closed_form(w,k) for w in fs}
            ab = {w.count(b'1') for w in fs}
            assert len(ab)==(3 if n%2==0 else 2),(k,n,ab)
            assert len(im)==(len(ab) if n%2==0 else len(ab)+1),(k,n)
            cases += len(fs)
        i,left,right=witness(k)
        assert t(i)==0 and t(i+k)==1
        assert left.count(b"1") == right.count(b"1")
        assert left.count(b'1')==k+1 and right.count(b'1')==k+1
        assert left[-1:]==b'1' and right[-1:]==b'0'
        assert closed_form(left,k)==b'0'*k+b'1'*(k+1)
        assert closed_form(right,k)==b'0'*(k-1)+b'10'+b'1'*k
        assert left in factors(2*k+1) and right in factors(2*k+1)
    short_checks=0
    for k in range(1,21):
        for n in range(1,2*k+1):
            fs=factors(n)
            assert len({closed_form(w,k) for w in fs})==len({w.count(b'1') for w in fs})
            short_checks+=1
    print('VERIFY_OK')
    print('exhaustive_binary_word_iteration_cases',total)
    print('complete_morphic_factor_cases',cases)
    print('iterates_tested',128)
    print('all_shorter_length_cases',short_checks)
    print('last_witness_offset',witness(128)[0])

if __name__=='__main__':
    main()
