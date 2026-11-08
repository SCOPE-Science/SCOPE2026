"""Finite tests for the minimum-width formula of polymatroid polytopes.

Only finite computations: no assertion of historical priority or formal proof.
Requires Python 3 standard library; run: python verify.py
"""
from itertools import combinations
from math import sqrt, isclose
from random import Random

R = Random(19847)


def make_f_from_coverage(n):
    universe = range(R.randint(2, 10))
    subsets = [set(v for v in universe if R.randrange(3) == 0) for _ in range(n)]
    for i in range(n):
        subsets[i].add(i % len(universe))
    return {mask:len(set().union(*(subsets[i] for i in range(n) if (mask >> i)&1))) for mask in range(1<<n)}


def rank_gf2(xs, mask):
    basis = {}
    for i, v in enumerate(xs):
        if not ((mask >> i) & 1): continue
        while v:
            pivot = v.bit_length()-1
            if pivot not in basis:
                basis[pivot] = v
                break
            v ^= basis[pivot]
    return len(basis)


def make_f_gf2(n):
    dim=R.randint(2, 5)
    xs=[R.randrange(1, 2**dim) for _ in range(n)]
    return {mask:rank_gf2(xs,mask) for mask in range(1<<n)}


def make_f_partition(n):
    colors = [R.randrange(1, 5) for _ in range(n)]
    caps = {c:R.randrange(1, 4) for c in set(colors)}
    return {mask:sum(min(caps[c],sum(1 for i in range(n) if ((mask>>i)&1) and colors[i] == c)) for c in caps) for mask in range(1<<n)}


def support(w, f):
    vals = sorted((max(0.0,v), i) for i,v in enumerate(w))
    vals.reverse()
    acc=0.0
    last=0
    for j,(v,i) in enumerate(vals):
        last |= 1<<i
        nextval= vals[j+1][0] if j+1<len(vals) else 0.0
        acc += (v-nextval)*f[last]
    return acc


def width(u, s, f):
    su=[v*t for v,t in zip(s,u)]
    return support(su,f)+support([-z for z in su],f)


def case(n, f, s):
    ratios={mask:f[mask]/sqrt(sum(s[i]**-2 for i in range(n) if (mask>>i)&1)) for mask in range(1,1<<n)}
    target=min(ratios.values())
    winners=[]
    for mask,val in ratios.items():
        if isclose(val,target,rel_tol=1e-12, abs_tol=1e-12):
            z=sqrt(sum(s[i]**-2 for i in range(n) if (mask>>i)&1))
            u=[(1/s[i])/z if (mask>>i)&1 else 0.0 for i in range(n)]
            assert isclose(width(u,s,f),target,rel_tol=1e-11,abs_tol=1e-11)
            assert isclose(width([-v for v in u],s,f),target,rel_tol=1e-11,abs_tol=1e-11)
            winners.append(mask)
    for t in range(120):
        u=[R.gauss(0,1) for _ in range(n)]
        norm=sqrt(sum(x*x for x in u))
        u=[x/norm for x in u]
        assert width(u,s,f) >= target-1e-10, (n,target,width(u,s,f))
    return len(winners)


if __name__=='__main__':
    profiles=0
    winners=0
    for n in range(2,8):
        for maker in (make_f_from_coverage,make_f_gf2,make_f_partition):
            for trial in range(7):
                f=maker(n)
                # Exact submodularity check in all pairs of subsets.
                for a in range(1<<n):
                    for b in range(1<<n):
                        assert f[a]+f[b]>=f[a|b]+f[a&b]
                s=[R.choice((0.5,1.0,1.5,2.0,3.0)) for _ in range(n)]
                winners+=case(n,f,s)
                profiles+=1
    for r in range(1,6):
        for n in range(r,30):
            f={mask:min(mask.bit_count(),r) for mask in range(1<<min(n,12))} if n<=12 else None
            expected=min(1.0,r/sqrt(n))
            if f is not None:
                result=min(f[mask]/sqrt(mask.bit_count()) for mask in range(1,1<<n))
                assert isclose(expected,result,rel_tol=1e-12)
    print('POLYMATROID_WIDTH_FINITE_CHECKS_PASSED', 'profiles=',profiles,'critical_sets=',winners,'random_normals=',profiles*120)
