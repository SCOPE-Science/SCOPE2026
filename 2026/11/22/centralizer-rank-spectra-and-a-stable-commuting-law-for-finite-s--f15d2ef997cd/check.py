#!/usr/bin/env python3
"""Finite-prime-field consistency checks for a Schrödinger Lie bracket centralizer theorem."""
from itertools import product
from collections import Counter

def bracket(a,b,n,p):
    h,e,f=a[:3]; H,E,F=b[:3]
    out=[(e*F-f*E)%p, (2*(h*E-e*H))%p, (2*(f*H-h*F))%p]
    z=0
    for i in range(n):
        x,y=a[3+2*i:5+2*i]
        X,Y=b[3+2*i:5+2*i]
        out.extend(((h*X+e*Y-H*x-E*y)%p,(f*X-h*Y-F*x+H*y)%p))
        z+=x*Y-y*X
    return out+[(z%p)]

def rank_mod(matrix,p):
    M=[r[:] for r in matrix]; m=len(M); n=len(M[0]); row=0
    for col in range(n):
        pivot=next((j for j in range(row,m) if M[j][col]%p),None)
        if pivot is None: continue
        M[row],M[pivot]=M[pivot],M[row]
        mult=pow(M[row][col],-1,p)
        M[row]=[(v*mult)%p for v in M[row]]
        for i in range(row+1,m):
            if M[i][col]:
                t=M[i][col]
                M[i]=[(u-t*v)%p for u,v in zip(M[i],M[row])]
        row+=1
        if row==m:break
    return row

def expected(n,q):
    return Counter({
        2*n+4:q,
        2*n+1:q*(q+1)*(q**n-1),
        2*n:q*(q**n-1)*(q**n-q),
        n+2:q*(q*q-1)*q**n,
        n+1:q*(q*q-1)*(q**(2*n)-q**n),
        2:q*(q**3-q*q)*q**(2*n),
    })

def check(n,p):
    d=2*n+4; basis=[[int(j==i) for j in range(d)] for i in range(d)]
    actual=Counter()
    for a in product(range(p),repeat=d):
        cols=[bracket(a,b,n,p) for b in basis]
        mat=[list(row) for row in zip(*cols)]
        cdim=d-rank_mod(mat,p)
        actual[cdim]+=1
    pred=Counter()
    # Combine dimensions which coincide at small n.
    for dim,count in [(d,p),(2*n+1,p*(p+1)*(p**n-1)),
                      (2*n,p*(p**n-1)*(p**n-p)),
                      (n+2,p*(p*p-1)*p**n),
                      (n+1,p*(p*p-1)*(p**(2*n)-p**n)),
                      (2,p*(p**3-p*p)*p**(2*n))]:pred[dim]+=count
    assert {i:v for i,v in actual.items() if v}!={} # nonempty
    assert actual==+pred,(n,p,actual,pred)
    cc=sum(count*p**dim for dim,count in actual.items())
    N0=p**(4*n-1)+(p-1)*p**(2*n-1)
    H=p**(3*n-1)+(p-1)*p**(2*n-1)
    predicted=p*p*(N0+(p+1)*((p*p-1)*H+(p**3-p*p)*p**(2*n)))
    assert cc==predicted,(cc,predicted)
    print('VERIFIED',f'q={p}',f'n={n}',f'size={p**d}',f'commuting_pairs={cc}',f'centralizer_dims={sorted(actual.items())}')
if __name__=='__main__':
    for n,p in ((1,3),(1,5),(2,3)):
        check(n,p)
    print('VERIFY_OK')
