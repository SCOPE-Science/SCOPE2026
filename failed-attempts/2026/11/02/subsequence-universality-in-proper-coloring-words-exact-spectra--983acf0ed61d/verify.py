#!/usr/bin/env python3
"""Independent finite checks for proper-alphabet word universality enumeration.

Run: python3 verify.py. Standard-library only. All host words are labeled.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, factorial


def arch_index(word, q):
    seen = set()
    count = 0
    for a in word:
        seen.add(a)
        if len(seen) == q:
            seen.clear()
            count += 1
    return count


def is_subsequence(pattern, word):
    i = 0
    for c in word:
        if i < len(pattern) and c == pattern[i]:
            i += 1
    return i == len(pattern)


def first_arch_counts(q, nmax, prior):
    # Independent DP on actual letter-mask states, not the analytic stage formula.
    states = {(0, prior): 1}
    suffix = [1]
    arches = [0]
    all_mask = (1 << q) - 1
    for n in range(1, nmax + 1):
        nxt = defaultdict(int)
        complete = 0
        for (mask, last), mult in states.items():
            for c in range(q):
                if c == last:
                    continue
                new_mask = mask | (1 << c)
                if new_mask == all_mask:
                    complete += mult
                else:
                    nxt[(new_mask, c)] += mult
        suffix.append(sum(nxt.values()))
        arches.append(complete)
        states = nxt
    return arches, suffix


def analytic_counts(q, nmax):
    # Expand the claimed rational stage products as formal power series.
    one = [1] + [0]*nmax
    zero = [0]*(nmax+1)
    def shift(a):
        return [0]+a[:-1]
    e = one
    a = zero
    su = list(one)
    for j in range(1,q):
        geom = [pow(j-1,i) for i in range(nmax+1)]
        x = conv(e,geom,nmax)
        su = [su[i]+(q-1)*shift(x)[i] for i in range(nmax+1)]
        e = [(q-j)*v for v in shift(x)]
    a = [(q-1)*v for v in shift(e)]
    su0 = [1]+[q*(v-1 if i == 0 else v)//(q-1) for i,v in enumerate(su)][1:]
    a0 = [q*v//(q-1) for v in a]
    return a,su,a0,su0


def conv(a, b, nmax):
    c = [0] * (nmax + 1)
    for i, x in enumerate(a):
        if x:
            for j in range(nmax + 1-i):
                c[i+j] += x*b[j]
    return c


def predicted(q, nmax):
    a0, s0 = first_arch_counts(q, nmax, None)
    a, s = first_arch_counts(q, nmax, 0)
    an, sn, an0, sn0 = analytic_counts(q,nmax)
    assert a == an and s == sn and a0 == an0 and s0 == sn0, (q,a,an,s,sn,a0,an0,s0,sn0)
    future = [s]
    for k in range(1, nmax//q + 1):
        future.append(conv(a, future[-1], nmax))
    table = [[0] * (nmax//q + 1) for _ in range(nmax+1)]
    for n in range(nmax+1):
        table[n][0] = s0[n]
    for k in range(1, nmax//q + 1):
        v = conv(a0, future[k-1], nmax)
        for n in range(nmax+1):
            table[n][k] = v[n]
    return table


def ternary_recurrence(nmax):
    vals = [[0]*(nmax//3+1) for _ in range(nmax+1)]
    for n in range(nmax+1):
        for k in range(nmax//3+1):
            rhs = {(0,0):1,(1,0):2,(2,0):3,(3,1):2}.get((n,k),0)
            vals[n][k] = rhs + (vals[n-1][k] if n>=1 else 0) + (4*vals[n-3][k-1] if n>=3 and k>=1 else 0)
    return vals


def ternary_tail(n, k):
    if k == 0:
        return 1 if n == 0 else 3*2**(n-1)
    if n < 3*k:
        return 0
    d = n-2*k
    prob = Fraction(sum(comb(d,j) for j in range(k,d+1)),2**d)
    return 3*2**(n-1)*prob


def proper_words(q,n):
    if n == 0:
        yield ()
        return
    def gen(prefix):
        if len(prefix) == n:
            yield tuple(prefix)
            return
        for c in range(q):
            if not prefix or prefix[-1] != c:
                prefix.append(c)
                yield from gen(prefix)
                prefix.pop()
    yield from gen([])


def main():
    limits = {2:12,3:18,4:10,5:8,6:7}
    host_tests = 0
    literal_tests = 0
    comparisons = 0
    for q, nmax in limits.items():
        model = predicted(q,nmax)
        exact = defaultdict(int)
        for n in range(nmax+1):
            if n == 0:
                exact[(0,0)] = 1
                continue
            for tup in proper_words(q,n):
                host_tests += 1
                k = arch_index(tup,q)
                exact[(n,k)] += 1
                if q <= 4 and n <= 8:
                    # Independently verify the universal and first absent levels.
                    for m in (k,k+1):
                        all_exist = True
                        for pattern in product(range(q),repeat=m):
                            literal_tests += 1
                            if not is_subsequence(pattern,tup):
                                all_exist = False
                                break
                        assert all_exist == (m == k), (q,n,tup,m)
            for k in range(n//q+1):
                assert exact[(n,k)] == model[n][k], (q,n,k,exact[(n,k)],model[n][k])
                comparisons += 1
            assert sum(model[n]) == q*(q-1)**(n-1), (q,n)
            if n == q*(n//q) and n>0:
                k=n//q
                assert model[n][k] == factorial(q)*((q-1)*factorial(q-1))**(k-1), (q,n)
        if q == 3:
            recurrence = ternary_recurrence(nmax)
            for n in range(nmax+1):
                assert recurrence[n] == model[n], (n,model[n],recurrence[n])
                for k in range(n//3+1):
                    tail = sum(model[n][k:])
                    assert tail == ternary_tail(n,k), (n,k,tail,ternary_tail(n,k))
                    comparisons += 1
    print('VERIFY_OK proper_hosts=%d literal_pattern_checks=%d parameter_coefficients=%d alphabets=2..6 nmax=%s ternary_binomial_tails=TRUE'%(host_tests,literal_tests,comparisons,limits))


if __name__ == '__main__':
    main()
