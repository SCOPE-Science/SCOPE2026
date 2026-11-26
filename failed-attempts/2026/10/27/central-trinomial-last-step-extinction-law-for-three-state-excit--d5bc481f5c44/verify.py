"""Finite-path Greenberg--Hastings terminal-time independent checks."""
from itertools import product
from collections import defaultdict
from math import factorial

def iterate(x):
    n=len(x)
    return tuple(2 if v==1 else 0 if v==2 else int((i>0 and x[i-1]==1) or (i<n-1 and x[i+1]==1)) for i,v in enumerate(x))

def brute(n):
    count=0
    for x in product(range(3),repeat=n):
        y=x;t=0
        while any(y):
            assert t<=n+1,(n,x,t,y)
            y=iterate(y);t+=1
        if t==n+1:count+=1
    return count

def ballot(n):
    d={(1,1):1}
    for _ in range(n-2):
        nd=defaultdict(int)
        for (h,a),w in d.items():
            for b in range(3):
                delta=(a==0 and b==1)-(a==1 and b==0)
                if h+delta>=1:nd[h+delta,b]+=w
        d=nd
    return 2*sum(d.values())

def central_trinomial(m):
    return sum(factorial(m)//(factorial(j)**2*factorial(m-2*j)) for j in range(m//2+1))

def gf_coeffs(max_n):
    # G(z)=sqrt((1+z)/(1-3z)), so (1-3z)G(z)^2=1+z;
    # terminal generating function W(z)=z*(G(z)-1).
    g=[1]
    for k in range(1,max_n):
        rhs=(1 if k==1 else 0)+3*sum(g[i]*g[k-1-i] for i in range(k))
        v=rhs-sum(g[i]*g[k-i] for i in range(1,k))
        assert v%2==0,(k,v)
        g.append(v//2)
    return {n:g[n-1] for n in range(2,max_n+1)}

if __name__=='__main__':
    a=gf_coeffs(42)
    for n in range(2,43):
        assert ballot(n)==a[n],(n,ballot(n),a[n])
        assert a[n]==central_trinomial(n-1)+central_trinomial(n-2)
        if n<=11:
            b=brute(n)
            assert a[n]==b,(n,a[n],b)
            print(f'n={n} states={3**n} terminal={a[n]} brute={b} ballot={ballot(n)}')
    print('PATH_GHM_FOUR_WAY_VERIFY_OK n=2..11 exhaustive; n=2..42 ballot-GF-trinomial')
