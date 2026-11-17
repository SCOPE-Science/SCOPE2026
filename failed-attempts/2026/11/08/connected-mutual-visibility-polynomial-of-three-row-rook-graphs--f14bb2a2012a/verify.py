#!/usr/bin/env python3
"""Independent finite verification of connected mutual-visibility enumeration on K3 square Kn."""
from collections import Counter, deque
from math import comb

def predicted(n):
    c=Counter()
    # One occupied row, arbitrary nonempty chosen columns.
    for j in range(1,n+1): c[j]+=3*comb(n,j)
    # Exactly one 2-row column, no 3-row column.
    for j in range(n): c[j+2]+=3*n*comb(n-1,j)*2**j
    # Exactly one full 3-row column, all remaining columns are empty or singles.
    for j in range(n): c[j+3]+=n*comb(n-1,j)*3**j
    # Exactly two different 2-row column types, each used once.
    for j in range(max(0,n-1)):
        c[j+4]+=3*n*(n-1)*comb(n-2,j)*3**j
    # One column of each 2-row type.
    for j in range(max(0,n-2)):
        c[j+6]+=n*(n-1)*(n-2)*comb(n-3,j)*3**j
    return {k:v for k,v in c.items() if v}

def brute(n):
    vertices=[(i,j) for i in range(3) for j in range(n)]
    nbr=[set() for _ in vertices]
    for a,(i,j) in enumerate(vertices):
        for b,(k,l) in enumerate(vertices):
            if a!=b and (i==k or j==l): nbr[a].add(b)
    cnt=Counter(); maxval=0
    for mask in range(1,1<<(3*n)):
        chosen=[v for v in range(3*n) if mask>>v&1]
        seen={chosen[0]}; stack=[chosen[0]]
        while stack:
            a=stack.pop()
            for b in nbr[a]:
                if mask>>b&1 and b not in seen:seen.add(b);stack.append(b)
        if len(seen)!=len(chosen):continue
        feasible=True
        for ia,a in enumerate(chosen):
            i,j=vertices[a]
            for b in chosen[ia+1:]:
                k,l=vertices[b]
                if i!=k and j!=l:
                    if (mask>>(i*n+l)&1) and (mask>>(k*n+j)&1):
                        feasible=False;break
            if not feasible:break
        if feasible:cnt[len(chosen)]+=1;maxval=max(maxval,len(chosen))
    return dict(cnt),maxval

for n in range(1,6):
    ex,maximum=brute(n)
    pr=predicted(n)
    assert ex==pr,(n,ex,pr)
    assert maximum== (n+3 if n>=3 else n+2 if n==2 else 3)
    print('EXHAUSTIVE_OK',n,'coefficients',dict(sorted(ex.items())),'max',maximum)
for n in range(3,31):
    c=predicted(n)
    assert max(c)==n+3
    assert c[n+3]==n*(n-1)*(n-2)*3**(n-3)
print('MAXIMUM_COEFFICIENT_OK 3..30')
print('VERIFY_OK')
