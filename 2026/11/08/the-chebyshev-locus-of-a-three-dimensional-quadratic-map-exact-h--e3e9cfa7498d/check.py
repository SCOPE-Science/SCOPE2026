"""Reproduce the Chebyshev-coordinate algebra and finite periodic checks.

The all-period and ergodic assertions require the mathematical proof in RESULT.md.
"""
from fractions import Fraction as Q
import sympy as sp

x,v,u,w=sp.symbols('x v u w')
a2,a3,b1,b2,c=sp.symbols('a2 a3 b1 b2 c')
k=b2*c
A=a3*k*k
B=-k*(a2+2*a3*b1)
C=a2*b1+a3*b1*b1
s=-4/A
t=(4-B)/(2*A)
psi=A*x*x+B*x+C
phi=sp.expand(psi.subs(x,t+s*v)-t-s*(4*v-4*v*v))
condition=k*k*a2*a2+2*k*(a2+2*a3*b1)-8
assert sp.cancel(phi/s-condition/16)==0
assert sp.expand(4*A*C-B**2+2*B+8+condition)==0

param_examples=[
 {'a2':Q(4),'a3':Q(-4),'b1':Q(1),'b2':Q(1),'c':Q(1)},
 {'a2':Q(1),'a3':Q(5,8),'b1':Q(2),'b2':Q(1),'c':Q(1)},
 {'a2':Q(2),'a3':Q(-2),'b1':Q(1),'b2':Q(2),'c':Q(1)},
 {'a2':Q(1),'a3':Q(-9,4),'b1':Q(1),'b2':Q(-1),'c':Q(1)},
 {'a2':Q(2),'a3':Q(-4),'b1':Q(0),'b2':Q(1),'c':Q(1)},
 {'a2':Q(0),'a3':Q(2),'b1':Q(1),'b2':Q(1),'c':Q(1)},
]
verified=0
for p in param_examples:
 aa,aa3,bb,bb2,cc=(p[z] for z in ('a2','a3','b1','b2','c'))
 kk=bb2*cc; AA=aa3*kk*kk; BB=-kk*(aa+2*aa3*bb)
 assert kk*kk*aa*aa+2*kk*(aa+2*aa3*bb)==8,(p,'not on locus')
 ss=-4/AA; tt=(4-BB)/(2*AA)
 for i in range(9):
  uu=Q(i,8); vv=Q((i*3)%9,8); ww=Q((i*5)%9,8)
  xx=tt+ss*uu; yy=bb-kk*(tt+ss*vv); zz=cc*(tt+ss*ww)
  fx=aa*yy+aa3*yy**2; fy=bb-bb2*zz; fz=cc*xx
  expx=tt+ss*(4*vv*(1-vv)); expy=bb-kk*(tt+ss*ww); expz=cc*(tt+ss*uu)
  assert (fx,fy,fz)==(expx,expy,expz)
  verified+=1

# All fixed points of the full tent iterate occur once on its dyadic branches.
def tent_fixed(n):
 m=2**n
 return [Q(j,m-1) if j%2==0 else Q(j+1,m+1) for j in range(m)]
for n in range(1,11):
 pts=tent_fixed(n)
 assert len(pts)==len(set(pts))==2**n
 for j,pt in enumerate(pts):
  assert Q(j,2**n)<=pt<=Q(j+1,2**n)
  def tent(z): return 2*z if z<=Q(1,2) else 2*(1-z)
  z=pt
  for _ in range(n): z=tent(z)
  assert z==pt

# Primitive-point census by direct minimal periods on tent fixed points.
for n in range(1,10):
 pts=tent_fixed(n)
 def tent(z): return 2*z if z<=Q(1,2) else 2*(1-z)
 counts={}
 for pt in pts:
  z=pt
  for d in range(1,n+1):
   z=tent(z)
   if z==pt:
    counts[d]=counts.get(d,0)+1
    break
 assert sum(counts.values())==2**n
 for d in counts:
  assert n%d==0

print('CHECK_OK: 6 rational parameter witnesses; 54 exact conjugacy tests; tent fixed-point proof corroborated through n=10; primitive periods through n=9')
