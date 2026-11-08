"""Exact enumeration for zero-triples in the inverse-square modular graph.
Uses no external dependencies. Checks a formula for every modulus 2..300.
"""
from math import gcd

def factor(n):
    d=2
    fs=[]
    while d*d<=n:
        if n%d==0:
            a=0
            while n%d==0:
                n//=d;a+=1
            fs.append((d,a))
        d+=1
    if n>1: fs.append((n,1))
    return fs

def factor_T(p,a):
    if p == 3:
        return 3**(a-1) if a<=2 else 0
    if p % 3 == 1:
        return 2*p**(a//2)
    return 0

def predicted(n):
    T=1
    ph=n
    for p,a in factor(n):
        T*=factor_T(p,a)
        ph=ph//p*(p-1)
    return ph*T

def enumerate_direct(n):
    units=[x for x in range(n) if gcd(x,n)==1]
    squares={x:pow(pow(x,-1,n),2,n) for x in units}
    ans=0
    for x in units:
        for y in units:
            z=(-x-y)%n
            if z in squares and (squares[x]+squares[y]+squares[z])%n==0:
                ans+=1
    return ans

def count_by_ratio(n):
    ans=0
    for t in range(n):
        if gcd(t,n)==1 and gcd(1+t,n)==1 and (t*t+t+1)**2%n==0:
            ans+=1
    return ans

def run():
    ns=range(2,301)
    for n in ns:
        n_direct=enumerate_direct(n)
        n_formula=predicted(n)
        n_ratio=count_by_ratio(n)
        ph=sum(gcd(x,n)==1 for x in range(n))
        assert n_direct == n_formula == ph*n_ratio,(n,n_direct,n_formula,n_ratio)
    for n,v in {2:0,3:2,7:12,9:18,21:24,27:0,49:588,81:0,91:288,169:4056}.items():
        assert predicted(n)==v,(n,predicted(n),v)
    print('VERIFY_OK moduli=2..300 direct_triple_enumeration=299 ratio_count=299 formula=PASS')
    print('critical_examples',[(n,predicted(n)) for n in (3,7,9,27,49,81,169)])

if __name__=='__main__':run()
