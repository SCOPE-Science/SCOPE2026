#!/usr/bin/env python3
"""Finite arithmetic and numerical consistency checks for a weighted jet kernel."""
import cmath, math, random

def rise(h,n):
    ans=1.0
    for j in range(n): ans*=h+j
    return ans

def coeff(h,a,b):
    c=[1.,a,b]; r=[0.]*5
    for i in range(3):
        for j in range(3):
            r[4-i-j]+=(-1)**i*rise(h,i+j)*c[i]*c[j]
    return r

def polynomial(h,a,b,t):
    r=coeff(h,a,b)
    return sum(r[k]*t**k for k in range(5))

def positive_half_roots(h,a,b):
    d=rise(h,2);D=rise(h,4)
    z=d*(2*b-a*a);w=D*b*b
    disc=complex(z*z-4*w)
    u=[(-z+cmath.sqrt(disc))/2,(-z-cmath.sqrt(disc))/2]
    rr=[]
    for k in u:
        s=cmath.sqrt(k);rr.extend([s,-s])
    return rr

random.seed(2323)
count=0
for h in [1.1,1.5,2.0,2.9,5.2,13.0]:
  for b in [-3.,-1.1,-.1,.1,.8,4.]:
    threshold=2*b+2*math.sqrt(rise(h,4))/rise(h,2)*abs(b)
    for rel in [.1,.5,.9,1.,1.1,2.,4.]:
      a=math.sqrt(threshold*rel)
      r=coeff(h,a,b)
      assert abs(r[3])<1e-10 and abs(r[1])<1e-9
      assert math.isclose(r[2],rise(h,2)*(2*b-a*a),rel_tol=1e-12,abs_tol=1e-10)
      assert math.isclose(r[0],rise(h,4)*b*b,rel_tol=1e-12,abs_tol=1e-10)
      roots=positive_half_roots(h,a,b)
      for z in roots:
        assert abs(polynomial(h,a,b,z))<1e-6*max(1,abs(z)**4,abs(r[0]))
      if rel<1: assert sum(z.imag>1e-7 for z in roots)==2
      elif rel>1: assert sum(z.imag>1e-7 for z in roots)==0
      else: assert all(abs(z.imag)<1e-6 for z in roots)
      count+=1
for h in [1.2,2.,3.,7.]:
  for a in [0.,.4,2.]:
    assert abs(coeff(h,a,0.)[0])<1e-12
    assert coeff(h,a,0.)[2]<=0
    count+=1
# Direct complex derivative check (finite-difference not used):
for h in [1.2,2.,4.5]:
  for _ in range(50):
    a=random.uniform(-2,2); b=random.uniform(-2,2)
    z=random.uniform(-2,2)+1j*random.uniform(.15,2)
    w=random.uniform(-2,2)+1j*random.uniform(.15,2)
    t=z-w.conjugate()
    c=[1,a,b]
    direct=sum(c[i]*c[j]*(-1)**i*rise(h,i+j)/t**(i+j) for i in range(3) for j in range(3))
    ans=polynomial(h,a,b,t)/t**4
    assert abs(direct-ans)<1e-8*max(1,abs(direct))
    count+=1
print('PASS',count,'parameter or derivative-consistency configurations')
