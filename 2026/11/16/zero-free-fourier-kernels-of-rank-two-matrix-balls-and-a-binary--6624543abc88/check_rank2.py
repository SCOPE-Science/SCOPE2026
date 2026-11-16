"""Independent exact tests of low-rank matrix-ball character sums.
Uses elementary row reduction, binary Walsh transform, and integer traces.
"""
from functools import lru_cache
from itertools import product
from math import prod

@lru_cache(None)
def gaussian(n,k,q):
    if not 0<=k<=n: return 0
    if k==0 or k==n: return 1
    return gaussian(n-1,k-1,q)+q**k*gaussian(n-1,k,q)

def rank_mod_p(entries,m,n,p):
    a=[list(entries[i*n:(i+1)*n]) for i in range(m)]
    row=0
    for col in range(n):
        k=next((i for i in range(row,m) if a[i][col]%p),None)
        if k is None: continue
        a[row],a[k]=a[k],a[row]
        u=pow(a[row][col],-1,p)
        a[row]=[(u*x)%p for x in a[row]]
        for i in range(m):
            if i!=row and a[i][col]%p:
                v=a[i][col]
                a[i]=[(x-v*y)%p for x,y in zip(a[i],a[row])]
        row+=1
        if row==m: break
    return row

def coeff_formula(m,n,r,q):
    t=m-r
    a=gaussian(m-1,1,q)
    c=(a-1)*gaussian(m,1,q)-gaussian(m,2,q)+1
    return q**(2*n)*gaussian(t,2,q)-(a-1)*q**n*gaussian(t,1,q)+c

def rank_count(m,n,r,q):
    return gaussian(m,r,q)*prod(q**n-q**i for i in range(r))

def fast_walsh(a):
    n=len(a)
    h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def check_binary(m,n):
    size=1<<(m*n)
    vals=[]
    for mask in range(size):
        entries=[(mask>>j)&1 for j in range(m*n)]
        vals.append(int(rank_mod_p(entries,m,n,2)<=2))
    fw=fast_walsh(vals[:])
    counts=[0]*(m+1)
    for mask,value in enumerate(fw):
        b=[(mask>>j)&1 for j in range(m*n)]
        r=rank_mod_p(b,m,n,2)
        assert value==coeff_formula(m,n,r,2),(m,n,mask,r,value,coeff_formula(m,n,r,2))
        counts[r]+=1
    assert counts==[rank_count(m,n,r,2) for r in range(m+1)]
    assert sum(fw)==size  # zero frequency lies inside ball
    assert sum(x*x for x in fw)==size*sum(vals)
    print(f'binary {m}x{n}: {size} exact Fourier values, norm numerator={sum(map(abs,fw))}, denominator={size}')

def check_ternary(m,n):
    q=3
    # Exhaust all A in rank <=2; trace pairing with rank-r canonical dual.
    ball=[]
    count=[0]*(m+1)
    for a in product(range(q),repeat=m*n):
        rank=rank_mod_p(a,m,n,q)
        count[rank]+=1
        if rank<=2:ball.append(a)
    assert count==[rank_count(m,n,r,q) for r in range(m+1)]
    for r in range(m+1):
        z=[0,0,0]
        for a in ball:
            z[sum(a[i*n+i] for i in range(r))%3]+=1
        assert z[1]==z[2]
        value=z[0]-z[1]
        assert value==coeff_formula(m,n,r,q),(m,n,r,value,coeff_formula(m,n,r,q))
    print(f'ternary {m}x{n}: {q**(m*n)} matrices, {len(ball)} in rank-2 ball, {m+1} independent character sums')

if __name__=='__main__':
    check_binary(3,3)
    check_binary(3,4)
    check_binary(4,4)
    check_ternary(3,3)
    for q in (2,3,4,5,7,8,9,11,16):
        for m in range(3,25):
            for n in (m,m+1,m+2,m+4):
                neg=[m-r for r in range(m+1) if coeff_formula(m,n,r,q)<0]
                expected=([2,1] if q==2 and n==m and m>=5 else [1])
                assert neg==expected,(q,m,n,neg,expected)
                assert all(coeff_formula(m,n,r,q)!=0 for r in range(m+1))
                assert sum(rank_count(m,n,r,q) for r in range(m+1))==q**(m*n)
                assert coeff_formula(m,n,0,q)==1+rank_count(m,n,1,q)+rank_count(m,n,2,q)
    print('RANK_TWO_BALL_ALL_EXACT_CHECKS_PASS')
