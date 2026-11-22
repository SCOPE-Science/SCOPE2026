"""Exact independent rational Gram reconstruction for cubic spherical-gradient sampling.
Run: python3 check_cubic_gradient.py
"""
from fractions import Fraction as F
from itertools import combinations
from math import prod, factorial

def add(*ps):
 o={}
 for p in ps:
  for k,v in p.items():o[k]=o.get(k,F(0))+v
 return {k:v for k,v in o.items() if v}

def term(d, coeff, inds):
 es=[0]*d
 for i in inds:es[i]+=1
 return {tuple(es):F(coeff)}

def mul(a,b):
 o={}
 for x,v in a.items():
  for y,w in b.items():
   z=tuple(i+j for i,j in zip(x,y))
   o[z]=o.get(z,F(0))+v*w
 return {k:v for k,v in o.items() if v}

def deriv(p,j):
 o={}
 for e,v in p.items():
  if e[j]:
   a=list(e);a[j]-=1
   a=tuple(a)
   o[a]=o.get(a,F(0))+v*e[j]
 return o

def sphere_monomial(e):
 if any(k%2 for k in e):return F(0)
 d=len(e); m=sum(e)//2
 num=prod(prod(range(1,k,2)) for k in e)
 den=prod(d+2*i for i in range(m))
 return F(num,den)

def expectation(p,kind):
 if kind=='sphere':return sum(v*sphere_monomial(e) for e,v in p.items())
 return sum(v for e,v in p.items() if all(k%2==0 for k in e))

def basis(d):
 r=[]
 for i in range(d):
  r2=add(*(term(d,1,[j,j]) for j in range(d)))
  pi=add(term(d,1,[i,i,i]),{k:-F(3,d+2)*v for k,v in mul(term(d,1,[i]),r2).items()})
  r.append(('zonal'+str(i),pi,0))
 for i in range(d):
  others=[j for j in range(d) if j!=i]
  base=others[-1]
  for j in others[:-1]:
   p=add(term(d,1,[i,j,j]),term(d,-1,[i,base,base]))
   r.append(('transverse'+str(i)+'_'+str(j),p,1))
 for i,j,k in combinations(range(d),3):
  r.append(('squarefree'+str(i)+'_'+str(j)+'_'+str(k),term(d,1,[i,j,k]),2))
 return r

def test(d):
 b=basis(d); N=len(b)
 lam=[F(2*(d+4),d*d*(d+1)),F(2*(d+2)*(d+4),3*d*(d+1)),F((d-3)*(d+2)*(d+4),d*d*(d+1))]
 b_derivs=[[deriv(p,j) for j in range(d)] for _,p,_ in b]
 for i,(_,p,sec) in enumerate(b):
  for j,(_,q,sec2) in enumerate(b[:i+1]):
   B=F(0)
   for r in range(d):B+=expectation(mul(b_derivs[i][r],b_derivs[j][r]),'cube')
   B= (B-F(9,d)*expectation(mul(p,q),'cube'))/d**2
   A=3*(d+1)*expectation(mul(p,q),'sphere')
   expected=lam[sec]*A if sec==sec2 else 0
   assert B==expected,(d,i,j,B,expected)
 count=[sum(1 for _,_,s in b if s==j) for j in range(3)]
 assert count==[d,d*(d-2),d*(d-1)*(d-2)//6]
 trace=sum(lam[j]*count[j] for j in range(3))
 assert trace==N,(trace,N)
 if d>=4:
  assert min(lam)==lam[0]
  maximum=lam[1] if d<=9 else lam[2]
  assert max(lam)==maximum
  cond=F(d*(d+2),3) if d<=9 else F((d-3)*(d+2),2)
  assert maximum/lam[0]==cond
 else:
  assert lam[2]==0
 print('PASS',d,'dim',N,'multiplicities',count,'eigenvalues',*[str(x) for x in lam],'condition',str(cond) if d>=4 else 'infinite')

if __name__=='__main__':
 for d in range(3,8):test(d)
