"""Exact arithmetic checks for the Markov-sampled scalar-quadratic claim.
Requires Python 3 and sympy. Run: python checks/verify.py
These finite checks supplement, not replace, the analytic proof.
"""
from fractions import Fraction as F
import itertools
import sympy as s

A,D,C,r=s.symbols('A D C r',real=True)
g,h,v,w=s.symbols('g h v w',real=True)
Q=A*A+D*D; U=A+D*D/(1-A)
moment=[g-(A*g-D*h),h-r*(A*h-D*g-C),
        v-(Q*v-2*A*D*w+2*C*D*g-2*A*C*h+C*C),
        w-r*(Q*w-2*A*D*v+2*C*D*h-2*A*C*g)]
sol=s.solve(moment,(g,h,v,w))
V=C*C*((1+U*r)*(1-Q*r)+4*A*D**2*r*r/(1-A))/((1-U*r)*((1-Q)*(1-Q*r)-4*A*A*D*D*r))
assert s.cancel(V-sol[v])==0
print('symbolic stationary moment identity: PASS')

step,t=s.symbols('step t',real=True)
Vn=s.factor(V.subs({A:1-step,D:step*t,C:step}, simultaneous=True))
q=1-t*t;u=1-step*q
Vm=step**2*(1+t*t)/(2-step*q)**2
Vp=(1+t*t)/q**2
assert s.cancel(Vn.subs(r,-1)-Vm)==0
assert s.cancel(Vn.subs(r,1)-Vp)==0
assert s.cancel((Vp-Vm)-4*(1+t*t)*u/(q**2*(2-step*q)**2))==0
Fpoly=step**3*(t**4-1)+3*step**2*(1+t*t)-2*step*(t*t+2)+2
Gpoly=step**2*(t**4-1)+3*step*(t*t+1)-4*t*t-2
Fder=2*step*Fpoly/((2-step*q)**3*(2-2*step+step**2*q))
Gder=-2*Gpoly/(step*q**3*(2-step*(1-t))*(2-step*(1+t)))
assert s.cancel(s.diff(Vn,r).subs(r,-1)-Fder)==0
assert s.cancel(s.diff(Vn,r).subs(r,1)-Gder)==0
z,Uvar=s.symbols('z Uvar',real=True)
Frep=(4-2*Uvar)*z**2+(Uvar**3-5*Uvar)*z+Uvar**3+Uvar
Fsos=(4-2*Uvar)*(z-Uvar*(5-Uvar**2)/(8-4*Uvar))**2+Uvar*(1-Uvar)**2*(16-Uvar-2*Uvar**2-Uvar**3)/(8*(2-Uvar))
assert s.cancel(Frep-Fsos)==0
assert s.cancel((Fpoly.subs(step,(1-Uvar)/(1-t*t))-(Frep/(1-z)**2).subs(z,t*t)))==0
assert s.cancel(Gpoly.subs(step,(1-Uvar)/(1-t*t))-(4*t**4-(1+t*t)*Uvar*(Uvar+1))/(1-t*t))==0
print('symbolic endpoints, derivatives, and positivity decomposition: PASS')

# Exact dynamic moment update, and independent path enumeration.
def update(m,a,d,c,rr):
  gg,hh,vv,ww=m
  qq=a*a+d*d
  return (a*gg-d*hh,rr*(a*hh-d*gg-c),
          qq*vv-2*a*d*ww+2*c*d*gg-2*a*c*hh+c*c,
          rr*(qq*ww-2*a*d*vv+2*c*d*hh-2*a*c*gg))

def paths(n,step,tt,pr):
  out=F(0)
  for sig in (-1,1):
    for flips in itertools.product((False,True),repeat=n-1):
      prob=F(1,2); signs=[sig]
      for flip in flips:
        prob*= (1-pr if flip else pr)
        signs.append(-signs[-1] if flip else signs[-1])
      x=F(0)
      for ss in signs:x=(1-step*(1+tt*ss))*x-step*ss
      out+=prob*x*x
  return out
count=0
for tt in (F(0),F(1,7),F(1,4),F(2,5),F(3,5)):
 for step0 in (F(1,5),F(3,5),F(1),F(6,5)):
  if step0>=2/(1+tt): continue
  for pr in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
   rr=2*pr-1;a=1-step0;d=step0*tt
   mom=(F(0),)*4
   for n in range(1,7):
    mom=update(mom,a,d,step0,rr)
    assert mom[2]==paths(n,step0,tt,pr),(n,tt,step0,pr,mom[2])
    count+=1
print(f'exact Markov-path versus moment recurrence: {count} PASS')

# Stationary 4x4 solved exactly and compared to the closed-form risk.
def stationary_moments(step0,tt,rr):
  aa=1-step0; dd=step0*tt;cc=step0
  us=aa+dd*dd/(1-aa);qq=aa*aa+dd*dd
  H= -rr*cc/(1-us*rr)
  G= -dd*H/(1-aa)
  base=(1-qq)*(1-qq*rr)-4*aa*aa*dd*dd*rr
  VV=cc*cc*((1+us*rr)*(1-qq*rr)+4*aa*dd*dd*rr*rr/(1-aa))/((1-us*rr)*base)
  W=(rr*(-2*aa*dd*VV+2*cc*dd*H-2*aa*cc*G))/(1-rr*qq)
  return G,H,VV,W
checks=0
for tt in (F(0),F(1,11),F(1,4),F(2,5),F(3,5),F(4,5)):
 for step0 in (F(1,7),F(1,2),F(9,10),F(11,10),F(6,5),F(3,2),F(17,10)):
  if step0>=2/(1+tt):continue
  vals=[]
  for rr in (F(-1),F(-3,4),F(-1,2),F(-1,4),F(0),F(1,4),F(1,2),F(3,4),F(1)):
    ss=stationary_moments(step0,tt,rr)
    assert ss==update(ss,1-step0,step0*tt,step0,rr)
    vals.append(ss[2]);checks+=1
  assert all(x>=min(vals[0],vals[-1]) for x in vals)
  assert ((vals[-1]-vals[0]>0)==(step0*(1-tt*tt)<1)) or vals[-1]==vals[0]
print(f'exact stationary fixed points and interior comparisons: {checks} PASS')
print('All checks completed.')
