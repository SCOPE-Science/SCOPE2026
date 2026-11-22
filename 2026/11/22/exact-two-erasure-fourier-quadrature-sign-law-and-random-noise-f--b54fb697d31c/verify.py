"""Direct finite checks for exact double-erasure trigonometric quadrature.

All universal assertions in the note are proved analytically; finite tests only
probe implementations and boundary conventions.
"""
from math import pi, sin, cos, tan, isclose
import numpy as np

def formula(n,a,b):
    m=(n-3)//2
    nu=m+1
    r=(nu*(b-a)) % n
    if r>n//2:
        a,b=b,a
        r=n-r
    delta=r
    assert 1<=delta<= (n-1)//2
    h=pi/n
    k=np.array([(nu*(j-a))%n for j in range(n)])
    w=(1-np.cos((2*k-delta)*h)/cos(delta*h))/n
    H=(1/tan(h)*tan(delta*h)-delta)/n
    L2=(1+0.5/cos(delta*h)**2)/n
    return w,delta,H,L2,k

def verify():
    counts={'cases':0,'positive_patterns':0,'negative_patterns':0,'direct_solves':0,'max_fourier_residual':0.0,'max_weight_residual':0.0}
    for n in range(5,56,2):
        m=(n-3)//2
        for a in range(n):
            for b in range(a+1,n):
                w,delta,H,L2,k=formula(n,a,b)
                counts['cases']+=1
                assert abs(w[a])<1e-10 and abs(w[b])<1e-10
                assert abs(sum(w)-1)<1e-10
                neg=int(np.sum(w< -1e-10))
                assert neg==delta-1,(n,a,b,delta,neg)
                if delta==1:counts['positive_patterns']+=1
                else:counts['negative_patterns']+=1
                assert (delta==1)==(((b-a)%n in (2,n-2)))
                assert abs(float(-sum(w[w<0]))-H)<1e-10
                assert abs(float(np.dot(w,w))-L2)<1e-10
                for r in range(1,m+1):
                    moment=np.dot(w,np.exp(2j*pi*r*np.arange(n)/n))
                    counts['max_fourier_residual']=max(counts['max_fourier_residual'],abs(moment))
                    assert abs(moment)<1e-10
                if n<=15 and (a,b) in ((0,1),(0,2),(0,n//2),(1,n-1)):
                    surviving=[j for j in range(n) if j not in (a,b)]
                    freq=np.arange(-m,m+1)
                    V=np.exp(2j*pi*np.outer(freq,np.array(surviving))/n)
                    rhs=np.array([1.0 if q==0 else 0.0 for q in freq])
                    direct=np.linalg.solve(V,rhs)
                    err=max(abs(direct-w[surviving]))
                    assert err<1e-9,(n,a,b,err)
                    counts['max_weight_residual']=max(counts['max_weight_residual'],float(err))
                    counts['direct_solves']+=1
        assert counts['cases']>0
    assert counts['max_fourier_residual']<1e-10
    for n in range(5,200,2):
        K=(n-1)//2
        ratios=[1+1/(2*cos(pi*d/n)**2) for d in range(1,K+1)]
        assert abs(sum(ratios)/K-(n+3)/2)<1e-8
    print('All finite checks PASS:',counts, 'and 98 random-erasure mean identities')
    for n in (5,7,9,11,101):
        delta=(n-1)//2
        w,_,H,L2,_=formula(n,0,(-2*delta)%n)
        print('n',n,'worst neg mass',round(H,12),'TV',round(1+2*H,12),'variance ratio',round(n*L2,12))

if __name__=='__main__':verify()
