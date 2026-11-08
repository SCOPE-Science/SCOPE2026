#!/usr/bin/env python3
"""Exact finite certificate for bivariate Ising polynomials on two 16-vertex graphs.

No external dependencies. Two independently encoded exhaustive enumerations are
compared; the claimed factorization is checked coefficient by coefficient.
"""
from collections import Counter
from itertools import combinations, product
from math import comb

N = 16

def edges(graph):
    result = []
    steps = {(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
    for i in range(N):
        x, y = divmod(i, 4)
        for j in range(i+1, N):
            u, v = divmod(j, 4)
            linked = (x == u or y == v) if graph == 'rook' else ((u-x)%4, (v-y)%4) in steps
            if linked: result.append((i,j))
    assert len(result) == 48
    return result

def enumerate_adjacency(graph):
    nbr = [0]*N
    for i,j in edges(graph):
        nbr[i] |= 1<<j
        nbr[j] |= 1<<i
    hist = Counter()
    inside = [0]*(1<<N)
    for mask in range(1<<N):
        if mask:
            low = mask & -mask
            i = low.bit_length()-1
            remainder = mask ^ low
            inside[mask] = inside[remainder]+(nbr[i]&remainder).bit_count()
        k=mask.bit_count()
        cut=6*k-2*inside[mask]
        hist[k,cut]+=1
    return hist

def pop4(mask): return mask.bit_count()
def bit(mask, j): return (mask >> (j%4))&1

def enumerate_rows(graph):
    hist = Counter()
    for a,b,c,d in product(range(16),repeat=4):
        rows=(a,b,c,d)
        k=sum(pop4(t) for t in rows)
        if graph == 'rook':
            cut=sum(pop4(t)*(4-pop4(t)) for t in rows)
            for y in range(4):
                count=sum(bit(t,y) for t in rows)
                cut+=count*(4-count)
        else:
            cut=0
            for r in range(4):
                t,u=rows[r],rows[(r+1)%4]
                for y in range(4):
                    cut += bit(t,y)^bit(t,y+1)
                    cut += bit(t,y)^bit(u,y)
                    cut += bit(t,y)^bit(u,y+1)
        hist[k,cut]+=1
    return hist

def coefficient_difference():
    out={}
    for name in ('rook','shrikhande'):
        a=enumerate_adjacency(name)
        b=enumerate_rows(name)
        assert a==b, (name,'enumeration mismatch')
        assert sum(a.values())==65536
        assert all(sum(v for (k,c),v in a.items() if k==r)==comb(16,r) for r in range(17))
        out[name]=a
    diff=Counter(out['rook'])
    diff.subtract(out['shrikhande'])
    diff=Counter({key:v for key,v in diff.items() if v})
    expected=Counter()
    for k, p, multiplier in [(4,12,8),(6,18,-32),(8,20,48),(10,18,-32),(12,12,8)]:
        for j in range(7):
            expected[k,p+2*j]+=multiplier*comb(6,j)*(-1)**j
    assert diff==expected, ('factor coefficient mismatch',diff-expected,expected-diff)
    # A second, zero-field check using the recognized factor at z=1:
    zero_field=Counter()
    for (k,c),v in diff.items():zero_field[c]+=v
    zero_field={c:v for c,v in zero_field.items() if v}
    predicted={}
    for j in range(9):
        # 16 q^12 (q^2-1)^8 (3q^4+2q^2+1)
        for degree,coeff in [(0,1),(2,2),(4,3)]:
            c=12+2*j+degree
            predicted[c]=predicted.get(c,0)+16*comb(8,j)*(-1)**(8-j)*coeff
    predicted={c:v for c,v in predicted.items() if v}
    assert zero_field==predicted
    return out, diff

def table(out):
    for name,hist in out.items():
        d=[]
        for k in range(9):
            maxcut=max(c for (kk,c) in hist if kk==k)
            degeneracy=hist[k,maxcut]
            d.append((k,maxcut,degeneracy))
        print(name,'max-cut-by-k',d)

if __name__=='__main__':
    out,diff=coefficient_difference()
    print('INDEPENDENT_ENUMERATIONS_OK',sum(out['rook'].values()),sum(out['shrikhande'].values()))
    print('FACTORIZATION_OK',len(diff),'nonzero (k,cut) coefficients')
    table(out)
    print('VERIFIED')
