#!/usr/bin/env python3
"""Exact insertion-neighbourhood verification for ordered adjacent-pair spectra.

All source words and spectra are linear. Only the Python standard library is used.
"""
from itertools import product
from math import factorial


def pair_profile(w, q):
    count = [0] * (q * q)
    for a, b in zip(w, w[1:]):
        count[q * a + b] += 1
    return tuple(count)


def literal_insertion_profile_count(w, q):
    images = set()
    for i in range(len(w) + 1):
        for a in range(q):
            images.add(pair_profile(w[:i] + (a,) + w[i:], q))
    return len(images)


def predicted_count(w, q):
    pairs = set(zip(w, w[1:]))
    loops = sum((a, a) in pairs for a in range(q))
    transitions = sum(a != b for a, b in pairs)
    return (len(set(w)) + (q - 1) * loops + (q - 2) * transitions
            + 2 * (q - 1) - (w[0] != w[-1]))


def de_bruijn_linear(q):
    # Canonical de Bruijn recursion, with every directed pair occurring once.
    a = [0] * (2 * q + 2)
    sequence = []
    def db(t, p):
        if t > 2:
            if 2 % p == 0:
                sequence.extend(a[1:p + 1])
        else:
            a[t] = a[t-p]
            db(t+1,p)
            for j in range(a[t-p]+1,q):
                a[t] = j
                db(t+1,t)
    db(1,1)
    assert len(sequence)==q*q
    word = tuple(sequence + sequence[:1])
    assert len(set(zip(word,word[1:]))) == q*q
    assert word[0] == word[-1]
    return word


def check_signature_taxonomy(q):
    # A signed change vector is an exact integer vector over the q^2 ordered pairs.
    loop = set()
    nondegenerate = set()
    for a,b,c in product(range(q), repeat=3):
        d=[0]*(q*q)
        d[q*a+c]+=1
        d[q*c+b]+=1
        d[q*a+b]-=1
        if c==a or c==b:
            loop.add(tuple(d))
        else:
            nondegenerate.add(tuple(d))
    assert len(loop)==q
    assert len(nondegenerate)==q*(q-1)**2
    assert loop.isdisjoint(nondegenerate)
    return len(loop),len(nondegenerate)


def main():
    direct_cases = 0
    for q, cap in [(2,10),(3,8),(4,5),(5,4)]:
        for n in range(1,cap+1):
            for w in product(range(q),repeat=n):
                assert predicted_count(w,q)==literal_insertion_profile_count(w,q), (q,n,w)
                direct_cases += 1
        check_signature_taxonomy(q)
        print(f"exact_direct_check alphabet={q} lengths=1..{cap} passed")

    for q in range(2,8):
        w=de_bruijn_linear(q)
        cap=q*(q-1)**2+3*q-2
        assert literal_insertion_profile_count(w,q)==cap
        for extra in range(1,8):
            z=w+(w[0],)*extra
            assert predicted_count(z,q)==cap
            if extra<=2:
                assert literal_insertion_profile_count(z,q)==cap
        print(f"sharp_witness alphabet={q} first_length={len(w)} capacity={cap} word={''.join(map(str,w)) if q<=4 else 'omitted'}")

    # Exact q=3 shortest-maximizer census, independent of the Euler-cycle count.
    q=3; n=10; cap=q*(q-1)**2+3*q-2
    num=0
    for w in product(range(q),repeat=n):
        observed=literal_insertion_profile_count(w,q)
        assert observed==predicted_count(w,q)
        if observed==cap:
            num+=1
            assert len(set(zip(w,w[1:])))==q*q and w[0]==w[-1]
    direct_cases += q**n
    assert num == factorial(q)**q == 216
    print(f"exact_shortest_census alphabet=3 length=10 maximizers={num}")
    print(f"total_literal_comparisons={direct_cases}")
    print("ALL CHECKS PASSED")

if __name__ == '__main__':
    main()
