#!/usr/bin/env python3
"""Exact symbolic finite-matrix computation for ladder excitation enumerators."""
import sympy as s
r=(-1,0,1)
T={k:s.zeros(3) for k in r}
for i,u in enumerate(r):
    for j,v in enumerate(r):
        for t in r:
            w=(t+v-u+1)%3-1
            k=(t+v-w-u)//3
            T[k][i,j]+=1
B=s.zeros(9)
for i,old in enumerate(r):
    for j,new in enumerate(r):
        if old==new and new!=0:continue
        for a in range(3):
            for b in range(3):
                B[3*i+a,3*j+b]=T[new][a,b]
u=s.zeros(1,9)
for a in range(3):u[3+a]=1
v=s.ones(9,1)
z=s.Symbol('z')
fg=s.factor((3*u*(s.eye(9)-z*B).inv()*v)[0])
zg=s.factor((3*s.ones(1,3)*(s.eye(3)-z*T[0]).inv()*s.ones(3,1))[0])
assert s.cancel(fg-3*(3+z*z)/(1-9*z+z*z-3*z**3))==0
assert s.cancel(zg-3*(3-2*z)/(1-7*z+4*z*z))==0
print('Q(z) =',fg)
print('Z(z) =',zg)
print('PASS: exact polynomial-rational identity for both transfer matrices.')
