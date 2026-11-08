"""Checks for the Euclidean inball of Cayley sums of coordinate boxes.

Run: python verify_cayley.py
Requires numpy and scipy. Exact geometric deductions are given in RESULT.md.
"""
import math
import random
import numpy as np
from scipy.optimize import linprog


def matrix_radii(A):
    m = len(A)
    d = len(A[0]) - 1
    r0 = 1.0 / (d + math.sqrt(d))
    rows = []
    for row in A:
        h = math.sqrt(1 + sum((row[j]-row[0])**2 for j in range(1,d+1)))
        b = row[0]*math.sqrt(d) + sum(row[1:])
        rows.append((h,b,(b-h-1)*r0))
    return r0,rows


def exact_lp(A):
    m = len(A)
    d = len(A[0])-1
    # Unknowns x_1..x_m, y_1..y_d, r.
    N = m+d+1
    U=[];v=[]
    for j in range(d):
        a=np.zeros(N);a[m+j]=-1;a[-1]=1
        U.append(a);v.append(0)
    a=np.zeros(N);a[m:m+d]=1;a[-1]=math.sqrt(d)
    U.append(a);v.append(1)
    for i,row in enumerate(A):
        a=np.zeros(N);a[i]=-1;a[-1]=1
        U.append(a);v.append(0)
        a=np.zeros(N);a[i]=1
        for j in range(d):a[m+j]=row[0]-row[j+1]
        h=math.sqrt(1+sum((row[j+1]-row[0])**2 for j in range(d)))
        a[-1]=h
        U.append(a);v.append(row[0])
    c=np.zeros(N);c[-1]=-1
    return linprog(c,A_ub=U,b_ub=v,bounds=[(None,None)]*N,method='highs')


test_count = 0

def check(value, message=""):
    global test_count
    test_count += 1
    if not value:
        raise AssertionError(message)

def verify():
    rng=random.Random(601991)
    checks=0
    cases=0
    # General matrices, including saturating and nonsaturating examples.
    for d in range(1,5):
        for m in range(1,5):
            for t in range(70):
                A=[]
                for i in range(m):
                    row=[rng.randrange(5) for _ in range(d+1)]
                    if not any(row):row[0]=1
                    A.append(row)
                r0,rows=matrix_radii(A)
                ans=exact_lp(A)
                check(ans.success, (d,m,A,ans.message))
                pred=min((b-h-1 for h,b,_ in rows))>=-1e-10
                if pred:
                    check(abs(ans.x[-1]-r0)<2e-8, (d,m,A,ans.x[-1],r0))
                    # Midpoint of every predicted center interval is feasible.
                    xmid=[r0+(b-h-1)*r0/2 for h,b,_ in rows]
                    y=[r0]*d
                    check(min(xmid)>=r0-1e-10)
                    for i,row in enumerate(A):
                        h,b,_=rows[i]
                        cap=row[0]*(1-d*r0)+sum(row[j+1]*r0 for j in range(d))
                        check(cap-xmid[i]>=r0*h-1e-10)
                        checks+=2
                else:
                    check(ans.x[-1]<r0-1e-8, (d,m,A,ans.x[-1],r0))
                cases+=1;checks+=3
    # Integer two-parameter Ferroni family. Degenerate only (alpha,beta)=(1,1).
    for d in range(1,32):
        for alpha in range(1,12):
            for beta in range(1,12):
                A=[[alpha]+[beta if i==j else 0 for j in range(d)] for i in range(d)]
                r0,rows=matrix_radii(A)
                norm=math.sqrt(1+(beta-alpha)**2+(d-1)*alpha*alpha)
                ell=(alpha*math.sqrt(d)+beta-norm-1)*r0
                check(abs(rows[0][2]-ell)<1e-10)
                check(ell>=-1e-10)
                check((ell<1e-10)==(alpha==1 and beta==1), (d,alpha,beta,ell))
                # Symbolically rationalized strict positivity numerator:
                # (alpha sqrt(d)+beta-1)^2 - M^2
                rhs=2*(alpha*math.sqrt(d)*(beta-1)+beta*(alpha-1))
                lhs=(alpha*math.sqrt(d)+beta-1)**2-norm**2
                check(abs(lhs-rhs)<1e-8)
                checks+=4
    print(f"PASS: {cases} independent LPs, {test_count} assertions; sparse parameter formula checked through d=31.")

if __name__=='__main__':verify()
