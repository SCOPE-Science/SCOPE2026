"""Exact rational verification of the three-step Ferrers root-polytope sphere formula.

Python standard library only. Every output is a finite check, not an infinite proof.
"""
from fractions import Fraction as F
from itertools import product


def solve(a, b):
    a = tuple(map(F, a)); b = tuple(map(F, b))
    A, B = sum(a), sum(b)
    d1 = a[2]/A - b[0]/B
    d2 = (a[1]+a[2])/A - (b[0]+b[1])/B
    k11 = a[2]*(a[0]+a[1])/A + b[0]*(b[1]+b[2])/B
    k22 = (a[1]+a[2])*a[0]/A + (b[0]+b[1])*b[2]/B
    k12 = a[2]*a[0]/A + b[0]*b[2]/B
    det = k11*k22-k12*k12
    assert det > 0
    if d1 <= 0 and d2 <= 0:
        l1=l2=F(0)
    elif d1 > 0 and d2 <= k12*d1/k11:
        l1,l2=d1/k11,F(0)
    elif d2 > 0 and d1 <= k12*d2/k22:
        l1,l2=F(0),d2/k22
    else:
        l1,l2=(k22*d1-k12*d2)/det, (k11*d2-k12*d1)/det
    assert l1>=0 and l2>=0
    assert d1-k11*l1-k12*l2<=0 and d2-k12*l1-k22*l2<=0
    assert l1*(d1-k11*l1-k12*l2)==0 and l2*(d2-k12*l1-k22*l2)==0
    U = [1/A-l1*(F(i==2)-a[2]/A)-l2*(F(i>=1)-(a[1]+a[2])/A) for i in range(3)]
    V = [1/B+l1*(F(j==0)-b[0]/B)+l2*(F(j<=1)-(b[0]+b[1])/B) for j in range(3)]
    assert min(U)>0 and min(V)>0
    norm = sum(a[i]*U[i]**2 for i in range(3))+sum(b[j]*V[j]**2 for j in range(3))
    expected = 1/A+1/B+l1*(k11*l1+k12*l2)+l2*(k12*l1+k22*l2)
    assert norm == expected
    radius = 2-expected
    assert sum(a[i]*U[i] for i in range(3))==1
    assert sum(b[j]*V[j] for j in range(3))==1
    # All edge-vertex squared distances agree with the predicted clearance.
    contacts=[]
    for i in range(3):
        for j in range(3-i):
            actual = radius-(2-2*(U[i]+V[j])+norm)
            prediction=2*(l1*F(j==0 and i<2)+l2*F(i==0 and j<2))
            assert actual==prediction,(a,b,i,j,actual,prediction)
            if actual==0: contacts.append((i+1,j+1))
    assert contacts
    # Stationarity: contact edges attain the minimum inner product.
    minimum=min(U[i]+V[j] for i in range(3) for j in range(3-i))
    assert minimum==norm
    return l1,l2,radius,contacts


def run():
    count=0
    regimes=set()
    for a in product(range(1,5),repeat=3):
        for b in product(range(1,5),repeat=3):
            l1,l2,r,contacts=solve(a,b)
            count+=1
            regimes.add((l1>0,l2>0))
    assert count==4096 and len(regimes)==4
    a=(1,1,1); b=(1,2,3)
    l1,l2,R,contacts=solve(a,b)
    assert (l1,l2,R)==(F(2,23),F(1,23),F(34,23)),(l1,l2,R)
    assert contacts==[(1,3),(2,2),(3,1)]
    print('THREE_STEP_FERRERS_EXACT_PASS',count,'regimes',len(regimes))

if __name__=='__main__':run()
