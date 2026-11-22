#!/usr/bin/env python3
"""Exact certificate for a Picard-family 13-rank stratum (sympy + Python integers).
Run with python verify.py; no external data files are required.
"""
from sympy import symbols, Poly, discriminant

p=13
assert all((i*i)%p != 8 for i in range(p))
x,a,b=symbols('x a b')
f=x**4+a*x**2+b*x+1

def reduce13(expr):
    return Poly(expr,a,b,modulus=p).as_expr()

def coefficient(power,exp):
    F=Poly(f**power,x,a,b,modulus=p)
    terms={(e[1],e[2]):int(c)%p for e,c in F.terms() if e[0]==exp}
    return Poly.from_dict(terms,(a,b),modulus=p).as_expr() if terms else 0

h=coefficient(4,12)
B=[[coefficient(8,12), coefficient(8,11)],
   [coefficient(8,25), coefficient(8,24)]]
Delta=reduce13(discriminant(f,x))
assert reduce13(h-(6*a*a+4))==0
assert reduce13(B[0][0]*B[1][1]-B[0][1]*B[1][0] - 4*(a*a+5)*Delta**2)==0

# F_169 = F_13[u]/(u^2-8); represent c+d*u as (c,d).
zero=(0,0);one=(1,0);u=(0,1)
def add(v,w):return ((v[0]+w[0])%p,(v[1]+w[1])%p)
def sub(v,w):return ((v[0]-w[0])%p,(v[1]-w[1])%p)
def mul(v,w):return ((v[0]*w[0]+8*v[1]*w[1])%p,(v[0]*w[1]+v[1]*w[0])%p)
def inv(v):
    norm=(v[0]**2-8*v[1]**2)%p
    assert norm!=0
    k=pow(norm,-1,p)
    return ((v[0]*k)%p,(-v[1]*k)%p)
def trim(V):
    V=list(V)
    while V and V[-1]==zero:V.pop()
    return V

def to_poly(expr):
    F=Poly(expr,a,b,modulus=p)
    deg=F.degree(b)
    if deg < 0:return []
    V=[zero]*(deg+1)
    for (i,j),v in F.terms():
        assert i>=0
        if i%2: V[j]=add(V[j],(0,(int(v)*pow(8,i//2,p))%p))
        else:V[j]=add(V[j],((int(v)*pow(8,i//2,p))%p,0))
    return trim(V)

def padd(V,W):
    n=max(len(V),len(W))
    return trim([add(V[i] if i<len(V) else zero, W[i] if i<len(W) else zero) for i in range(n)])

def pmul(V,W):
    if not V or not W:return []
    U=[zero]*(len(V)+len(W)-1)
    for i,v in enumerate(V):
        if v==zero:continue
        for j,w in enumerate(W): U[i+j]=add(U[i+j],mul(v,w))
    return trim(U)

def pdiv(V,W):
    assert W
    V=trim(V)
    Q=[zero]*max(0,len(V)-len(W)+1)
    while len(V)>=len(W):
        d=len(V)-len(W)
        q=mul(V[-1],inv(W[-1]));Q[d]=q
        for j,w in enumerate(W): V[d+j]=sub(V[d+j],mul(q,w))
        V=trim(V)
    return trim(Q),V

def pmod(V,W):return pdiv(V,W)[1]
def pgcd(V,W):
    while W:V,W=W,pmod(V,W)
    if V:V=[mul(v,inv(V[-1])) for v in V]
    return trim(V)
def derivative(V):return trim([mul((i,0),V[i]) for i in range(1,len(V))])
def powmod(V,n,mod):
    Z=[one]
    while n:
        if n&1:Z=pmod(pmul(Z,V),mod)
        V=pmod(pmul(V,V),mod);n//=2
    return Z

def pfrob(V):
    if not V:return []
    W=[zero]*(13*(len(V)-1)+1)
    for i,(c,d) in enumerate(V):W[13*i]=(c,(-d)%p)
    return trim(W)

M=[[to_poly(v) for v in row] for row in B]
M_exp=[[to_poly(a*(4*b**6+2*b**2)-2*b**4), to_poly(a*(4*b**5-b)-5*b**7+5*b**3)],
       [to_poly(-4*b),to_poly(-a*b**2+2)]]
assert M==M_exp
# Frob^13 followed by the original 2-dimensional Hasse-Witt block.
Mp=[[pfrob(v) for v in row] for row in M]
P=[[padd(pmul(Mp[i][0],M[0][j]), pmul(Mp[i][1],M[1][j]))
    for j in range(2)] for i in range(2)]
G=P[0][0]
for row in P:
    for entry in row:G=pgcd(G,entry)

D=to_poly(9+8*a*b*b-b**4)
assert D==to_poly(Delta)
Q=to_poly(b**18+3*a*b**16+7*b**14+7*a*b**12+2*b**10+6*a*b**8+4*b**6+2*a*b**4+7*b**2-a)
assert len(Q)==19
assert G==pmul(pmul(D,D),Q)
assert pgcd(Q,D)==[one]
assert pgcd(Q,derivative(Q))==[one]
assert Q[0]==(0,12)

# Irreducible factor-degree profile over F_169 via squarefree Frobenius gcd.
X=[zero,one]
Xd=X
fixed={}
for d in range(1,7):
    Xd=powmod(Xd,169,Q)
    diff=Xd+[zero]*max(0,2-len(Xd));diff[1]=sub(diff[1],one)
    fixed[d]=len(pgcd(Q,trim(diff)))-1
assert fixed=={1:0,2:6,3:0,4:6,5:0,6:18},fixed

print('VERIFY_OK')
print('Hasse determinant = 4(a^2+5)Delta^2 and h=6(a^2+5)')
print('On a^2=8, gcd entries of B^[13] B = Delta^2 Q, deg Q=18')
print('Q squarefree, coprime to Delta; rank-zero geometric points=36')
print('Factor degrees over F_169: 2^3 6^2; over F_13: 4^3 12^2')
