#!/usr/bin/env python3
"""Independent consistency checks of normalized two-row Monge inballs.
Scientific statement and proof are in RESULT.md. Requires scipy for LP comparisons.
"""
from fractions import Fraction
from math import sqrt
from itertools import product

assertions = 0

def ck(statement):
    global assertions
    assert statement
    assertions += 1

# Exact discrete extremizer inequalities and tangencies, scaled to r=1.
for m in range(2,51):
    deficit = m*m//2
    if m % 2:
        shifts = [Fraction(0)]
    else:
        shifts = [Fraction(-1),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(1)]
    for theta in shifts:
        ds = [Fraction(m+1-2*j)+theta for j in range(1,m+1)]
        x = [max(Fraction(0),-d) for d in ds]
        y = [max(Fraction(0),d) for d in ds]
        ck(sum(x)+sum(y)==deficit)
        for j in range(m):
            ck(x[j]>=0 and y[j]>=0)
            ck(y[j]-x[j]==ds[j])
        for j in range(m-1):
            ck((y[j]-x[j])-(y[j+1]-x[j+1])==2)
        zeros = sum(t==0 for t in x+y)
        if m%2:
            ck(zeros==m+1)
        else:
            ck(zeros==(m+1 if abs(theta)==1 else m))

# Direct finite enumeration in the reduced scalar LP: integer d_j, with adjacent gaps >=2.
# Exhaustive over a stated finite domain: this is NOT a proof for arbitrary real data.
for m in range(2,6):
    bound=m+2
    count=0
    for ds in product(range(-bound,bound+1), repeat=m):
        if any(ds[j]-ds[j+1]<2 for j in range(m-1)):
            continue
        count+=1
        ck(sum(abs(z) for z in ds)>=m*m//2)
    ck(count>0)

# Independent full-dimensional Chebyshev LP comparisons.
try:
    import numpy as np
    from scipy.optimize import linprog
except ImportError:
    print(f'PASS: {assertions} exact tests; scipy unavailable, numerical LP skipped')
else:
    for m in range(2,19):
        alpha=sqrt(1-1/(2*m))
        r_expected=1/(2*m*alpha + m*m//2)
        # (a_1,...,a_m,b_1,...,b_m,r), -a_j+alpha r<=0 etc.
        rows=[]; rhs=[]
        for k in range(2*m):
            row=[0.]*(2*m+1);row[k]=-1.;row[-1]=alpha
            rows.append(row);rhs.append(0.)
        for j in range(m-1):
            row=[0.]*(2*m+1)
            # a_j+b_(j+1)-a_(j+1)-b_j+2r<=0
            row[j]+=1;row[m+j+1]+=1;row[j+1]-=1;row[m+j]-=1;row[-1]+=2
            rows.append(row);rhs.append(0.)
        equality=[[1.]*(2*m)+[0.]]
        obj=[0.]*(2*m)+[-1.]
        sol=linprog(obj,A_ub=rows,b_ub=rhs,A_eq=equality,b_eq=[1.],bounds=[(None,None)]*(2*m+1),method='highs')
        ck(sol.success)
        ck(abs(sol.x[-1]-r_expected)<2e-8)
        ck(abs(sum(sol.x[:2*m])-1)<2e-8)
        # Probe optimal-face dimension through the first-column row difference
        last_bound=list(zip([None]*(2*m+1),[None]*(2*m+1)))
        last_bound[-1]=(r_expected-1.e-10,r_expected+1.e-10)
        vals=[]
        for sgn in (-1,1):
            obj=[0.]*(2*m+1)
            obj[0]=sgn;obj[m]=-sgn
            alt=linprog(obj,A_ub=rows,b_ub=rhs,A_eq=equality,b_eq=[1.],bounds=last_bound,method='highs')
            ck(alt.success)
            vals.append(alt.x[m]-alt.x[0])
        if m%2:
            ck(abs(vals[0]-vals[1])<1.e-7)
        else:
            ck(abs(abs(vals[0]-vals[1])-2*r_expected)<1.e-7)
    print(f'PASS: {assertions} exact/LP assertions, m=2..18 LP, m=2..50 exact')
