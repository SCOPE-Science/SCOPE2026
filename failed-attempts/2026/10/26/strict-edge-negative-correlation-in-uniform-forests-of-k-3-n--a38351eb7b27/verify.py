#!/usr/bin/env python3
"""Exact independent enumeration and identity checks for K_{3,n} uniform forests."""
from fractions import Fraction
from itertools import combinations

checks=0

def check(a,b,msg=''):
    global checks
    checks+=1
    if a!=b: raise AssertionError(f'{msg}: {a!r} != {b!r}')

def base(n):
    v=3*n*n+13*n+16
    u=3*n*n+23*n+38
    return v,u

def claimed(n):
    v,u=base(n)
    one=Fraction(u,4*v)
    joint=(Fraction(2*n+6,v),Fraction(3*n*n+33*n+66,16*v),Fraction(3*n*n+33*n+82,16*v))
    covariance=tuple(q-one*one for q in joint)
    return one,joint,covariance

def validate_enum(n):
    E=[(a,3+i) for i in range(n) for a in range(3)]
    m=len(E)
    Z=0; single=[0]*m; pair=[[0]*m for _ in range(m)]
    for mask in range(1<<m):
        parent=list(range(n+3))
        def find(x):
            while parent[x]!=x:
                x=parent[x]
            return x
        chosen=[]; forest=True
        for e,(u,v) in enumerate(E):
            if not mask>>e&1: continue
            u=find(u); v=find(v)
            if u==v:
                forest=False; break
            parent[u]=v
            chosen.append(e)
        if not forest: continue
        Z+=1
        for a in chosen: single[a]+=1
        for a,b in combinations(chosen,2): pair[a][b]+=1
    v,u=base(n)
    check(Z*16,4**n*v,f'Z n={n}')
    p,q,cov=claimed(n)
    for e in range(m): check(Fraction(single[e],Z),p,f'one n={n} edge={e}')
    for e in range(m):
      for f in range(e+1,m):
        leaf1,h1=divmod(e,3)
        leaf2,h2=divmod(f,3)
        typ=0 if leaf1==leaf2 else 1 if h1==h2 else 2
        check(Fraction(pair[e][f],Z),q[typ],f'pair n={n} {e},{f}')
        check(Fraction(pair[e][f],Z)-p*p,cov[typ],f'cov n={n} {e},{f}')
    return Z

def pmul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

def psub(a,b):
    return [(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))]

def pscale(a,c): return [c*x for x in a]

# Polynomial coefficient order: constant, linear, quadratic, ...
u=[38,23,3]
v=[16,13,3]
ws=[6,2]
w1=[66,33,3]
w2=[82,33,3]
identities=[
 (psub(pmul(u,u),pscale(pmul(ws,v),16)),[-92,-12,53,42,9]),
 (psub(pmul(u,u),pmul(w1,v)),[388,362,82,0,0]),
 (psub(pmul(u,u),pmul(w2,v)),[132,154,34,0,0])]
for obtained,expected in identities:check(obtained,expected,'polynomial Rayleigh difference')
for n in range(1,1001):
  p,j,c=claimed(n)
  check(c[0] <= 0, True, f'same leaf nonpositive {n}')
  if n>=2:
    check(c[0]<0,True,'same leaf strict')
    check(c[1]<0,True,'different leaf same hub strict')
    check(c[2]<0,True,'different leaf different hub strict')
for n in range(1,7):
  print(f'exhaustive K_{{3,{n}}}: {validate_enum(n)} forests')
print(f'PASS: {checks} exact assertions')
