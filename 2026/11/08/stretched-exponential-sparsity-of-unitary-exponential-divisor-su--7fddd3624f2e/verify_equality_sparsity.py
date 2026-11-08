"""Exact finite checks for the unitary/exponential divisor equality theorem.
Run: python equality_sparsity_verify.py
"""
from math import isqrt

def build_spf(N):
    s = list(range(N+1))
    for p in range(2,isqrt(N)+1):
        if s[p]==p:
            for k in range(p*p,N+1,p):
                if s[k]==k:s[k]=p
    return s

def factor(n,s):
    out=[]
    while n>1:
        p=s[n]; a=0
        while n%p==0:n//=p;a+=1
        out.append((p,a))
    return out

def values(f):
    us=es=1
    for p,a in f:
        powpa=p**a
        us *= 1+powpa
        es *= sum(p**d for d in range(1,a+1) if a%d==0)
    return us,es

def verify(N=500000):
    s=build_spf(N); ans=[]; checked=0
    for n in range(1,N+1):
        f=factor(n,s)
        u,e=values(f)
        if u==e:ans.append(n)
        for p,a in f:
            if a==1:
                # Multiplicative prime-removal identity, exact at every test instance.
                m=n//p; um,em=values(factor(m,s))
                assert u==(p+1)*um and e==p*em
                if u==e:assert p*(em-um)==um and em>um
                checked+=1
    assert ans==[1,20,45,320,6615,382200],ans
    print('VERIFY_OK N=',N,' equality_cases=',ans,' prime_exponent_one_cases=',checked)
if __name__=='__main__': verify()
