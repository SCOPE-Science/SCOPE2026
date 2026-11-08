"""Exact rational replay for mirrored five-site Crank--Nicolson positivity.
Only the Python standard library is required. Finite replay supplements the proof.
"""
from fractions import Fraction as Q
from math import sqrt


def inverse(A):
    n=len(A)
    B=[[Q(A[i][j]) for j in range(n)]+[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if B[i][k])
        B[k],B[p]=B[p],B[k]
        v=B[k][k]
        B[k]=[x/v for x in B[k]]
        for i in range(n):
            if i != k:
                v=B[i][k]
                B[i]=[B[i][j]-v*B[k][j] for j in range(2*n)]
    return [row[n:] for row in B]


def resolvent(h,t):
    L=[[Q(0) for _ in range(5)] for _ in range(5)]
    for i,w in enumerate([Q(1),t,t,Q(1)]):
        L[i][i]+=w;L[i+1][i+1]+=w
        L[i][i+1]-=w;L[i+1][i]-=w
    return inverse([[Q(int(i==j))+h*L[i][j]/2 for j in range(5)] for i in range(5)])


def formulas(h,t):
    D1=h*h*t+2*h*t+4*h+4
    D2=5*h*h*t+6*h*t+4*h+4
    e=(h+2)*((1+h*t)/D2+1/D1)
    c=D1/D2
    d=2*h*t*(3*h*h*t+4*h*t+4*h+4)/(D1*D2)
    diff=2*h*(t*(h+2)**2-4*(h+1))/(D1*D2)
    F=(3*h**4*t*t+8*h**3*t*t+4*h**3*t+4*h*h*t*t
       -8*h*h*t-16*h*t-16*h-16)
    C=3*h*h*t+2*h*t-4*h-4
    return D1,D2,e,c,d,diff,F,C


def positive_check(h,t):
    R=resolvent(h,t)
    D1,D2,e,c,d,diff,F,C=formulas(h,t)
    assert R[1][1]==R[3][3]==e
    assert R[2][2]==c
    assert R[0][0]==R[4][4]==e+d
    assert R[1][1]-R[2][2]==diff
    assert 2*R[2][2]-1==-C/D2
    assert 2*R[1][1]-1==-F/(D1*D2)
    assert d>0 and D1>0 and D2>0
    assert all(R[i][j]>0 for i in range(5) for j in range(5))
    assert all(sum(R[i])==1 for i in range(5))
    for i in range(5):
        for j in range(5):
            assert (2*R[i][j]-int(i==j)>=0)==(i!=j or R[i][i]>=Q(1,2))


def val(h,t):
    _,_,e,c,_,_,_,_=formulas(Q(h),Q(t))
    return min(float(e),float(c))-.5


def bisect(t):
    lo=0.;hi=1.
    while val(hi,t)>0:hi*=2
    for _ in range(65):
        mid=(lo+hi)/2
        if val(mid,t)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def run():
    checks=0
    for th in [Q(k,11) for k in range(1,120,4)]+[Q(k,7) for k in range(1,120,5)]:
        for hh in [Q(j,6) for j in range(1,37,2)]+[Q(j,9) for j in range(1,45,3)]:
            positive_check(hh,th)
            checks+=1
    assert formulas(Q(2),Q(3,4))[6:] == (Q(0),Q(0))
    checks+=1
    for t in [0.0001,.001,.01,.05,.25,.5,.74,.75,.76,1.,2.,10.,100.]:
        hc=(2-t+sqrt(t*t+8*t+4))/(3*t)
        def F(h):return (3*h**4*t*t+8*h**3*t*t+4*h**3*t+4*h*h*t*t-8*h*h*t-16*h*t-16*h-16)
        lo=0.;hi=max(1.,hc*5)
        while F(hi)<0:hi*=2
        for _ in range(80):
            mid=(lo+hi)/2
            if F(mid)<0:lo=mid
            else:hi=mid
        hf=(lo+hi)/2
        root=bisect(t)
        pred=hf if t<Q(3,4) else hc
        assert abs(root-pred)<2e-8*max(1.,pred)
        assert (hf<hc)==(t<.75)
        checks+=1
    assert abs(bisect(.000001)*sqrt(.000001)-2)<.001
    checks+=1
    print('VERIFY_OK',checks)

if __name__=='__main__':run()
