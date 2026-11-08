#!/usr/bin/env python3
"""Independent finite-degree checks for two polynomial derivations.
No finite check substitutes for the symbolic proof.
"""
from collections import defaultdict

def add(a,b,p):
    d=defaultdict(int,a)
    for m,c in b.items():d[m]=(d[m]+c)%p
    return {m:c%p for m,c in d.items() if c%p}

def scale(a,s,p): return {m:(s*c)%p for m,c in a.items() if (s*c)%p}

def mon(a,b):return {(a,b):1}

def deriv(poly,p,which):
    out=defaultdict(int)
    for (a,b),c in poly.items():
        if which=='D' and b:
            k=(a+p+1,b-1);out[k]=(out[k]+c*b)%p
        elif which=='E' and a:
            k=(a-1,b+p+1);out[k]=(out[k]+c*a)%p
    return {x:y for x,y in out.items() if y}

def apply(poly,word,p):
    for w in word[::-1]:poly=deriv(poly,p,w)
    return poly

def lin(poly,p,i,j,kind):
    # D_i,E_i,H_i as explicit polynomial vector fields
    res=defaultdict(int)
    for (a,b),c in poly.items():
        t=i+j # ignored
        if kind=='D' and b:
            key=(a+p*(i+1)+1,b+p*i-1)
            res[key]=(res[key]+c*b)%p
        if kind=='E' and a:
            key=(a+p*j-1,b+p*(j+1)+1)
            res[key]=(res[key]+c*a)%p
    return {k:v for k,v in res.items() if v}

def act_basis(poly,p,name,i):
    # D_i = (x^py^p)^i D; E_i same; H_i=(x^py^p)^(i+1)(x d_x - y d_y)
    out=defaultdict(int)
    for (a,b),c in poly.items():
        if name=='D' and b:
            key=(a+p*(i+1)+1,b+p*i-1)
            out[key]=(out[key]+c*b)%p
        if name=='E' and a:
            key=(a+p*i-1,b+p*(i+1)+1)
            out[key]=(out[key]+c*a)%p
        if name=='H' and (a-b)%p:
            key=(a+p*(i+1),b+p*(i+1))
            out[key]=(out[key]+c*(a-b))%p
    return {k:v for k,v in out.items() if v}

def comm_test(p,name1,i,name2,j,target,ind,coeff):
    for a in range(4):
      for b in range(4):
        f=mon(a,b)
        lhs=add(act_basis(act_basis(f,p,name2,j),p,name1,i),scale(act_basis(act_basis(f,p,name1,i),p,name2,j),-1,p),p)
        rhs=scale(act_basis(f,p,target,ind),coeff,p) if target else {}
        assert lhs==rhs,(p,name1,i,name2,j,a,b,lhs,rhs)

checks=0
for p in [2,3,5,7]:
  # Individual generators vanish to p-th power on tested monomials
  for a in range(9):
    for b in range(9):
      f=mon(a,b)
      for letter in ['D','E']:
        assert apply(f,letter*p,p)=={}
        checks+=1
  for n in range(1,13):
    f=mon(1,0)
    lhs=apply(f,'DE'*n,p)
    rhs=mon(1+p*n,p*n)
    assert lhs==rhs,(p,n,lhs,rhs)
    checks+=1
  for i in range(4):
    for j in range(4):
      comm_test(p,'D',i,'E',j,'H',i+j,1);checks+=1
      comm_test(p,'H',i,'D',j,'D',i+j+1,2);checks+=1
      comm_test(p,'H',i,'E',j,'E',i+j+1,-2);checks+=1
      comm_test(p,'D',i,'D',j,None,0,0);checks+=1
      comm_test(p,'E',i,'E',j,None,0,0);checks+=1
      comm_test(p,'H',i,'H',j,None,0,0);checks+=1
  if p==2:
    # Verify the Clifford-type defining relations on test monomials.
    for a in range(7):
      for b in range(7):
        f=mon(a,b)
        # H = DE+ED
        assert act_basis(f,p,'H',0)==add(apply(f,'DE',p),apply(f,'ED',p),p)
        # D/E commute with H
        assert add(act_basis(apply(f,'D',p),p,'H',0),act_basis(act_basis(f,p,'H',0),p,'D',0),p)=={}
        assert add(act_basis(apply(f,'E',p),p,'H',0),act_basis(act_basis(f,p,'H',0),p,'E',0),p)=={}
        checks+=3
print(f'VERIFY_OK primes=2,3,5,7 checks={checks} nilpotent=yes iterates=yes lie_brackets=yes char2_relations=yes')
