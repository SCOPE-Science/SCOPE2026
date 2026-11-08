#!/usr/bin/env python3
"""Direct Jacobian rank test for the nilpotent commuting-triple quadratic scheme."""
from itertools import product

def rank(A,q):
    A=[[v%q for v in row] for row in A]
    r=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][c]),None)
        if pivot is None:continue
        A[r],A[pivot]=A[pivot],A[r]
        k=pow(A[r][c],-1,q)
        A[r]=[(v*k)%q for v in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                t=A[i][c]
                A[i]=[(a-t*b)%q for a,b in zip(A[i],A[r])]
        r+=1
    return r

def equations_jac(x,q,r):
    J=[]
    for i in range(r):
        a,b,c=x[i]; row=[0]*(3*r)
        row[3*i:3*i+3]=[2*a,c,b]
        J.append(row)
    for i in range(r):
        a,b,c=x[i]
        for j in range(i+1,r):
            d,e,f=x[j]
            row=[0]*(3*r);row[3*i:3*i+3]=[0,f,-e];row[3*j:3*j+3]=[0,-c,b];J.append(row)
            row=[0]*(3*r);row[3*i:3*i+3]=[e,-d,0];row[3*j:3*j+3]=[-b,a,0];J.append(row)
            row=[0]*(3*r);row[3*i:3*i+3]=[f,0,-d];row[3*j:3*j+3]=[-c,0,a];J.append(row)
    return J

def check(q,r):
    N=[(a,b,c) for a,b,c in product(range(q),repeat=3) if (a*a+b*c)%q==0]
    def comm(x,y):
        a,b,c=x;d,e,f=y
        return (b*f-c*e)%q==0 and (a*e-b*d)%q==0 and (a*f-c*d)%q==0
    points=(x for x in product(N,repeat=r) if all(comm(x[i],x[j]) for i in range(r) for j in range(i+1,r)))
    seen=0
    for x in points:
        actual=rank(equations_jac(x,q,r),q)
        expected=0 if all(z==(0,0,0) for z in x) else 2*r-1
        assert actual==expected, (x,actual,expected)
        seen+=1
    assert seen==1+(q+1)*(q**r-1),(q,r,seen)
    print('Jacobian q=%d r=%d points=%d expected_rank_nonzero=%d PASS'%(q,r,seen,2*r-1))
for q,r in ((3,2),(3,3),(5,2),(5,3)):
    check(q,r)
print('ALL_QUADRATIC_CONE_JACOBIAN_CHECKS_PASS')
