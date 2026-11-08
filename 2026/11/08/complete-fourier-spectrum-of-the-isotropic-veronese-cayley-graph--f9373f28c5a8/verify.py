"""Exact finite arithmetic and direct character checks for isotropic Veronese Cayley spectra."""
from itertools import product
from collections import Counter
from math import comb, pi
import cmath

def check(q):
    pts=[];seen=set()
    for v in product(range(q), repeat=3):
        if v==(0,0,0) or sum(x*x for x in v)%q:continue
        i=next(i for i,x in enumerate(v) if x)
        c=pow(v[i],-1,q); w=tuple((x*c)%q for x in v)
        if w not in seen:seen.add(w);pts.append(w)
    assert len(pts)==q+1
    S=set()
    for w in pts:
        for a in range(1,q):
            S.add(tuple(a*w[i]*w[j]%q for i in range(3) for j in range(3)))
    assert len(S)==q*q-1
    z=cmath.exp(2j*pi/q)
    counted=Counter()
    for a,b,c,d,e in product(range(q),repeat=5):
        # symmetric Y with Y33=0, coords 11=a 22=b 12=c 13=d 23=e
        Y=(a,c,d,c,b,e,d,e,0)
        k=0
        for u in pts:
            v=sum(Y[3*i+j]*u[i]*u[j] for i in range(3) for j in range(3))%q
            if v==0:k+=1
        lam=q*k-(q+1)
        if (a,b,c,d,e)==(0,)*5: assert k==q+1 and lam==q*q-1
        else:assert k<=4
        # independent primitive root-of-unity sum
        val=sum(z**(sum(X[i]*Y[i] for i in range(9))%q) for X in S)
        assert abs(val-lam)<1e-8,(q,a,b,c,d,e,k,val,lam)
        counted[k]+=1
    assert counted[q+1]==1
    for k in range(5):
        incl=comb(q+1,k)*sum((-1)**j*comb(q+1-k,j)*(q**(5-k-j)-1) for j in range(5-k))
        assert incl==counted[k],(q,k,incl,counted[k])
        assert incl>0
    print('PASS q=',q,'q^5=',q**5,'S=',len(S),'root multiplicities=',dict(sorted(counted.items())))

if __name__=='__main__':
    check(5)
    print('ISOTROPIC_VERONESE_FOURIER_CENSUS_PASS')
