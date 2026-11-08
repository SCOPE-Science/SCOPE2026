#!/usr/bin/env python3
"""Independent exact quotient and genus-two Cartier calculations.

The genus-two equation follows from the displayed involution; this script
verifies the Laurent identity and its characteristic-seven Hasse determinant.
"""

def la_add(A,B):
    C=A.copy()
    for k,v in B.items(): C[k]=C.get(k,0)+v
    return {k:v for k,v in C.items() if v}

def la_mul(A,B):
    C={}
    for i,x in A.items():
        for j,y in B.items(): C[i+j]=C.get(i+j,0)+x*y
    return {k:v for k,v in C.items() if v}

def la_pow(A,n):
    out={0:1}
    for _ in range(n):out=la_mul(out,A)
    return out

X={1:1}; Xi={-1:1}; U=la_add(X,Xi)
S5=la_add(la_add(la_pow(U,5),{k:-5*v for k,v in la_pow(U,3).items()}),{k:5*v for k,v in U.items()})
assert S5=={5:1,-5:1},S5
# Involution r: x -> x^-1; y -> y/x^5.
# v=y(x+1)/x^3 is invariant because (x^-1+1)/(x^-3*x^5)=(x+1)/x^3.
# Cross-multiply the quotient square identity by x^6 and compare Laurent coefficients.
for a in (0,1,3,-2):
    lhs=la_mul(la_add(la_add({10:1},{5:a}),{0:1}),la_pow(la_add(X,{0:1}),2))
    rhs=la_mul({6:1},la_mul(la_add(U,{0:2}),la_add(S5,{0:a})))
    assert lhs==rhs,(a,lhs,rhs)

# Independent polynomial arithmetic in F_7[a,u].
# Monomial (i,j) denotes a^i*u^j.
def add(A,B):
    c=A.copy()
    for k,v in B.items():c[k]=(c.get(k,0)+v)%7
    return {k:v for k,v in c.items() if v}

def mul(A,B):
    c={}
    for (i,j),x in A.items():
        for (ii,jj),y in B.items():c[(i+ii,j+jj)]=(c.get((i+ii,j+jj),0)+x*y)%7
    return {k:v for k,v in c.items() if v}

def power(A,n):
    v={(0,0):1}
    for _ in range(n):v=mul(v,A)
    return v

f=add({(0,5):1,(0,3):-5,(0,1):5,(1,0):1},{})
d=mul(add({(0,1):1},{(0,0):2}),f)
d3=power(d,3)
def coeff_x(e):return {i:v for (i,j),v in d3.items() if j==e}
B=[[coeff_x(i*7-j) for j in (1,2)] for i in (1,2)]
assert B[0][0]=={1:3},B
assert B[1][0]=={1:3},B
assert B[1][1]=={1:4},B

def mul_a(A,B):
    out={}
    for i,x in A.items():
        for j,y in B.items():out[i+j]=(out.get(i+j,0)+x*y)%7
    return {i:v for i,v in out.items() if v}

def sub_a(A,B):
    return {i:v for i,v in add({(j,0):u for j,u in A.items()},{(j,0):-u for j,u in B.items()}).items() if i[1]==0 for i,v in [(i[0],v)]}

det=sub_a(mul_a(B[0][0],B[1][1]),mul_a(B[0][1],B[1][0]))
assert det=={1:2,3:2},det
print('PASS: involution quotient identity and genus-two determinant 2a(a^2+1)')
