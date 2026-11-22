"""Finite rational verification of coupon completion and Poisson-time mixtures."""
from fractions import Fraction as F
from math import factorial, comb, sqrt, exp

def gf(n,z):
    a=F(n)*(1-z)/z
    out=F(1)
    for k in range(1,n+1):out*=F(k)/(k+a)
    return out

def geom_first(n, steps):
    # distribution of first completion T by independent coupon draws, DP exact fractions
    s=[F(0)]*(n+1);s[0]=F(1)
    out=[]
    for t in range(1,steps+1):
        nxt=[F(0)]*(n+1)
        for j in range(n):
            nxt[j]+=s[j]*F(j,n)
            nxt[j+1]+=s[j]*F(n-j,n)
        nxt[n]+=s[n]
        out.append(nxt[n]-s[n]);s=nxt
    return out

def missing(n,t,k):
    # inclusion-exclusion probability exactly k missing after t draws
    return comb(n,k)*sum(((-1)**h)*comb(n-k,h)*F(n-k-h,n)**t for h in range(n-k+1))

def beta_miss(n,k):
    # U~Beta(1,n), conditional K~Bin(n,U)
    return F(n*comb(n,k)*factorial(k)*factorial(2*n-k-1),factorial(2*n))

def check():
    num=0
    for n in range(2,8):
        H=sum(F(1,k) for k in range(1,n+1))
        first=geom_first(n,350)
        assert abs(float(sum(first))-1)<1e-10
        assert abs(float(sum((t+1)*p for t,p in enumerate(first)))-float(n*H))<1e-7
        z=F(n-1,n)**2
        assert gf(n,z)==sum((z**(t+1))*first[t] for t in range(len(first))) or abs(float(gf(n,z)-sum((z**(t+1))*first[t] for t in range(len(first)))))<1e-30
        for k in range(n+1):
            v=beta_miss(n,k)
            assert v>=0
            num+=1
        assert sum(beta_miss(n,k) for k in range(n+1))==1
        assert beta_miss(n,0)==F(1,2)
        print('n', n, 'beta_binomial_p0', str(beta_miss(n,0)), 'generating_function', float(gf(n,z)))
    print('PASS',num,'rational Beta-binomial entries, normalization, generating identity')
if __name__=='__main__': check()
