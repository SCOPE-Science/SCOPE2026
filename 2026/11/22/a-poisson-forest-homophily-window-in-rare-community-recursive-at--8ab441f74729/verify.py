"""Finite exact checks and asymptotic controls for rare-type community-weighted attachment.
Standard library only. Run: python verify.py
"""
from fractions import Fraction as F
from math import log, factorial
from itertools import product

checks=0
def ok(test):
    global checks
    assert test
    checks+=1

# Exact finite conditional law, with prescribed types. The weights do not
# depend on degrees when gamma=0. Compare the per-vertex kernel with
# its community-selection factorization for all short type sequences.
qa,qb=F(1,3),F(2,5)
for n in range(1,8):
  for types in product('AB',repeat=n):
    vertices=['A','B']
    for typ in types:
      a_ct=vertices.count('A'); b_ct=vertices.count('B')
      w=[((1-qa) if v=='A' else qa) if typ=='A' else (qb if v=='A' else (1-qb)) for v in vertices]
      prob=[v/sum(w) for v in w]
      ok(sum(prob)==1)
      if typ=='B':
        alpha=qb/(1-qb)
        ok(sum(prob[i] for i,x in enumerate(vertices) if x=='A') == alpha*a_ct/(b_ct+alpha*a_ct))
      else:
        ok(sum(prob[i] for i,x in enumerate(vertices) if x=='A') == (1-qa)*a_ct/((1-qa)*a_ct+qa*b_ct))
      vertices.append(typ)

# Exact multinomial covariance for B-to-A choices at deterministic A-birth times.
# For two distinct A vertices, their child-count covariance is the negative
# sum of simultaneous choice products. Variance = sum p(1-p).
for n in (100,300,1000,3000,10000):
  r,b=2,3; a=F(2,3); births=[n//3,2*n//3]
  mu=[F(0),F(0)]; cov=F(0); err=F(0)
  for j in range(1,n+1):
    A=r+sum(t<j for t in births)
    B=b+j-1-sum(t<j for t in births)
    if j in births: continue
    den=B+a*A
    ps=[a/den if j>t else F(0) for t in births]
    for i in range(2):mu[i]+=ps[i]
    cov-=ps[0]*ps[1]
    err+=(ps[0]+ps[1])**2
  for i,t in enumerate(births):
    ok(abs(float(mu[i])-float(a)*log(n/t)) < 13/n)
  ok(cov<=0)
  ok(float(err)<80/n)
  # Exact value of the limiting compound Poisson mark intensities for a=2/3
  for k in range(12):
    intensity=a**k/(1+a)**(k+1)
    ok(intensity>0)
    if k>0:ok(intensity/(a**(k-1)/(1+a)**k)==a/(1+a))

# Exact critical homophily competition among A or B targets, for a sparse
# prescribed A-arrival: n q_A -> theta, with r+j-1 available A targets.
for theta in (F(0),F(1),F(3),F(10)):
  for k in range(1,8):
    for u_num in range(1,9):
      u=F(u_num,10); a_ct=2+k-1
      desired=theta*u/(a_ct+theta*u)
      for n in (1000,10000):
        t=int(u*n); qa=theta/n
        b_ct=3+t-k
        exact=qa*b_ct/(qa*b_ct+(1-qa)*a_ct)
        ok(abs(float(exact-desired)) <= 60/n)

# Limiting marked-point-process Poisson means sum exactly to arrival rate c.
a=F(2,3)
for cutoff in (10,30,90):
  mass=sum((a**k)/(1+a)**(k+1) for k in range(cutoff))
  ok(mass==1-(a/(1+a))**cutoff)
print('PASS',checks,'exact/finite checks')
