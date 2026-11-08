#!/usr/bin/env python3
"""Exact rational regression checks for the noisy row-projection invariant-law theorem.

The general all-dimension assertion is established analytically in RESULT.md;
these finite checks verify the illustrative covariance formulas and graph examples.
No external dependencies are required.
"""
from fractions import Fraction as F
from itertools import product

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def add(A,B):
    return [[a+b for a,b in zip(row,col)] for row,col in zip(A,B)]

def scale(a,A):
    return [[a*b for b in row] for row in A]

def outer(u):
    return [[a*b for b in u] for a in u]

def transpose(A):
    return [list(x) for x in zip(*A)]

def project(u):
    return add([[F(i==j) for j in range(len(u))] for i in range(len(u))],scale(F(-1),outer(u)))

def gaussian_update(u,sigma2,S):
    P=project(u)
    return add(matmul(matmul(P,S),transpose(P)),scale(sigma2,outer(u)))

def dot(u,v):
    return sum(a*b for a,b in zip(u,v))

checks=0
u=[F(1), F(0)]
w=[F(3,5),F(4,5)]
v=[F(0),F(1)]
z=[F(-4,5),F(3,5)]
assert dot(u,u)==dot(w,w)==dot(v,v)==dot(z,z)==1
assert dot(u,v)==dot(w,z)==0
checks+=6

for sig1,sig2 in product([F(1,4),F(1),F(4),F(9)],repeat=2):
    c2=dot(u,w)**2
    A=(sig2+c2*sig1)/(1+c2)
    B=(sig1+c2*sig2)/(1+c2)
    C1=add(scale(sig1,outer(u)),scale(A,outer(v)))
    C2=add(scale(sig2,outer(w)),scale(B,outer(z)))
    for C in (C1,C2):
        assert gaussian_update(u,sig1,C)==C1
        assert gaussian_update(w,sig2,C)==C2
        checks+=2
    for prob in [F(1,7),F(1,2),F(6,7)]:
        S=add(scale(prob,C1),scale(1-prob,C2))
        out=add(scale(prob,gaussian_update(u,sig1,S)),scale(1-prob,gaussian_update(w,sig2,S)))
        assert out==S
        checks+=1
    if sig1==sig2:
        assert C1==C2==[[sig1,F(0)],[F(0),sig1]]
        checks+=1

sig1,sig2=F(1),F(4)
c2=F(9,25)
A=(sig2+c2*sig1)/(1+c2)
B=(sig1+c2*sig2)/(1+c2)
C1=add(scale(sig1,outer(u)),scale(A,outer(v)))
C2=add(scale(sig2,outer(w)),scale(B,outer(z)))
assert A==F(109,34) and B==F(61,34)
assert C1==[[F(1),F(0)],[F(0),F(109,34)]]
assert C2==[[F(44,17),F(18,17)],[F(18,17),F(109,34)]]
checks+=4
p=F(1,2)
v1,v2=C1[0][0],C2[0][0]
variance=p*v1+(1-p)*v2
k4=3*(p*v1*v1+(1-p)*v2*v2-variance*variance)
assert variance==F(61,34)
assert k4==F(2187,1156)
assert k4/variance**2==F(2187,3721)
checks+=3

# Three normalized rows: the graph is connected through the third row.
rows=[u,v,w]
sigmas=[F(1),F(1),F(4)]
edges={(i,j) for i in range(3) for j in range(i+1,3) if dot(rows[i],rows[j])!=0}
assert edges=={(0,2),(1,2)}
assert sigmas[0]!=sigmas[2]
checks+=2

# Orthogonal case: heterogeneous noise still supports a Gaussian stationary law.
D=[[F(1),F(0)],[F(0),F(4)]]
assert gaussian_update(u,F(1),D)==D
assert gaussian_update(v,F(4),D)==D
checks+=2
print('PASS:',checks,'exact rational assertions')
print('two-row first-variance =',variance,'; fourth cumulant =',k4)
print('3-row nonorthogonality edges:',sorted(edges))

# Exact stationary 2nd- and 4th-order moments for a three-row overcomplete
# example. The linear moment equations are solved over the rationals.
def solve_linear(A,b):
    n=len(b)
    aug=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        k=next(i for i in range(j,n) if aug[i][j])
        aug[j],aug[k]=aug[k],aug[j]
        z=aug[j][j]
        aug[j]=[v/z for v in aug[j]]
        for i in range(n):
            if i!=j:
                z=aug[i][j]
                aug[i]=[a-z*b for a,b in zip(aug[i],aug[j])]
    return [row[-1] for row in aug]

def pmul(A,B):
    C={}
    for a,x in A.items():
        for b,y in B.items():
            k=tuple(i+j for i,j in zip(a,b))
            C[k]=C.get(k,F(0))+x*y
    return C

def ppow(P,n):
    out={(0,0,0):F(1)}
    for _ in range(n):out=pmul(out,P)
    return out

def expectation_polynomial(P,degree,known):
    # Output coefficients of unknown moments plus known constant.
    if degree==2: order=[(2,0),(1,1),(0,2)]
    else: order=[(4,0),(3,1),(2,2),(1,3),(0,4)]
    result=[]
    for a,b in order:
        total=F(0)
        coeff=[F(0)]*len(order)
        for u,sig in zip(P[0],P[1]):
            R=project(u)
            xp={(1,0,0):R[0][0],(0,1,0):R[0][1],(0,0,1):u[0]}
            yp={(1,0,0):R[1][0],(0,1,0):R[1][1],(0,0,1):u[1]}
            for (x,y,e),num in pmul(ppow(xp,a),ppow(yp,b)).items():
                if e%2: continue
                en={0:F(1),2:sig,4:3*sig*sig}[e]
                val=num*en/len(P[0])
                if (x,y) in order: coeff[order.index((x,y))]+=val
                else: total+=val*known[(x,y)]
        result.append((coeff,total))
    return order,result

rows3=[u,v,w]
sig3=[F(1),F(1),F(4)]
_,sys2=expectation_polynomial((rows3,sig3),2,{(0,0):F(1)})
M2=solve_linear([[F(i==j)-r[0][j] for j in range(3)] for i,r in enumerate(sys2)], [r[1] for r in sys2])
assert M2==[F(2405,1442),F(300,721),F(1465,721)]
checks+=3
m2={(2,0):M2[0],(1,1):M2[1],(0,2):M2[2],(0,0):F(1)}
_,sys4=expectation_polynomial((rows3,sig3),4,m2)
M4=solve_linear([[F(i==j)-r[0][j] for j in range(5)] for i,r in enumerate(sys4)],[r[1] for r in sys4])
assert M4[0]==F(7011019779,716387042)
assert M4[-1]==F(5592527427,358193521)
checks+=2
fourth_cumulant=M4[0]-3*M2[0]**2
assert fourth_cumulant==F(1489362309243,1033030114564)
assert fourth_cumulant>F(927369,1039682)
checks+=2
print('PASS:',checks,'total exact rational assertions')
print('3-row stationary e1 fourth cumulant:',fourth_cumulant)
