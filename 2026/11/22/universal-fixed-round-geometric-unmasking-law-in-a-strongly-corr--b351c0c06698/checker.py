#!/usr/bin/env python3
"""Finite consistency checks for the exact Ising masked-unmasking stage cost."""
import math
import numpy as np


def information(f, d):
    z=(1-2*f)**d
    return 0.5*((1+z)*math.log1p(z)+(1-z)*math.log1p(-z))


def closed(f,p,q,ks):
    a=1-p
    z=np.exp(2*ks*math.log1p(-2*f))
    c=1/(2*ks*(2*ks-1))
    return float(q*q*a*a*np.sum(c*z/(1-a*(1-q)*z)*((1-z)/(1-a*z))**2))


def gaps(f,p,q,n):
    # Independent triple sum from the exact gap representation.
    assert p>0
    a=1-p;b=1-q
    inf=[0]+[information(f,i) for i in range(1,3*n+3)]
    tot=0.0
    for l in range(1,n+1):
        for d in range(1,n+1):
            base=p*p*q*q*(a**(l+d))*(b**(d-1))
            for r in range(1,n+1):
                bar=inf[d]-inf[d+l]-inf[d+r]+inf[d+l+r]
                tot+=base*(a**(r-1))*bar
    return tot


def schedule(f,m,ks):
    ps=[0.0]+[(f/math.log(2))**((m-j)/m) for j in range(1,m)]+[1.0]
    return sum(closed(f,ps[j-1],(ps[j]-ps[j-1])/(1-ps[j-1]),ks) for j in range(1,m+1))


def main():
    count=0
    for f,p,q in [(0.17,0.3,0.4),(0.12,0.25,0.55),(0.15,0.4,0.7)]:
        ks=np.arange(1,3000,dtype=float)
        exact=closed(f,p,q,ks)
        triple=gaps(f,p,q,45)
        assert abs(exact-triple)<0.00001,(f,p,q,exact,triple)
        count+=1
    for f in [0.03,0.008,0.002]:
        ks=np.arange(1,int(20/f)+1,dtype=float)
        lhs=closed(f,0,1,ks)
        rhs=math.log(2)+f*math.log(f)+(1-f)*math.log1p(-f)
        assert abs(lhs-rhs)<1e-9,(f,lhs,rhs)
        count+=1
    for m in [2,3,4]:
        vals=[]
        for f in [1e-4,1e-5]:
            ks=np.arange(1,int(8/f)+1,dtype=float)
            ans=schedule(f,m,ks)
            leading=m*math.log(2)**(1/m)*f**((m-1)/m)
            vals.append(ans/leading)
            assert 0<ans<leading,(m,f,ans,leading)
            count+=1
        assert abs(vals[1]-1)<abs(vals[0]-1),(m,vals)
        count+=1
    print(f'PASS: {count} independent finite checks; no claim of infinite computational verification.')

if __name__=='__main__':
    main()
