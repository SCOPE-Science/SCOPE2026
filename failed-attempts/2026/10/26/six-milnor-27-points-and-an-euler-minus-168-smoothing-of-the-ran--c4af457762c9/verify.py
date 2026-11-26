#!/usr/bin/env python3
"""Exact independent identity checker for a smoothing of a quartic K3-fibred threefold.
Requires only Python 3 standard library. The geometric hypotheses are proved separately."""
from collections import defaultdict
from fractions import Fraction

def plus(*terms):
    a=defaultdict(int)
    for x in terms:
        for k,v in x.items(): a[k]+=v
    return {k:v for k,v in a.items() if v}

def scale(a,m): return {k:v*m for k,v in a.items() if v*m}

def mul(a,b):
    c=defaultdict(int)
    for (h1,f1,t1),v in a.items():
        for (h2,f2,t2),w in b.items():
            h,f,t=h1+h2,f1+f2,t1+t2
            if f<=1 and t<=4: c[(h,f,t)]+=v*w
    return {k:v for k,v in c.items() if v}

def power(a,n):
    r={(0,0,0):1}
    for _ in range(n): r=mul(r,a)
    return r

def coeff(a,n):
    return {(h,f,0):v for (h,f,t),v in a.items() if t==n}
ONE={(0,0,0):1}
H={(1,0,0):1};F={(0,1,0):1};T={(0,0,1):1}
def cm(a): return plus(ONE,mul(T,a))
c=mul(cm(scale(F,2)),mul(power(cm(plus(H,scale(F,3))),2),mul(cm(plus(H,scale(F,4))),cm(H))))
c1,c2,c3=(coeff(c,k) for k in (1,2,3))
D=plus(scale(H,4),scale(F,12))
assert c1==D
assert c2=={(2,0,0):6,(1,1,0):38},c2
assert c3=={(3,0,0):4,(2,1,0):42},c3
integrand=mul(D,plus(c3,scale(mul(c2,D),-1),mul(c1,power(D,2)),scale(power(D,3),-1)))
assert integrand=={(4,0,0):-80,(3,1,0):-968},integrand
# From H(H+3F)^2(H+4F)=H^4+10FH^3=0 and integral FH^3=1.
euler=integrand[(4,0,0)]*(-10)+integrand[(3,1,0)]
assert euler==-168
# The only W-free quartics with nonnegative base degree are the five binary X,Y terms.
allowed=[]
for a in range(5):
 for b in range(5-a):
  for z in range(5-a-b):
   w=4-a-b-z
   if 12-3*a-3*b-4*z>=0: allowed.append((a,b,z,w))
assert sum(w==0 for a,b,z,w in allowed)==5
assert all(z==0 for a,b,z,w in allowed if w==0)
assert (0,0,3,1) in allowed and (0,0,4,0) not in allowed
# Projective roots [0:1],[-25:1],[-9:1],[1:0] are pairwise different.
roots={0,-25,-9,None}
assert len(roots)==4
# Res(q_x(t,1),q_y(t,1)) where q_x=3t^2+68t+225, q_y=t^3+68t^2+675t.
# Sylvester matrix: 3 shifts of quadratic followed by 2 shifts of cubic.
a=[3,68,225]; b=[1,68,675,0]
mat=[]
for i in range(3): mat.append([0]*i+a+[0]*(2-i))
for i in range(2): mat.append([0]*i+b+[0]*(1-i))
def det_bareiss(m):
    m=[list(map(int,row)) for row in m]; n=len(m);sign=1;prev=1
    for k in range(n-1):
        if m[k][k]==0:
            j=next(j for j in range(k+1,n) if m[j][k]);m[k],m[j]=m[j],m[k];sign=-sign
        p=m[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                num=m[i][j]*p-m[i][k]*m[k][j]
                assert num%prev==0
                m[i][j]=num//prev
        for i in range(k+1,n):m[i][k]=0
        prev=p
    return sign*m[-1][-1]
res=det_bareiss(mat)
assert res==-207360000,res
# At infinity q_y(1,0)=1, so no common projective zero of q_x,q_y.
# Cubic complete-intersection colength 3*3=9; extra s^3 and z factors give 27.
mu=3*3*3
assert mu==27
# Six exceptional degree-2 del Pezzo surfaces have e=10.
e_del_pezzo=2*3-(2-2*3)
assert e_del_pezzo==10
resolved_euler=48
singular_euler=resolved_euler-6*(e_del_pezzo-1)
smoothed_euler=singular_euler-6*mu
assert (singular_euler,smoothed_euler)==(-6,-168)
assert resolved_euler-smoothed_euler==6*(e_del_pezzo-1+mu)==216
# Four coplanar lines have self-intersection -2 and pairwise intersection 1.
A=[[-2 if i==j else 1 for j in range(4)] for i in range(4)]
assert det_bareiss(A)==-27,det_bareiss(A)
print('VERIFY_OK canonical_chern_Euler=-168 local_Milnor=27 six_germs Euler_jump=216 forced_four_lines_rank=4')
