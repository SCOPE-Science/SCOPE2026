#!/usr/bin/env python3
"""Exact projective orbit and geometric smoothness for the extremal cubic."""
from collections import deque
from pathlib import Path

E=[(a,b,c,3-a-b-c) for a in range(4)
   for b in range(4-a) for c in range(4-a-b)]
index={e:j for j,e in enumerate(E)}
assert len(E)==20
REP=67194

def toggle(S,x):
    if x in S:S.remove(x)
    else:S.add(x)

def poly_multiply(A,B):
    out=set()
    for e in A:
        for h in B:
            toggle(out,tuple(x+y for x,y in zip(e,h)))
    return out

def substitution(row_images):
    powers=[{tuple(int(i==j) for i in range(4))
             for j in range(4) if row_images[k]&(1<<j)} for k in range(4)]
    images=[]
    for mon in E:
        p={(0,0,0,0)}
        for k in range(4):
            for _ in range(mon[k]):p=poly_multiply(p,powers[k])
        v=0
        for e in p:v ^= 1<<index[e]
        images.append(v)
    return images

def transform(mask, images):
    out=0
    while mask:
        b=mask&-mask
        out ^= images[b.bit_length()-1]
        mask ^= b
    return out

# Adjacent transpositions plus one elementary transvection generate GL4(F2).
G=[]
rows=(1,2,4,8)
for i in range(3):
    r=list(rows);r[i],r[i+1]=r[i+1],r[i]
    G.append(tuple(r))
G.append((3,2,4,8))
images=[substitution(g) for g in G]

def left(g,m):
    result=[]
    for row in g:
        v=0
        for i in range(4):
            if row&(1<<i):v ^= m[i]
        result.append(v)
    return tuple(result)

matrices={rows};todo=deque([rows])
while todo:
    m=todo.popleft()
    for g in G:
        n=left(g,m)
        if n not in matrices:matrices.add(n);todo.append(n)
assert len(matrices)==20160
orbits={REP}; todo=deque([REP])
while todo:
    f=todo.popleft()
    for g in images:
        n=transform(f,g)
        if n not in orbits:orbits.add(n);todo.append(n)
cert={int(z) for z in Path('extremal_coefficients.txt').read_text().splitlines()}
assert len(orbits)==840 and orbits==cert
assert min(orbits)==REP
# Direct geometric smoothness proof for REP: in characteristic two,
# dF/dX0 = X3^2. At any projective singular point X3=0.
# Then dF/dX2 = X2^2, so X2=0;
# then dF/dX1 = X1^2, so X1=0;
# then dF/dX3 = X0^2, so X0=0, impossible.
# Verify the four derivatives symbolically, reducing coefficients mod 2.
from sympy import symbols,diff,Poly,GF
X=symbols('X0:4')
F=sum((__import__('functools').reduce(lambda p,x:p*x,
           (X[i]**e[i] for i in range(4)),1)
           for j,e in enumerate(E) if REP&(1<<j)))
def mod2(x):return Poly(x,*X,modulus=2).as_expr()
d=[mod2(diff(F,xi)) for xi in X]
expected=[X[3]**2,
  X[1]**2+X[2]**2+X[2]*X[3]+X[3]**2,
  X[1]*X[3]+X[2]**2+X[3]**2,
  X[0]**2+X[1]*X[2]]
assert all(mod2(a-b)==0 for a,b in zip(d,expected))
print('group size',len(matrices))
print('orbit size',len(orbits))
print('stabilizer size',len(matrices)//len(orbits))
print('orbit equals exhaustive extremal set',True)
print('representative coefficient mask',REP)
print('representative polynomial',F)
print('geometric smoothness derivative triangular certificate',True)
