#!/usr/bin/env python3
"""Exact symbolic verification for the five-point symmetric polynomial hypergroup theorem.
Requires SymPy. No numerical evidence is used as a substitute for the proof.
"""
import random
import sympy as s
u,v,w=s.symbols('u v w', real=True)
A=1-u-w
D=(1-u)*(1-w)+u*w
B=1-u-v+u*v-v*w
C=(1-w)**2-u*(1-2*w)-v*D
J=s.zeros(5)
d=[0,u,v,w,1]
for i in range(5):
    if i<4:J[i,i+1]=1-d[i]
    if i>0:J[i,i-1]=d[i]
assert all(s.simplify(sum(J[i,j] for j in range(5))-1)==0 for i in range(5))
R=[s.eye(5), J]
for i in range(1,4):
    R.append(s.simplify((J*R[-1]-d[i]*R[-2])/(1-d[i])))
assert all(s.simplify(R[i][0,j]-int(i==j))==0 for i in range(5) for j in range(5))
for i in range(5):
    assert all(s.simplify(sum(R[i][j,k] for k in range(5))-1)==0 for j in range(5))
assert s.factor(D*B-(1+w-u)*C-w*w*A)==0
assert s.factor(C-D*(w-v)-(1-u)*(1-w)*(1-2*w))==0
# Nine nontrivial classes of structure constants up to symmetric triple permutation.
triple = {
 (1,1,2): 1-u,
 (1,2,3): 1-v,
 (1,3,4): 1-w,
 (2,2,2): (w-u+v*A)/(1-u),
 (2,2,4): (1-v)*(1-w)/(1-u),
 (2,3,3): (1-u-v*w)/(1-u),
 (2,4,4): A/(1-u),
 (3,3,4): (1-w)*B/((1-u)*(1-v)),
 (4,4,4): C/((1-u)*(1-v)*(1-w)),
}
for (i,j,k),expr in triple.items():
    assert s.factor(R[i][j,k]-expr)==0,(i,j,k)
for i in range(5):
  for j in range(5):
    for k in range(5):
      e=s.factor(R[i][j,k])
      if k>i+j or i>j+k or j>i+k or (i+j+k)%2:
        assert e==0,(i,j,k,e)
      elif 0 in (i,j,k):
        if i==0:
            assert e==int(j==k)
        elif j==0:
            assert e==int(i==k)
        elif k==0:
            norm=s.prod(d[t]/(1-d[t-1]) for t in range(1,i+1)) if i==j else 0
            assert s.factor(e-norm)==0,(i,j,k,e,norm)
      else:
        a,b,c=sorted((i,j,k))
        hk=s.prod(d[t]/(1-d[t-1]) for t in range(1,k+1))
        hc=s.prod(d[t]/(1-d[t-1]) for t in range(1,c+1))
        assert s.factor(e/triple[(a,b,c)]-hc/hk)==0,(i,j,k,e)
# Strictly increasing rational profiles: a full 125-coefficient check for each.
rng=random.Random(23111)
for _ in range(200):
    vals=sorted(rng.sample(range(1,100),3))
    point={u:s.Rational(vals[0],100),v:s.Rational(vals[1],100),w:s.Rational(vals[2],100)}
    expected=A.subs(point)>=0 and C.subs(point)>=0
    actual=all(e.subs(point)>=0 for matrix in R for e in matrix)
    assert expected==actual,(point,expected,actual)
# Independent sharp boundaries and a positive hypergroup outside Newton log-concavity.
tests=[((s.Rational(1,6),s.Rational(1,4),s.Rational(11,12)),False,True),
       ((s.Rational(1,12),s.Rational(5,12),s.Rational(2,3)),True,False),
       ((s.Rational(1,20),s.Rational(3,20),s.Rational(7,20)),True,True)]
for vals,want_A,want_C in tests:
    z=dict(zip([u,v,w],vals))
    assert (A.subs(z)>=0)==want_A
    assert (C.subs(z)>=0)==want_C
z=dict(zip([u,v,w],tests[-1][0]))
nu=[u,v-2*u,w-3*v+3*u,1-4*w+6*v-4*u]
ns=[x.subs(z) for x in nu]
assert all(t>0 for t in ns)
assert ns[2]**2<ns[1]*ns[3]
assert [A.subs(z),C.subs(z)]==[s.Rational(3,5),s.Rational(1249,4000)]
print('CHECK_OK 125_coefficients=exact 9_nontrivial_classes=exact 200_profiles=rational 3_boundary_cases=exact')
