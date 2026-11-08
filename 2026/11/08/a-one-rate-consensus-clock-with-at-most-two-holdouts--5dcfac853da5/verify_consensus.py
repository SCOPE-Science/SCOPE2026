#!/usr/bin/env python3
"""Exact, standalone finite-state checks for complete-hypergraph proportional copying.
All arithmetic uses fractions. No randomness, third-party packages, or external files.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def expected_survival(n, missing, x, t):
    assert 0 < x < n and t >= 1
    if missing == 0:
        return F(0)
    if missing == 1:
        return F(2*x*(n-x), n*(n-1))*F(2,n)**(t-1)
    if missing == 2:
        return F(3*x*(n-x), n*(n-1))*F(4*n-6,n*(n-1))**(t-1)
    raise ValueError


def mask_successors(n, k, mask):
    """Full labeled-state one-step law, independently of occupancy formulas."""
    denom = comb(n,k)*k
    counts = {}
    for group in combinations(range(n),k):
        bits = sum(1 << i for i in group)
        for leader in group:
            target = (mask | bits) if (mask >> leader)&1 else (mask & ~bits)
            counts[target] = counts.get(target,0)+1
    assert sum(counts.values()) == denom
    return {target:F(cnt,denom) for target,cnt in counts.items()}


def labeled_census():
    examined = 0
    for n in range(4,10):
        for missing in (0,1,2):
            k=n-missing
            num=1<<n
            moves=[mask_successors(n,k,mask) for mask in range(num)]
            f=[F(0) if mask in (0,num-1) else F(1) for mask in range(num)]
            for t in range(1,6):
                f=[sum((prob*f[dest] for dest,prob in moves[mask].items()),F(0)) for mask in range(num)]
                for mask in range(1,num-1):
                    x=mask.bit_count()
                    assert f[mask] == expected_survival(n,missing,x,t),(n,missing,t,mask,f[mask])
                    examined+=1
        print('labeled exact survivors: n=%d complete' % n)
    return examined


def count_kernel(n,k):
    p=[[F(0) for _ in range(n+1)] for _ in range(n+1)]
    for x in range(n+1):
        for j in range(max(0,k-(n-x)),min(k,x)+1):
            weight=F(comb(x,j)*comb(n-x,k-j),comb(n,k))
            p[x][x-j]+=weight*F(k-j,k)
            p[x][x-j+k]+=weight*F(j,k)
        assert sum(p[x],F(0))==1
    return p


def mean_from_count_kernel(p):
    # Fraction-exact Gaussian elimination for mean first-hitting times.
    n=len(p)-1
    matrix=[[F(int(i==j))-p[i+1][j+1] for j in range(n-1)] + [F(1)] for i in range(n-1)]
    for col in range(n-1):
        pivot=next(i for i in range(col,n-1) if matrix[i][col])
        matrix[col],matrix[pivot]=matrix[pivot],matrix[col]
        z=matrix[col][col]
        matrix[col]=[v/z for v in matrix[col]]
        for row in range(n-1):
            if row==col: continue
            a=matrix[row][col]
            matrix[row]=[matrix[row][j]-a*matrix[col][j] for j in range(n)]
    return [row[-1] for row in matrix]


def count_census():
    examined=0
    for n in range(4,14):
        for missing in (0,1,2):
            p=count_kernel(n,n-missing)
            means=mean_from_count_kernel(p)
            for x in range(1,n):
                mean = F(1) if missing==0 else F(1)+(
                    F(2*x*(n-x),(n-1)*(n-2)) if missing==1 else
                    F(3*x*(n-x),(n-2)*(n-3)))
                assert means[x-1]==mean,(n,missing,x,means[x-1],mean)
                f=[F(int(y==x)) for y in range(n+1)]
                for t in range(1,8):
                    f=[sum(f[z]*p[z][y] for z in range(n+1)) for y in range(n+1)]
                    s=1-f[0]-f[n]
                    assert s==expected_survival(n,missing,x,t),(n,missing,x,t,s)
                    examined+=1
    return examined


def sharpness():
    n,k,x=6,3,1
    p=count_kernel(n,k)
    d=[F(int(y==x)) for y in range(n+1)]
    s=[]
    for t in range(1,4):
        d=[sum(d[z]*p[z][y] for z in range(n+1)) for y in range(n+1)]
        s.append(1-d[0]-d[n])
    assert s==[F(2,3),F(1,2),F(59,150)],s
    assert s[1]*s[1]!=s[0]*s[2]
    return s


if __name__=='__main__':
    l=labeled_census()
    c=count_census()
    s=sharpness()
    print('PASS: %d labeled survival checks; %d independent count-chain survival checks; exact means n=4..13 and all x' %(l,c))
    print('n=6, group=3, x=1 non-geometric survivors:',', '.join(map(str,s)))
