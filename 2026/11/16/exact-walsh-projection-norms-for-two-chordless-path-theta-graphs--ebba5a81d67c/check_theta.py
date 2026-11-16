#!/usr/bin/env python3
"""Independent exhaustive Walsh and spanning-tree check for two-path-plus-edge theta graphs."""
from itertools import product, combinations
from math import comb
from fractions import Fraction

def formula(a,b):
    za=Fraction(comb(a,a//2),2**a) if a%2==0 else Fraction(0)
    zb=Fraction(comb(b,b//2),2**b) if b%2==0 else Fraction(0)
    pa=Fraction(comb(a,(a-1)//2),2**a) if a%2 else Fraction(0)
    pb=Fraction(comb(b,(b-1)//2),2**b) if b%2 else Fraction(0)
    ua=a*za+(a+1)*pa
    ub=b*zb+(b+1)*pb
    return ua*ub+za*ub+zb*ua+pa*(1-zb)+pb*(1-za)-2*pa*pb

def tree_edges(a,b):
    # vertices 0,1 terminals; a path through vertices 2,...a; b path through vertices a+1,...a+b-1
    path_a=[0]+list(range(2,a+1))+[1]
    path_b=[0]+list(range(a+1,a+b))+[1]
    return list(zip(path_a[:-1],path_a[1:]))+list(zip(path_b[:-1],path_b[1:]))+[(0,1)]

def actual_tree_masks(a,b):
    edges=tree_edges(a,b); m=len(edges); N=a+b
    result=[]
    for keep in combinations(range(m),N-1):
        par=list(range(N))
        def find(x):
            while par[x]!=x:
                x=par[x]
            return x
        for k in keep:
            u,v=edges[k]; par[find(u)]=find(v)
        if len({find(x) for x in range(N)})==1:
            result.append(sum(1<<i for i in keep))
    return result

def fwht(A):
    n=len(A);h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x=A[j];y=A[j+h];A[j]=x+y;A[j+h]=x-y
        h*=2
    return A

def verify(a,b):
    edges=a+b+1
    Ts=actual_tree_masks(a,b)
    assert len(Ts)==a*b+a+b,(a,b,len(Ts))
    arr=[0]*(1<<edges)
    for mask in Ts: arr[mask]=1
    fwht(arr)
    f=sum(map(abs,arr)); ex=Fraction(f,1<<edges)
    model=formula(a,b)
    assert ex==model,(a,b,ex,model)
    zero_count=0 if a%2 or b%2 else 2*(comb(a,a//2)*comb(b,b//2)+comb(a,a//2-1)*comb(b,b//2-1))
    assert len([v for v in arr if v==0])==zero_count,(a,b,zero_count)
    # Unnormalized Walsh Parseval and the zero-frequency tree coefficient.
    assert sum(v*v for v in arr)==(1<<edges)*len(Ts)
    assert arr[0]==len(Ts)
    # Independently compute W for every sign vector from path sums
    for signbits,w in enumerate(arr):
        x=sum(-1 if (signbits>>i)&1 else 1 for i in range(a))
        y=sum(-1 if (signbits>>(a+i))&1 else 1 for i in range(b))
        z=-1 if (signbits>>(a+b))&1 else 1
        phase=(-1)**(signbits.bit_count())
        assert w==phase*(x*y+z*(x+y)),(a,b,signbits,w,phase*(x*y+z*(x+y)))
    return (a,b,len(Ts),str(ex),len([v for v in arr if v!=0]))

if __name__=='__main__':
    tested=[]
    for a in range(2,7):
        for b in range(2,7):
            if a+b>11:continue
            tested.append(verify(a,b))
    for x in tested: print(*x)
    print('THETA_ALL_WALSH_CERTIFICATES_PASS',len(tested))
