#!/usr/bin/env python3
"""Symbolic and exact rational checks for the orientation law of three juvenile-adult seasons."""
from sympy import symbols, Matrix, simplify, expand, det, trace, Rational, sqrt
from itertools import permutations, product
from random import Random

a=symbols('a1 a2 a3'); b=symbols('b1 b2 b3'); s=symbols('s1 s2 s3'); u=symbols('u',positive=True)
B=[Matrix([[0,u*b[i]],[s[i],a[i]]]) for i in range(3)]
plus=B[2]*B[1]*B[0]; minus=B[1]*B[2]*B[0]
D=Matrix([[a[i],b[i],s[i]] for i in range(3)]).det()
P=b[0]*b[1]*b[2]*s[0]*s[1]*s[2]
assert simplify(trace(plus)-trace(minus)-u*D)==0
assert simplify(plus.det()+u**3*P)==0
assert simplify(minus.det()+u**3*P)==0
A=a[0]*a[1]*a[2]
Cplus=a[0]*b[1]*s[2]+a[1]*b[2]*s[0]+a[2]*b[0]*s[1]
Cminus=a[0]*b[2]*s[1]+a[1]*b[0]*s[2]+a[2]*b[1]*s[0]
assert simplify(trace(plus)-(A+u*Cplus))==0
assert simplify(trace(minus)-(A+u*Cminus))==0
print('symbolic universal identities passed')

v_a=[Rational(1,4), Rational(1,2),Rational(3,4)]
v_b=[Rational(1,2),Rational(2),Rational(1,2)]
v_s=[Rational(1,2)]*3
sub={u:1,**dict(zip(a,v_a)),**dict(zip(b,v_b)),**dict(zip(s,v_s))}
Wp=plus.subs(sub); Wm=minus.subs(sub)
Tp=trace(Wp); Tm=trace(Wm); Delta=Wp.det()
assert (Tp,Tm,Delta)==(Rational(21,32),Rational(33,32),-Rational(1,16))
assert Rational(1)-Tp+Delta>0
assert Rational(1)-Tm+Delta<0
assert D.subs(sub)==-Rational(3,8)
print('witness trace+',Tp,'trace-',Tm,'common determinant',Delta, 'orientation volume',D.subs(sub))
print('P_plus=',Wp, 'P_minus=',Wm)

# Multiply the rational matrix representations using separate tuple arithmetic,
# not SymPy matrix multiplication, to check all 6 orders.
def matmul(X,Y):
 return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
I=((Rational(1),Rational(0)),(Rational(0),Rational(1)))
base=[((Rational(0),v_b[i]),(v_s[i],v_a[i])) for i in range(3)]
classes={}
for perm in permutations(range(3)):
 Z=I
 for idx in perm:Z=matmul(base[idx],Z)
 tr=Z[0][0]+Z[1][1]
 classes[perm]=tr
assert len(set(classes.values()))==2 and set(classes.values())=={Tp,Tm}
assert classes[(0,1,2)]==Tp and classes[(0,2,1)]==Tm
print('6 orderings separate rational multiplication passed:',classes)

rng=Random(20261105)
for t in range(1000):
 aa=[Rational(rng.randrange(1,10),10) for _ in range(3)]
 ss=[Rational(rng.randrange(1,10),10) for _ in range(3)]
 ff=[Rational(rng.randrange(1,20),10) for _ in range(3)]
 mu=Rational(rng.randrange(1,30),10)
 M=[((Rational(0),mu*ff[i]),(ss[i],aa[i])) for i in range(3)]
 trset={}
 for p in permutations(range(3)):
  Z=I
  for i in p:Z=matmul(M[i],Z)
  trset[p]=Z[0][0]+Z[1][1]
 orient=Matrix([[aa[i],ff[i],ss[i]] for i in range(3)]).det()
 assert trset[(0,1,2)]-trset[(0,2,1)]==mu*orient
 assert len(set(trset.values()))<=2
print('1000 randomly generated exact rational 6-permutation tests passed')
