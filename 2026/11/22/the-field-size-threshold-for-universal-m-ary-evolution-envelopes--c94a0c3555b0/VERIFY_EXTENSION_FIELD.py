#!/usr/bin/env python3
"""F_4 arithmetic check of the sharp degree threshold in symmetric tensor spans."""
from itertools import product
from math import comb

def mul(a,b):
    c=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1):c ^= 1<<(i+j)
    if c&8:c ^= 0b1110 # x^3 = x^2+x, since x^2=x+1
    if c&4:c ^= 0b111 # x^2=x+1
    return c

def power(a,n):
    c=1
    for _ in range(n):c=mul(c,a)
    return c

def multi(n,d):
    if n==1:yield (d,)
    else:
        for j in range(d+1):
            for b in multi(n-1,d-j):yield (j,)+b

def rank(M):
    a=[r[:] for r in M];h=len(a);w=len(a[0]);k=0
    for j in range(w):
        piv=next((i for i in range(k,h) if a[i][j]),None)
        if piv is None:continue
        a[k],a[piv]=a[piv],a[k]
        inv=next(z for z in (1,2,3) if mul(z,a[k][j])==1)
        a[k]=[mul(x,inv) for x in a[k]]
        for i in range(h):
            if i==k:continue
            f=a[i][j]
            if f:a[i]=[x^mul(f,y) for x,y in zip(a[i],a[k])]
        k+=1
        if k==h:break
    return k

if __name__=='__main__':
    assert all(power(a,4)==a for a in range(4))
    for n in (2,3):
        for d in (2,3,4,5,6):
            bs=list(multi(n,d));points=list(product(range(4),repeat=n))
            M=[]
            for b in bs:
                row=[]
                for a in points:
                    v=1
                    for x,e in zip(a,b):v=mul(v,power(x,e))
                    row.append(v)
                M.append(row)
            r=rank(M)
            assert (r==len(bs))==(d<=4),(n,d,r,len(bs))
            if d>=5:
                for a in points:
                    u=mul(power(a[0],d-1),a[1])
                    v=mul(power(a[0],d-4),power(a[1],4))
                    assert u==v
            print('F4_CHECK',n,d,r,len(bs))
    print('EXTENSION_VERIFY_OK')
