#!/usr/bin/env python3
"""Exhaustive ASM/DSASM/OSASM enumeration to order 5.

The scientific check is reciprocal symmetry up to a monomial shift:
P(t) = t^m P(1/t).  For finite nonzero support [a,b], m is forced to a+b.
The order-3 odd OSASM row is reciprocal with shift 4; the order-5 row is not
reciprocal under any shift (the only possible shift is 6).
"""
import itertools
import math
from collections import Counter


def valid_rows(n):
    out=[]
    for row in itertools.product([-1,0,1], repeat=n):
        if sum(row)!=1:
            continue
        nz=[x for x in row if x]
        if not nz or nz[0]!=1 or nz[-1]!=1:
            continue
        if any(a==b for a,b in zip(nz,nz[1:])):
            continue
        out.append(row)
    return out


def gen_asms(n):
    rows=valid_rows(n)
    col=[0]*n
    last=[0]*n
    mat=[]
    out=[]
    def bt(r):
        if r==n:
            if all(x==1 for x in col):
                # The pruning already enforces column alternation; keep a final check.
                for j in range(n):
                    nz=[mat[i][j] for i in range(n) if mat[i][j]]
                    if sum(nz)!=1 or nz[0]!=1 or nz[-1]!=1 or any(a==b for a,b in zip(nz,nz[1:])):
                        return
                out.append(tuple(mat))
            return
        for row in rows:
            if r in (0,n-1) and sum(x!=0 for x in row)!=1:
                continue
            ok=True
            for j,x in enumerate(row):
                if col[j]+x not in (0,1):
                    ok=False; break
                if x and last[j] and x==last[j]:
                    ok=False; break
                if x and not last[j] and x!=1:
                    ok=False; break
            if not ok:
                continue
            old=last[:]
            mat.append(row)
            for j,x in enumerate(row):
                col[j]+=x
                if x: last[j]=x
            bt(r+1)
            mat.pop()
            for j,x in enumerate(row):
                col[j]-=x
            last[:]=old
    bt(0)
    return out


def is_dsasm(M):
    n=len(M)
    return all(M[i][j]==M[j][i] for i in range(n) for j in range(n))


def is_osasm(M):
    n=len(M)
    nzdiag=sum(M[i][i]!=0 for i in range(n))
    return nzdiag==(0 if n%2==0 else 1)


def kumari_odd_product(n):
    f=math.factorial
    num=(2**(n-1))*f(3*n+2)
    den=f(2*n+1)
    for i in range(1,n+1):
        num*=f(6*i-2)
        den*=f(2*n+2*i+1)
    assert num%den==0
    return num//den


def reciprocal_shift(poly):
    """Return the unique reciprocal shift if it works, else None."""
    a=min(poly); b=max(poly); m=a+b
    lo=min(a,m-b); hi=max(b,m-a)
    if all(poly.get(k,0)==poly.get(m-k,0) for k in range(lo,hi+1)):
        return m
    return None


def main():
    exp_asm={1:1,2:2,3:7,4:42,5:429}
    exp_ds={1:1,2:2,3:5,4:16,5:67}
    exp_os={1:1,2:1,3:4,4:3,5:32}
    dist={}
    for n in range(1,6):
        A=gen_asms(n)
        assert len(A)==exp_asm[n]
        ds=[M for M in A if is_dsasm(M)]
        assert len(ds)==exp_ds[n]
        os=[M for M in ds if is_osasm(M)]
        assert len(os)==exp_os[n]
        dist[n]=dict(sorted(Counter(M[0].index(1)+1 for M in os).items()))
        print(f"order {n}: ASM={len(A)} DSASM={len(ds)} OSASM={len(os)} T={dist[n]}")

    assert dist[1]=={1:1}
    assert dist[2]=={2:1}
    assert dist[3]=={1:1,2:2,3:1}
    assert dist[4]=={2:1,3:1,4:1}
    assert dist[5]=={1:3,2:7,3:9,4:9,5:4}
    assert sum(dist[3].values())==kumari_odd_product(1)==4
    assert sum(dist[5].values())==kumari_odd_product(2)==32

    assert reciprocal_shift(dist[3])==4
    assert reciprocal_shift(dist[5]) is None
    # Since support is [1,5], shift 6 is forced; these are direct failures.
    assert dist[5][1]==3 and dist[5][5]==4
    assert dist[5][2]==7 and dist[5][4]==9
    # Explicitly check a wider shift window too.
    ok_shifts=[]
    for m in range(0,11):
        lo=min(min(dist[5]),m-max(dist[5])); hi=max(max(dist[5]),m-min(dist[5]))
        if all(dist[5].get(k,0)==dist[5].get(m-k,0) for k in range(lo,hi+1)):
            ok_shifts.append(m)
    assert ok_shifts==[]
    print("order-3 reciprocal shift: 4")
    print("order-5 reciprocal shifts: none; forced shift 6 fails c1=3 vs c5=4")
    print("MINIMAL_ODD_COUNTEREXAMPLE n=2 (order 5)")
    print("VERIFY_OK")

if __name__=='__main__':
    main()
