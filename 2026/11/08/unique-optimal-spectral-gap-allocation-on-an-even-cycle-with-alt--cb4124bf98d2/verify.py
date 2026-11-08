"""Exact finite checks for the period-two priced cycle theorem.

Only the cases with rational cosine (m=2,3) are checked exactly here;
the proof for all m is analytic and independent of this file.
"""
from fractions import Fraction as Q
from itertools import combinations

def det(A):
    A=[list(map(Q,row)) for row in A]; n=len(A); d=Q(1)
    for i in range(n):
        pivot=next((j for j in range(i,n) if A[j][i]),None)
        if pivot is None:return Q(0)
        if pivot!=i: A[i],A[pivot]=A[pivot],A[i];d=-d
        t=A[i][i];d*=t
        for j in range(i+1,n):
            z=A[j][i]/t
            for k in range(i+1,n):A[j][k]-=z*A[i][k]
            A[j][i]=0
    return d

def construct(m,sa,sb,B):
    assert m in (2,3) and sa>0 and sb>0 and B>0
    ca,cb=sa*sa,sb*sb
    gamma=Q(0) if m==2 else Q(1,2)
    s2=1-gamma*gamma
    D=ca+cb+2*gamma*sa*sb
    lam=2*B*s2/(m*D)
    a=B*(1+gamma*sb/sa)/(m*D)
    b=B*(1+gamma*sa/sb)/(m*D)
    assert m*(ca*a+cb*b)==B
    assert lam*(2*(a+b)-lam)==4*a*b*s2
    if m==2:
        da2=4*ca/(ca+cb);db2=4*cb/(ca+cb)
    else:
        R=a+b-lam
        ck=2*gamma*gamma-1
        assert R*R==a*a+b*b+2*a*b*ck
        da2=2*(1-(a+b*ck)/R)
        db2=2*(1-(b+a*ck)/R)
    assert da2*cb==db2*ca
    assert (a*da2+b*db2)/2==lam
    n=2*m
    L=[[Q(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        j=(i+1)%n;w=a if i%2==0 else b
        L[i][i]+=w;L[j][j]+=w;L[i][j]-=w;L[j][i]-=w
    # L - lambda (I-J/n) positive semidefinite iff all principal minors nonnegative.
    H=[[L[i][j]-lam*((i==j)-Q(1,n)) for j in range(n)] for i in range(n)]
    cnt=0
    for r in range(1,n+1):
        for idx in combinations(range(n),r):
            d=det([[H[i][j] for j in idx] for i in idx]);assert d>=0,(m,sa,sb,B,idx,d)
            cnt+=1
    return cnt

def main():
    total=0
    for m in (2,3):
        for sa in (Q(1),Q(2),Q(3),Q(5,2)):
            for sb in (Q(1),Q(2),Q(4,3)):
                for B in (Q(1),Q(7,3)):
                    total+=construct(m,sa,sb,B)
    assert total==24*(15+63)
    print('EXACT_VERIFY_OK', 'parameter_cases=48','principal_minors='+str(total), 'dual_energy_checks=48')

if __name__=='__main__':main()
