#!/usr/bin/env python3
"""Finite reproducibility checks of cyclic single-deletion laws for de Bruijn words."""
from collections import Counter
from itertools import product


def debruijn_fkm(q, n):
    a = [0] * (q * n + 1)
    out = []
    def rec(t, p):
        if t > n:
            if n % p == 0:
                out.extend(a[1:p+1])
            return
        a[t] = a[t-p]
        rec(t+1, p)
        for j in range(a[t-p]+1, q):
            a[t] = j
            rec(t+1, t)
    rec(1, 1)
    return tuple(out)


def rotate_min(s):
    return min(s[i:] + s[:i] for i in range(len(s)))


def cyclic_runs(s):
    n=len(s)
    if len(set(s))==1:
        return [(s[0], n)]
    starts=[i for i in range(n) if s[i]!=s[(i-1)%n]]
    runs=[]
    for j,i in enumerate(starts):
        next_i=starts[(j+1)%len(starts)]
        runs.append((s[i], (next_i-i)%n or n))
    return runs


def expected(q,n):
    expect=Counter()
    for ell in range(1,n-1):
        expect[ell] = q*(q-1)**2 * q**(n-ell-2)
    expect[n-1] = q*(q-2)
    expect[n] = q
    return +expect


def check(seq,q,n):
    N=q**n
    assert len(seq)==N
    all_words={tuple(seq[(i+j)%N] for j in range(n)) for i in range(N)}
    assert len(all_words)==N
    assert all_words==set(product(range(q),repeat=n))
    exp=expected(q,n)
    runs=cyclic_runs(seq)
    assert Counter(length for letter,length in runs)==exp, (q,n,'runs')
    shadows=Counter()
    for i in range(N):
        deleted=rotate_min(seq[:i]+seq[i+1:])
        shadows[deleted]+=1
    assert len(shadows)==sum(exp.values()), (q,n,'shadow',len(shadows),sum(exp.values()))
    assert Counter(shadows.values())==exp, (q,n,'multiplicities')
    return len(shadows)


def binary_by_euler_choices(n):
    """Exhaustively vary both outgoing-arc orders at all overlap states."""
    m=1<<(n-1)
    root=0
    seen=set()
    for mask in range(1<<m):
        cursor=[0]*m
        output=[]
        def visit(v):
            while cursor[v]<2:
                t=cursor[v]
                cursor[v]+=1
                bit=t^((mask>>v)&1)
                visit(((v<<1)&(m-1))|bit)
                output.append(bit)
        visit(root)
        assert len(output)==2*m
        seq=tuple(reversed(output))
        doubled=seq+seq[:n-1]
        root_idx=next(i for i in range(len(seq)) if doubled[i:i+n]==(0,)*n)
        key=seq[root_idx:]+seq[:root_idx]
        if key not in seen:
            seen.add(key)
            yield key


def main():
    total=0
    for q,nmax in [(2,8),(3,5),(4,4),(5,3)]:
        for n in range(2,nmax+1):
            result=check(debruijn_fkm(q,n),q,n)
            total+=1
            print('FKM_PASS',q,n,result)
    for n in range(2,6):
        count=0
        for seq in binary_by_euler_choices(n):
            check(seq,2,n)
            count+=1
        expect_count=2**(2**(n-1)-n)
        assert count==expect_count,(n,count,expect_count)
        print('ALL_BINARY_PASS',n,count)
    print('VERIFY_OK','FKM_parameter_pairs',total,'binary_all_orders_2_to_5')

if __name__=='__main__':main()
