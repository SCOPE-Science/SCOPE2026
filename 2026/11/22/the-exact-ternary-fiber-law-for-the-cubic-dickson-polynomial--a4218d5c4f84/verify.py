#!/usr/bin/env python3
"""Exact finite checks for the cubic Dickson ternary fiber theorem.
Run with Python 3.10+, standard library only. These computations corroborate,
but do not replace, the theorem's p-adic proof.
"""
from collections import Counter
from math import floor


def sqrt_count(t, r):
    if r == 0:
        return 1
    t %= 3**r
    if t == 0:
        return 3 ** (r // 2)
    v = 0
    while t % 3 == 0:
        t //= 3
        v += 1
    if v % 2 or t % 3 != 1:
        return 0
    return 2 * 3 ** (v // 2)


def critical_count(t, m):
    mod = 3**m
    t %= mod
    if m <= 2:
        return (3 ** (m - 1)) if t == 0 else 0
    if t % 9:
        return 0
    return 3 * sqrt_count(t // 9, m-2)


def predicted_fiber(y, k):
    n = 3**k
    y %= n
    if k == 1:
        return 1
    if k == 2:
        return 3 if y in (0, 2, 7) else 0
    if y % 9 == 0:
        return 3
    if k == 3:
        return 9 if y in (2, n-2) else 0
    for sign in (1, -1):
        # Output is sign *(-2+27*t), where sign=1 or -1.
        if (sign*y+2) % 27 == 0:
            m = k-3
            t = ((sign*y+2)//27) % (3**m)
            return 9 * (int(t % 3 in (0, 2)) + critical_count(t,m))
    return 0


def predicted_max(k):
    if k==1: return 1
    if k==2: return 3
    if k==3: return 9
    if k==4: return 18
    if k % 2: return 9+3**((k+1)//2)
    return 9+2*3**(k//2)


def max_targets(k):
    n=3**k
    if k==1: return set(range(n))
    if k==2: return {0,2,7}
    if k<=5 or k%2: return {2,n-2}
    v=2-3**(k-1)
    return {v%n,(-v)%n}


def root_lift_target(y,k):
    roots=[0]
    mod=1
    for j in range(1,k+1):
        next_mod=3*mod
        roots=[r+d*mod for r in roots for d in range(3)
               if ((r+d*mod)**3-3*(r+d*mod)-y)%next_mod==0]
        mod=next_mod
    return len(roots)


def main():
    total_checks=0
    for k in range(1,10):
        modulus=3**k
        values=Counter((x*x*x-3*x)%modulus for x in range(modulus))
        assert sum(values.values())==modulus
        assert len(values)==(3 if k<=2 else 5 if k==3 else 13*3**(k-4))
        assert max(values.values())==predicted_max(k)
        actual_max={y for y,n in values.items() if n==predicted_max(k)}
        assert actual_max==max_targets(k), (k,actual_max,max_targets(k))
        for y in range(modulus):
            predicted=predicted_fiber(y,k)
            assert predicted==values[y],(k,y,predicted,values[y])
            total_checks+=1
        print(f'k={k}, modulus={modulus}, image={len(values)}, peak={max(values.values())}, max_targets={sorted(actual_max)}')
    # Independent pointwise lifting for large precision; no full enumeration claimed.
    for k in range(10,15):
        mod=3**k
        samples={0,2,mod-2, 2-3**(k-1), -2+3**(k-1), 9, 27, 81,
                 mod//3, mod//2, 2+27, -2+27, -2+27*9,
                 2-27*9, 2-27*3**(k-5)}
        # Reproducible pseudo-random but fixed probe values, no external dependency.
        z=135791113
        for _ in range(35):
            z=(1664525*z+1013904223)%(2**32)
            samples.add(z%mod)
        for y in samples:
            predicted=predicted_fiber(y,k)
            observed=root_lift_target(y,k)
            assert observed==predicted,(k,y,predicted,observed)
            total_checks+=1
        assert predicted_fiber(2,k)==predicted_max(k) if k%2 else True
    print(f'VERIFY_OK: {total_checks} independent target checks, exact all targets through 3^9 plus selected root-lifts through 3^14')

if __name__=='__main__': main()
