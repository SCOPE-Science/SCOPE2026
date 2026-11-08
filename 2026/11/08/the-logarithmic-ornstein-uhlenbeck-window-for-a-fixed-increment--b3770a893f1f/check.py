"""Exact finite-state and moment tests for a fixed-increment mixed two-color urn."""
from collections import defaultdict
from fractions import Fraction as Q
from math import exp, log

checks=0

def verify(a,b,p,init=(2,3),steps=7):
    global checks
    s=a+b; p=Q(p)
    states={init:Q(1)}
    d0=init[0]-init[1]; t0=sum(init)
    m1=Q(d0); m2=Q(d0*d0)
    avgk=s-2*b*p
    v=p*(a-b)**2+(1-p)*s*s
    # Pairwise joint products E[D_j D_k] from conditional expectation.
    for j in range(steps+1):
        t=t0+j*s
        emp1=sum((y-z)*v0 for (y,z),v0 in states.items())
        emp2=sum((y-z)**2*v0 for (y,z),v0 in states.items())
        assert emp1==m1,(a,b,p,j,'mean',emp1,m1)
        assert emp2==m2,(a,b,p,j,'second',emp2,m2)
        checks+=2
        if j==steps:break
        nxt=defaultdict(Q)
        for (y,z),prob in states.items():
            tot=y+z
            for eta,pe in ((1,Q(y,tot)),(-1,Q(z,tot))):
                for is_f,pm in ((True,p),(False,1-p)):
                    if is_f:
                        target=(y+a,z+b) if eta==1 else (y+b,z+a)
                    else:
                        target=(y+s,z) if eta==1 else (y,z+s)
                    nxt[target]+=prob*pe*pm
        states=dict(nxt)
        m2=(1+2*avgk/Q(t))*m2+v
        m1=(1+avgk/Q(t))*m1
    assert sum(states.values())==1
    checks+=1

for params in [(1,1,Q(1,2)),(1,2,Q(3,8)),(2,3,Q(5,8)),(3,2,Q(1,4))]:
    verify(*params)

# Algebraic conditional variance, tested exactly against all four outcomes.
for a,b in [(1,1),(1,2),(2,3),(4,2)]:
 for pn in [Q(1,10),Q(1,2),Q(9,10)]:
  s=a+b;kbar=s-2*b*pn; v=pn*(a-b)**2+(1-pn)*s*s
  for x in [Q(-1),Q(-2,5),Q(0),Q(3,7),Q(1)]:
   dist=[(pn*Q(1+x,2),a-b),(pn*Q(1-x,2),b-a),((1-pn)*Q(1+x,2),s),((1-pn)*Q(1-x,2),-s)]
   e=sum(prob*k for prob,k in dist)
   var=sum(prob*(k-e)**2 for prob,k in dist)
   assert e==kbar*x
   assert var==v-kbar*kbar*x*x
   checks+=2

# Exact second moment recurrence for the terminal rescaled difference;
# at the logarithmic critical window it approaches an OU covariance.
def second_moment(N,a,b,theta):
 s=a+b; pc=s/(4*b); pn=pc+theta/log(N)
 assert 0<pn<1
 lamb=1-2*b*pn/s
 v=pn*(a-b)**2+(1-pn)*s*s
 # initial (1,1) so D_0=0, T_0=2
 m2=0.0
 t0=2.0
 for j in range(N):
  m2 = (1+2*s*lamb/(t0+s*j))*m2+v
 return m2/(N*log(N))

for a,b in [(1,1),(1,2)]:
 s=a+b;pc=s/(4*b);v0=pc*(a-b)**2+(1-pc)*s*s
 for theta in [-0.7,0.0,0.9]:
  delta=2*b*theta/s
  target=v0*(-__import__('math').expm1(-2*delta))/(2*delta) if delta else v0
  errs=[]
  for N in [20000,200000]:
   got=second_moment(N,a,b,theta)
   errs.append(abs(got-target))
   assert abs(got-target)<0.50*target,(N,a,b,theta,got,target)
   checks+=1
  assert errs[1]<errs[0],(a,b,theta,errs)
  checks+=1

print('PASS',checks,'exact/algebraic/asymptotic checks')
