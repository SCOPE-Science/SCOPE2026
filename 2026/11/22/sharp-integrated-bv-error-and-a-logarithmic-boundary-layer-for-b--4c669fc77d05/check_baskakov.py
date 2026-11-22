"""Direct numerical consistency checks for a sharp Baskakov approximation theorem.
Run: python check_baskakov.py (requires numpy, scipy).
This is a numerical consistency test, not an infinite proof.
"""
from math import comb, log, sqrt, pi
import numpy as np
from scipy.special import betainc
from scipy.integrate import quad
from scipy.stats import nbinom

def F(n, j, x):
    return betainc(j, n, x/(1+x))

def J(n, j, x):
    return x*F(n,j,x) - j/(n-1)*betainc(j+1,n-1,x/(1+x))

def E(n,j,s):
    return 1-s+2*J(n,j,s)-J(n,j,1.)

def C(n):
    j=np.arange(1,n+1)
    lo=(j-1)/n
    hi=j/n
    a=E(n,j,lo); b=E(n,j,hi)
    k=int(np.argmax(np.maximum(a,b)))
    return float(max(a[k],b[k])),int(j[k]), ('lower' if a[k]>=b[k] else 'upper')

def direct_E(n,j,s):
    q=lambda x: 1-nbinom.cdf(j-1,n,1/(1+x))
    return quad(q,0,s,epsabs=1e-12)[0]+quad(lambda x:1-q(x),s,1,epsabs=1e-12)[0]

def main():
    counts={'tail':0,'integral':0,'endpoint':0}
    for n in [2,3,5,8,13,20,30]:
        for j in range(1,n+1):
            for x in [.07,.25,.64,1.0]:
                expected=1-nbinom.cdf(j-1,n,1/(1+x))
                assert abs(F(n,j,x)-expected)<2e-12,(n,j,x,F(n,j,x),expected)
                counts['tail']+=1
            s=(j-.37)/n
            direct=direct_E(n,j,s)
            assert abs(E(n,j,s)-direct)<3e-11,(n,j,s,E(n,j,s),direct)
            counts['integral']+=1
            vals=np.array([E(n,j,v) for v in np.linspace((j-1)/n,j/n,17)])
            assert max(vals)<=max(vals[0],vals[-1])+2e-11
            counts['endpoint']+=1
    print('independent_checks',counts)
    for n in [10,30,100,300,1000,3000,10000]:
        c,j,side=C(n)
        s=(j-1)/n if side=='lower' else j/n
        print('degree',n,'C',format(c,'.12g'),'j',j,'side',side,
              'sqrt_n_C',round(sqrt(n)*c,7),
              'boundary_scale',(1-s)*sqrt(n/log(n)))
    print('target leading constant',2/sqrt(pi),'target boundary scale',sqrt(2))
    print('All numerical checks passed.')

if __name__=='__main__':main()
