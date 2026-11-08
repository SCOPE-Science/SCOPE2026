#!/usr/bin/env python3
"""Independent finite checks for weighted circular antisquare-good word spectra.

The proof in RESULT.md is valid for all lengths; this checker performs finite
independent comparisons only. Python 3 standard library, no external data.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb

F = ('0011', '1100', '0110', '1001',
     '010101', '101010', '001011', '110100')


def f_avoids(word):
    n = len(word)
    wrapped = word * (1 + (n + 6) // n)
    return all(wrapped[i:i+len(pat)] != pat
               for pat in F for i in range(n))


def direct_good(word, max_order):
    n = len(word)
    wrapped = word * (2 + (2 * max_order) // n)
    for k in range(2, max_order+1):
        for i in range(n):
            v = wrapped[i:i+2*k]
            if all(v[j] != v[k+j] for j in range(k)):
                return False
    return True


def predicted_minority(n, t):
    out = Fraction(0)
    for s in range(t//2+1):
        long_gaps = t-s
        extra = n-4*t+2*s
        if extra >= 0:
            out += Fraction(n, long_gaps)*comb(long_gaps, s)*comb(extra+long_gaps-1, long_gaps-1)
    assert out.denominator == 1
    return int(out)


def predicted(n):
    v = Counter({0:1, n:1})
    for t in range(1, (n-1)//2+1):
        c = predicted_minority(n,t)
        if c:
            v[t] += c
            v[n-t] += c
    return v


def debruijn_transitions():
    trans = [[] for _ in range(32)]
    for state in range(32):
        for bit in (0,1):
            six = f'{state:05b}' + str(bit)
            if not any(six.endswith(v) for v in F):
                trans[state].append(((2*state+bit)%32, bit))
    return trans


def trace_counts_upto(nmax):
    trans = debruijn_transitions()
    output = [Counter() for _ in range(nmax+1)]
    for start in range(32):
        current = {(start,0):1}
        for step in range(1,nmax+1):
            nxt = defaultdict(int)
            for (state,weight), count in current.items():
                for state2,bit in trans[state]:
                    nxt[(state2,weight+bit)] += count
            current = nxt
            for (state,weight), count in current.items():
                if state==start:
                    output[step][weight] += count
    return output


def main():
    tested=0; direct_cases=0
    for n in range(1,17):
        tally=Counter()
        for bits in range(1<<n):
            word=''.join(str((bits>>i)&1) for i in range(n))
            valid=f_avoids(word)
            if n<=11:
                # At order 3*n, any observed obstruction has a concrete witness.
                assert valid==direct_good(word,3*n), (n,word)
                direct_cases+=1
            if valid:
                tally[word.count('1')] += 1
        assert tally==predicted(n),(n,tally,predicted(n))
        tested += 1<<n
    trace=trace_counts_upto(40)
    for n in range(1,41):
        assert trace[n]==predicted(n), (n,trace[n],predicted(n))
    for n in range(1,121):
        tally=predicted(n)
        for t in range(1,n):
            e = 3*min(t,n-t) + (min(t,n-t)%2)
            assert (t in tally)==(n>=e), (n,t)
    print('VERIFY_OK')
    print('binary_words_exhausted=', tested)
    print('direct_antisquare_comparisons=',direct_cases)
    print('independent_transfer_length_checks=40')
    print('sharp_weight_support_checks=120')
    print('P_4=',sum(predicted(4).values()), 'P_12=',sum(predicted(12).values()),'P_16=',sum(predicted(16).values()))


if __name__=='__main__':
    main()
