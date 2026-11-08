"""Exact rational checks for a simple symmetric bridge maximum/return identity.

Run: python verify.py
Python 3.9 or later; uses only standard library.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def predicted(n):
    assert n >= 1
    ratio = Fraction(4**n, comb(2*n,n))
    return {
        'E_K': ratio - 1,
        'E_M': (ratio - 1)/2,
        'E_KM': Fraction(3*n,2) + 1 - ratio,
        'E_K2': 4*n + 3 - 3*ratio,
        'E_M2': Fraction(2*n+1,2) - ratio/2,
        'cov': Fraction(3*n+1,2)-ratio**2/2,
        'varK': 4*n+2-ratio-ratio**2,
        'varM': Fraction(4*n+1,4)-ratio**2/4,
    }


def dp_moments(n):
    # State is (height, running maximum); aggregate count, K, K^2.
    d = {(0,0):(1,0,0)}
    for t in range(1,2*n+1):
        nd = defaultdict(lambda:(0,0,0))
        for (pos,high),(c,k,k2) in d.items():
            for delta in (-1,1):
                newpos=pos+delta
                if abs(newpos)>2*n-t: continue
                newhigh=max(high,newpos)
                c0,k0,k20=nd[(newpos,newhigh)]
                hit=int(newpos==0)
                nd[(newpos,newhigh)]=(c0+c, k0+k+hit*c,
                                     k20+k2+2*hit*k+hit*c)
        d=nd
    totals=[0]*6
    for (pos,maximum),(c,k,k2) in d.items():
        assert pos==0
        for i,val in enumerate((c,k,c*maximum,k*maximum,k2,c*maximum**2)):
            totals[i]+=val
    assert totals[0]==comb(2*n,n)
    den=totals[0]
    EK,EM,EKM,EK2,EM2=(Fraction(t,den) for t in totals[1:])
    return dict(E_K=EK,E_M=EM,E_KM=EKM,E_K2=EK2,E_M2=EM2,
                cov=EKM-EK*EM,varK=EK2-EK**2,varM=EM2-EM**2)


def exhaustive_moments(n):
    sums=[0]*6
    for plus in combinations(range(2*n),n):
        plus=set(plus)
        position=0; maximum=0; returns=0
        for j in range(2*n):
            position += 1 if j in plus else -1
            maximum=max(maximum,position)
            if position==0:returns+=1
        assert position==0
        for i,value in enumerate((1,returns,maximum,returns*maximum,returns**2,maximum**2)):
            sums[i]+=value
    den=sums[0]
    EK,EM,EKM,EK2,EM2=(Fraction(v,den) for v in sums[1:])
    return dict(E_K=EK,E_M=EM,E_KM=EKM,E_K2=EK2,E_M2=EM2,
                cov=EKM-EK*EM,varK=EK2-EK**2,varM=EM2-EM**2)


def main():
    checks=0
    for n in range(1,41):
        expected=predicted(n)
        observed=dp_moments(n)
        for name,value in expected.items():
            assert observed[name]==value,(n,name,observed[name],value)
            checks+=1
        if n>=2:
            assert expected['cov']<0
            checks+=1
        else:
            assert expected['cov']==0
            checks+=1
        if n<=9:
            independent=exhaustive_moments(n)
            for name,value in expected.items():
                assert independent[name]==value,(n,name,independent[name],value)
                checks+=1
    print(f'PASS {checks} exact rational identities; DP n=1..40, exhaustive n=1..9.')
    print('Covariance n=2:', predicted(2)['cov'])

if __name__=='__main__':main()
