"""Independent count-weighted small-state update for a partially attached vertex.
Symmetric bits within each clique cell behave identically under each step.
This is numerical corroboration, not an infinite proof.
"""
from math import comb

def majority(ones, degree, old):
    return int(2 * ones > degree) if 2 * ones != degree else old

def next_state(state, m, r):
    mask=(1<<m)-1
    S=(state&mask).bit_count()
    A=(state&((1<<r)-1)).bit_count()
    h=(state>>m)&1
    result=0
    for i in range(m):
        old=(state>>i)&1
        ones=S-old+(h if i<r else 0)
        degree=m if i<r else m-1
        result|=majority(ones,degree,old)<<i
    result|=majority(A,r,h)<<m
    return result

weighted=0
for m in range(3,61):
    for r in range(1,m+1):
        s=m-r
        fixed=periodic=0
        for a in range(r+1):
            for b in range(s+1):
                weight=comb(r,a)*comb(s,b)
                bits=((1<<a)-1)|(((1<<b)-1)<<r)
                for h in (0,1):
                    x=bits|(h<<m)
                    y=next_state(x,m,r)
                    z=next_state(y,m,r)
                    if x==y: fixed+=weight
                    elif x==z:periodic+=weight
        if m%2==0:
            q=m//2
            expected=comb(m-r,q) if r<=q else 0
        else:
            q=(m-1)//2
            expected=(comb(r,q+1) if r>=q+1 else 0)
            if r==m-1:expected+=comb(m-1,q)
        assert fixed==2 and periodic==2*expected, (m,r,fixed,periodic,expected)
        weighted+=(r+1)*(s+1)*2
print(f"PASS: 1827 (m,r) cases through m=60; fixed and two-cycle counts match for all; at least {weighted} cell configurations considered (including safe overcount of loop count).")
