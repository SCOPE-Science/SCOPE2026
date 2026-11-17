"""Exact rational checks for the oscillation-ball projection variation modulus.
Scientific checks use only standard Python; finite checks do not replace the proof.
"""
from fractions import Fraction as F
from functools import lru_cache

NEG=-10**9

def E(m,k,z):
    if m<1 or k<0 or k>m or (z==0 and k==m) or (z==1 and k==0):
        return NEG
    return min(m-1,2*k if z==0 else 2*(m-k),
               2*(m-k)-1 if z==0 else 2*k-1)

def exact_coefficient(n):
    best=F(1); winner=None
    for t in range(1,n):
        u=n-t
        for a in range(1,t+1):
            for b in range(1,u+1):
                for z in (0,1):
                    p=E(t,a,z)
                    if p<0:continue
                    for w in (0,1):
                        q=E(u,b,w)
                        if q<0:continue
                        B=(a+b if z==0 and w==0 else
                           a if z==1 and w==0 else
                           b if z==0 and w==1 else 0)
                        v=F(b*p+a*q+B,a+b)
                        if v>best:best,winner=v,(t,a,b,z,w)
    return best,winner

@lru_cache(None)
def word(m,k,z):
    assert E(m,k,z)>=0
    if m==1: return (z,)
    for r in (0,1):
        if E(m-1,k-z,r)+(r!=z)==E(m,k,z):
            return word(m-1,k-z,r)+(z,)
    raise AssertionError('missing maximizer')

def projection(x,R=F(1)):
    # Exact independent scalar minimization over clipping intervals.
    if max(x)-min(x)<=R:return list(x)
    breaks=sorted({v for xi in x for v in (xi-R,xi)})
    tests=[breaks[0]-1]+[(s+t)/2 for s,t in zip(breaks,breaks[1:])]+[breaks[-1]+1]
    intervals=[(None,breaks[0])]+list(zip(breaks,breaks[1:]))+[(breaks[-1],None)]
    for sample,(lo,hi) in zip(tests,intervals):
        lower=[v for v in x if v<sample]
        upper=[v for v in x if v>sample+R]
        if not lower and not upper:continue
        center=(sum(lower+upper,F(0))-R*len(upper))/len(lower+upper)
        if (lo is None or center>=lo) and (hi is None or center<=hi):
            return [max(center,min(xi,center+R)) for xi in x]
    raise AssertionError('clipping minimizer not located')

def variation(v):return sum((abs(b-a) for a,b in zip(v,v[1:])),F(0))

def check():
    expected=['1','1','2','5/2','3','10/3','4','9/2','5','27/5','6','13/2','7','52/7','8']
    for n,s in enumerate(expected,start=2):
        assert exact_coefficient(n)[0]==F(s),(n,s)
    print('EXACT_FINITE_COEFFICIENTS_N2_TO_N16_PASS')
    for n in range(2,12):
        exact,_=exact_coefficient(n)
        independent=F(1)
        for mask in range(1,1<<n):
            S=[i for i in range(n) if mask>>i&1]
            if len(S)<2:continue
            for t in range(1,n):
                a=sum(i<t for i in S);b=len(S)-a
                if not a or not b:continue
                c=F(b,len(S)); v=[c if i in S else F(int(i>=t)) for i in range(n)]
                independent=max(independent,variation(v))
        assert exact==independent,(n,exact,independent)
    print('INDEPENDENT_SUBSET_AND_CUT_ENUMERATION_N2_TO_N11_PASS')
    for n in range(4,22):
        coefficient,w=exact_coefficient(n)
        t,a,b,z,r=w
        left=word(t,a,z)
        right=tuple(reversed(word(n-t,b,r)))
        bits=left+right
        assert sum(bits[:t])==a and sum(bits[t:])==b
        x=[F(-b) if bits[i] and i<t else F(1+a) if bits[i] else F(1,2) for i in range(n)]
        y=[v+(F(1,10) if i>=t else F(0)) for i,v in enumerate(x)]
        px=projection(x);py=projection(y)
        assert variation([py[i]-px[i] for i in range(n)])/variation([y[i]-x[i] for i in range(n)])==coefficient,(n,coefficient)
    print('INDEPENDENT_EXACT_FINITE_INPUT_ATTAINMENT_N4_TO_N21_PASS')
    for n in range(2,55):
        c,_=exact_coefficient(n)
        assert F(n//2)<=c<=1+2*n//3,(n,c)
    print('PROVED_LINEAR_BOUNDS_SPOT_CHECK_N2_TO_N54_PASS')
    print('ALL_OSCILLATION_BALL_CHECKS_PASS')

if __name__=='__main__': check()
