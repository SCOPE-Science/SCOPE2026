"""Exact and numerical checks for continuous A-optimal grounding on stars.

Uses only Python standard library. These finite checks supplement an analytic proof.
"""
from fractions import Fraction as Q
from math import isclose
import random


def inv(A):
    n=len(A)
    M=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        pivot=next((i for i in range(k,n) if M[i][k]),None)
        if pivot is None: raise AssertionError('singular matrix')
        M[k],M[pivot]=M[pivot],M[k]
        pivotval=M[k][k]
        M[k]=[z/pivotval for z in M[k]]
        for i in range(n):
            if i!=k:
                factor=M[i][k]
                if factor:M[i]=[a-factor*b for a,b in zip(M[i],M[k])]
    return [r[n:] for r in M]


def formula(m,B,p):
    t=1+(B-p)/m
    u=m+p
    return (m-1)/t+(u+t)/(u*t-m)


def derivative(m,B,p):
    t=1+(B-p)/m
    u=m+p
    D=u*t-m
    return (m-1)/(m*t*t)+((1-Q(1,m))*D-(u+t)*(t-u/Q(m)))/(D*D)


def H(m,B):
    return B**3+4*m*B*B-m*(m**3-m*m-5*m)*B+2*m**3


def matrix(m,p,q):
    n=m+1
    M=[[Q(0) for _ in range(n)] for _ in range(n)]
    M[0][0]=m+p
    for i in range(1,n):
        M[i][i]=1+q
        M[i][0]=M[0][i]=-1
    return M


def float_derivative(m,B,p):
    return float(derivative(m,B,p))


def optimum(m,B):
    if float_derivative(m,B,0)>=0:return 0.0
    lo,hi=0.0,float(B)
    for _ in range(80):
        mid=(lo+hi)/2
        if float_derivative(m,B,mid)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def count_tests():
    checks=0
    rng=random.Random(93724)
    # Independent rational Gauss-Jordan matrix inversion versus arrowhead trace.
    for m in range(2,10):
        for b in (Q(1,5),Q(1),Q(2),Q(5),Q(11,3),Q(30)):
            for j in range(1,9):
                B=b;p=B*Q(j,10);q=(B-p)/m
                V=inv(matrix(m,p,q))
                exact=sum(V[i][i] for i in range(m+1))
                assert exact==formula(m,B,p);checks+=1
                # Independent directional-gradient identity d trace(inv(A))/dp
                W=[[sum(V[i][h]*V[h][k] for h in range(m+1)) for k in range(m+1)] for i in range(m+1)]
                grad=-W[0][0]+sum(W[i][i] for i in range(1,m+1))/m
                assert grad==derivative(m,B,p);checks+=1
            assert derivative(m,b,0)==-H(m,b)/(b*m*m*(b+m)**2);checks+=1
            assert derivative(m,b,b)==(b+2)/b;checks+=1
    # Check both boundary branches and the unique interior KKT root.
    for m in list(range(2,41)) + [50,75,100]:
        Bs=[.0001,.01,.1,.5,1,2,5,10,30,100,300,1000,m,m*m/2,2*m*m]
        for B in Bs:
            p=optimum(m,B)
            d0=float_derivative(m,B,0)
            assert (p==0)==(d0>=0);checks+=1
            assert p>=0 and p<B;checks+=1
            # Convexity / KKT certificate and sample-based global comparisons.
            F0=float(formula(m,B,p))
            for j in range(20):
                q=B*rng.random()
                assert float(formula(m,B,q))>=F0-1e-8*max(1,F0);checks+=1
            if p>0:
                assert abs(float_derivative(m,B,p))<2e-6*max(1,abs(d0));checks+=1
    for m in [2,3]:
        assert all(H(m,Q(k,5))>0 for k in range(1,1000));checks+=1
    for m in range(4,90):
        # H has two positive zeros: m=4 witness B=2, others B=m.
        mid=2 if m==4 else m
        assert H(m,Q(0))>0 and H(m,Q(mid))<0 and H(m,Q(2*m*m))>0;checks+=1
        lo,hi=0.,float(mid)
        for _ in range(70):
            z=(lo+hi)/2
            if H(m,z)>0:lo=z
            else:hi=z
        low=(lo+hi)/2
        lo,hi=float(mid),float(2*m*m)
        for _ in range(70):
            z=(lo+hi)/2
            if H(m,z)<0:lo=z
            else:hi=z
        high=(lo+hi)/2
        assert low<high and abs(H(m,low))/max(1,2*m**3)<1e-6;checks+=1
        assert abs(H(m,high))/max(1,m**6)<1e-6;checks+=1
        for B in [low/2,(low+high)/2,high*1.1]:
            p=optimum(m,B)
            assert (p>1e-10)==(B<low or B>high);checks+=1
    print('VERIFY_OK:',checks,'exact-rational and numerical assertions')

if __name__=='__main__': count_tests()
