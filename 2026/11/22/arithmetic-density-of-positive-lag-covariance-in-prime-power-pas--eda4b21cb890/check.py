#!/usr/bin/env python3
"""Exact and finite cross-checks of Pascal-column shift-covariance theorem."""
from fractions import Fraction as Q
from math import comb, floor

def vp(n,p):
    if n==0: return None
    k=0
    while n%p==0:
        n//=p;k+=1
    return k

def alpha(x,p):
    return Q(0) if x==0 else Q(1,p**vp(abs(x),p))

def covariance(p,a,h):
    r=p**a;t,u=divmod(h,r)
    return (Q(p)-(p+1)*(Q(r-u,r)*alpha(t,p)+Q(u,r)*alpha(t+1,p)))/(p-1)**2

def positive_by_criterion(p,a,h):
    r=p**a;t,u=divmod(h,r)
    if t%p==0:
        v=vp(t,p)
        if v is None:return Q(r-u,r)>Q(1,p+1)
        return Q(r-u,r)*(1-Q(1,p**v))>Q(1,p+1)
    if (t+1)%p==0:
        v=vp(t+1,p)
        return Q(u,r)*(1-Q(1,p**v))>Q(1,p+1)
    return False

def density(p,a):
    r=p**a
    c=lambda d:r*p**d//((p+1)*(p**d-1))
    c_inf=r//(p+1)
    return sum((Q(p-1,p**(d+1))*Q(2*r-1-2*c(d),r) for d in range(1,a+1)),Q(0))+Q(2*r-1-2*c_inf,r*p**(a+1))

def limit(p,terms=30):
    lam=sum((Q(1,p**d-1) for d in range(1,terms+1)),Q(0))
    value=Q(2,p)-Q(2*(p-1),p*(p+1))*lam
    return value

n_bin=0
for p in (2,3,5,7):
  for a in (1,2,3):
    r=p**a
    if r>250:continue
    for n in range(r,min(900,4*r+200)):
        x=comb(n,r)
        assert vp(x,p)==vp(n//r,p),(p,a,n,x)
        n_bin+=1
print('binomial Kummer identity verified cases',n_bin)

n_sign=0
for p in (2,3,5,7):
  for a in (1,2,3):
    r=p**a
    for h in range(1,min(10000,r*500)):
        c=covariance(p,a,h)
        assert c!=0,(p,a,h)
        assert (c>0)==positive_by_criterion(p,a,h),(p,a,h,c)
        n_sign+=1
print('exact lag sign independent decision cases',n_sign)

for p,a in ((2,1),(2,2),(3,1),(3,2),(5,1),(5,2)):
    r=p**a
    target=density(p,a)
    L=6 if p<=3 else 4
    nh=r*p**L
    got=Q(sum(covariance(p,a,h)>0 for h in range(1,nh)),nh)
    assert abs(target-got)<=Q(3,p**L),(p,a,target,got)
    approx=limit(p,35)
    assert abs(target-approx)<=Q(1,p**(a+1))+Q(2,p**34)
    print(f'p={p} a={a}: density={target}, shift finite={got} at N={nh}, high-a limit~{float(approx):.9f}')

# Full second-moment direct periodic verification with a growing p-adic precision.
# At depth L, v_p(0) is truncated to L, so convergence is O(L^2 p^-L).
n_mom=0
for p,a,h,L in ((2,1,1,14),(2,1,2,14),(2,2,3,14),(2,2,4,14),(3,1,1,9),(3,1,3,9),(3,2,8,9),(5,1,1,6)):
    r=p**a; P=p**L
    vs=[L if q==0 else vp(q,p) for q in range(P)]
    # cyclic sequence values using independent finite-period indexing
    total=total_x=total_y=total_x2=0
    for n in range(r*P):
        x=vs[n//r]
        y=vs[((n+h)//r)%P]
        total+=x*y;total_x+=x;total_y+=y;total_x2+=x*x
    meanx=Q(total_x,r*P)
    meany=Q(total_y,r*P)
    finite=Q(total,r*P)-meanx*meany
    predicted=covariance(p,a,h)
    assert abs(finite-predicted)<Q(3*(L+1)**2,p**L),(p,a,h,finite,predicted)
    print(f'cov p={p},a={a},h={h}, depth={L}: finite={float(finite):.9f}, limit={float(predicted):.9f}')
    n_mom+=r*P
print('cyclic p-adic moment tuples checked',n_mom)
print('all checks passed')
