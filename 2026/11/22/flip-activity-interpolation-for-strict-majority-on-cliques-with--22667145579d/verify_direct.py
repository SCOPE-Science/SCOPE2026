"""Independent bitwise full-state verification for majority automata on K_{2m} minus a matching."""
from collections import Counter
from math import comb

def update(x, m, k):
    n=2*m
    out=0
    for v in range(n):
        pair=v^1 if v<2*k else None
        degree=n-1-(pair is not None)
        ones=sum((x>>j)&1 for j in range(n) if j!=v and j!=pair)
        old=(x>>v)&1
        new=(ones*2>degree) or (ones*2==degree and old==1)
        if new:out|=1<<v
    return out

def polynomial(m,k):
    # Coefficient counts by number of discordant forbidden pairs.
    ans={}
    for j in range(k+1):
        s=sum(comb(k-j,r)*comb(2*m-2*k,m-j-2*r)
              for r in range(k-j+1) if 0<=m-j-2*r<=2*m-2*k)
        ans[j]=comb(k,j)*2**j*s
    return ans

checked=0
for m in range(2,8):
 for k in range(m+1):
    n=2*m;observed=Counter();fixed=0;primitive=0
    for x in range(1<<n):
        y=update(x,m,k)
        z=update(y,m,k)
        weight=x.bit_count()
        if weight!=m:
            assert y==(0 if weight<m else (1<<n)-1),(m,k,x,y)
        else:
            assert z==x,(m,k,x,y,z)
            frozen=sum(((x>>(2*i))&1)!=((x>>(2*i+1))&1) for i in range(k))
            expected=x
            for v in range(n):
                if v>=2*k or not ((x>>(v//2*2))&1)!=((x>>(v//2*2+1))&1):
                    expected^=1<<v
            assert y==expected,(m,k,x,y,expected)
            observed[frozen]+=1
        if y==x:fixed+=1
        elif z==x:primitive+=1
        checked+=1
    assert dict(observed)=={j:v for j,v in polynomial(m,k).items() if v},(m,k,observed,polynomial(m,k))
    assert fixed==2+(2**m if k==m else 0),(m,k,fixed)
    assert primitive==comb(2*m,m)-(2**m if k==m else 0),(m,k,primitive)
    print(f'm={m} k={k} fixed={fixed} primitive_states={primitive} activity_hist={dict(sorted(observed.items()))}')
print(f'PASS: {checked} total labelled initial states, all m=2..7 matching sizes')
