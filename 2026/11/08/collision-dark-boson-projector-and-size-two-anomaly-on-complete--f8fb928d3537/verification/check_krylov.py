"""Independent exact observability/Krylov computation; no projector formulas used."""
from itertools import combinations_with_replacement
from sympy import zeros, Matrix

for a,b in [(2,2),(2,3),(2,4),(3,3),(3,4),(4,4)]:
    n=a+b
    states=list(combinations_with_replacement(range(n),2))
    d=len(states); pos={x:i for i,x in enumerate(states)}
    A=zeros(n,n)
    for u in range(a):
        for v in range(a,n): A[u,v]=A[v,u]=1
    # Matrix action on symmetric amplitude matrices, in natural (unnormalized) basis.
    H=zeros(d,d)
    for c,(i,j) in enumerate(states):
        X=zeros(n,n); X[i,j]=X[j,i]=1
        Y=A*X+X*A
        for r,(k,l) in enumerate(states): H[r,c]=Y[k,l]
    # observations at coincident particle configurations, all moments 0..4
    D=zeros(n,d)
    for i in range(n):D[i,pos[(i,i)]]=1
    blocks=[]; Q=D
    for _ in range(5):
        blocks.append(Q);Q=Q*H
    O=blocks[0].col_join(blocks[1]).col_join(blocks[2]).col_join(blocks[3]).col_join(blocks[4])
    dark=d-O.rank()
    target=(n-1)*(n-4)//2+int(a==2)+int(b==2)
    assert dark==target,(a,b,dark,target)
    print(f'K_{{{a},{b}}}: full={d}, observable={O.rank()}, dark={dark}')
print('KRYLOV_INDEPENDENT_OK')
