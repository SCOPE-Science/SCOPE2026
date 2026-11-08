"""Standalone checks for a piecewise-affine renewal system (Python 3 stdlib)."""
from fractions import Fraction as Q
from math import exp, log, isclose


def det(M):
    A=[[Q(z) for z in row] for row in M]
    n=len(A); ans=Q(1)
    for k in range(n):
        i=next((j for j in range(k,n) if A[j][k]),None)
        if i is None: return Q(0)
        if i!=k:
            A[k],A[i]=A[i],A[k];ans=-ans
        pivot=A[k][k];ans*=pivot
        for j in range(k+1,n):
            c=A[j][k]/pivot
            for h in range(k+1,n):A[j][h]-=c*A[k][h]
            A[j][k]=Q(0)
    return ans


def f(x,q):return -q*x-1 if x<=0 else x-1

def pressure_root(q,s):
    # Positive Perron root for the tilt t=log(q)+s, using stable form.
    e=exp(s)
    lo=1+e/10**6;hi=1+e
    def a(z):return (z-1)-e*(1-z**(-q))
    assert a(lo)<0<=a(hi)
    for _ in range(140):
        mid=(lo+hi)/2
        if a(mid)>0:hi=mid
        else:lo=mid
    return (lo+hi)/2

count=0
for q in range(3,10):
    A=[[0]*q for _ in range(q)]
    P=[[Q(0)]*q for _ in range(q)]
    for j in range(q):A[0][j]=1;P[0][j]=Q(1,q)
    for i in range(1,q):A[i][i-1]=1;P[i][i-1]=Q(1)
    pi=[Q(2*(q-i),q*(q+1)) for i in range(q)]
    assert sum(pi)==1
    for j in range(q):assert sum(pi[i]*P[i][j] for i in range(q))==pi[j]
    # Polynomial identity by equality at q+1 integer arguments.
    for z in range(q+1):
        D=det([[z*(i==j)-A[i][j] for j in range(q)] for i in range(q)])
        target=z**q-sum(z**j for j in range(q))
        assert D==target,(q,z,D,target)
        count+=1
    # Every subcell of I_0 is mapped to I_j, then returns after j+1 steps.
    for j in range(q):
        x=-Q(2*j+1,2*q)
        y=f(x,q)
        assert Q(j-1)<y<Q(j) if j>0 else Q(-1)<y<Q(0)
        for i in range(j):y=f(y,q)
        assert Q(-1)<y<Q(0),(q,j,y)
        count+=1
    assert Q(q*q-1,12)/Q((q+1)**3,8)==Q(2*(q-1),3*(q+1)**2)
    count+=1
for q in (10,20,40,80):
    for s in (-1.0,0.0,1.0):
        lam=pressure_root(q,s)
        assert 1<lam<=1+exp(s)
        if q>=40:assert abs(lam-(1+exp(s)))<0.003,(q,s,lam)
        count+=1
print('VERIFY_OK exact_matrix_and_return_checks=',count,'q_integers=3..9 pressure_q=10,20,40,80')
