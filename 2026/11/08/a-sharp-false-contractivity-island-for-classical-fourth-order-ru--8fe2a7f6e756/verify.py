#!/usr/bin/env python3
"""Independent arithmetic checks for a two-state fourth-order time-step norm theorem.

No external dependencies. The analytic proof is in RESULT.md; this code checks its
exact polynomial certificate and explores the norm boundary numerically.
"""
from fractions import Fraction as Q
from math import comb, sqrt, exp

CHECKS = 0

def check(condition, message=''):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(message or f'assertion {CHECKS}')

def add(a,b):
    out = [Q(0)]*max(len(a),len(b))
    for i,x in enumerate(a): out[i]+=x
    for i,x in enumerate(b): out[i]+=x
    return trim(out)

def mul(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return trim(out)

def scale(a,x): return trim([Q(x)*v for v in a])
def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def deriv(a): return trim([i*a[i] for i in range(1,len(a))])
def evaluate(a,x):
    y=Q(0)
    for t in a[::-1]: y=y*x+t
    return y

r=[Q(1),Q(-1),Q(1,2),Q(-1,6),Q(1,24)]
q=[Q(1),Q(-1),Q(1,2),Q(-1,6)]
B=[2304,-4608,5760,-4176,2112,-786,212,-39,4]
check(scale(deriv(r),-1)==q,'r prime equals negative q')
check(scale(deriv(q),-1)==[Q(1),Q(-1),Q(1,2)],'q prime strictly negative')
check(scale(r,24)==add(mul([2,-2,1],[2,-2,1]),scale(add(mul([-2,1],[-2,1]),[1]),4)), 'r is sum of squares')
# Confirm signed derivative numerator is h^3 B/3456.
rr=mul(r,r)
F=add(scale(mul(mul([0,1],r),mul(q,q)),2),scale(mul(add([1],scale(rr,-1)),add(q,mul([0,1],deriv(q)))),-1))
check(scale(F,3456)==mul([0,0,0,1],list(map(Q,B))),'derivative identity')
# Positivity certificate: h=3t/(1+t), positive coefficients after multiplying (1+t)^8.
bernstein=[sum(B[k]*3**k*comb(8-k,j-k) for k in range(j+1)) for j in range(9)]
check(bernstein==[2304,4608,19584,37008,62352,47754,32274,4041,3141],'positive coefficients')
for x in bernstein: check(x>0,'positive Bernstein transform')
# Series coefficient check (h q)*(2+h^2/3) agrees through power 4.
approx=mul(mul([0,1],q),[Q(2),Q(0),Q(1,3)])
diff=add(add([1],scale(rr,-1)),scale(approx,-1))
for k in range(5): check(k>=len(diff) or diff[k]==0,'small-step series')

def rf(h): return 1-h+h*h/2-h**3/6+h**4/24
def qf(h): return 1-h+h*h/2-h**3/6

def bisect(func,a,b,steps=100):
    fa=func(a)
    check(fa*func(b)<=0,'root bracket')
    for _ in range(steps):
        m=(a+b)/2
        fm=func(m)
        if fa*fm<=0: b=m
        else: a=m; fa=fm
    return (a+b)/2

z=bisect(qf,1.0,2.0)
beta=bisect(lambda h:h**3-4*h*h+12*h-24,2.0,3.0)
check(abs(z-1.5960716379833189)<2e-13)
check(abs(beta-2.7852935634052816)<2e-13)

def phi(h): return (1-rf(h)**2)/(h*abs(qf(h)))
def boundaries(g):
    right=bisect(lambda h:phi(h)-g,z+1.e-8,beta-1.e-8)
    left=bisect(lambda h:phi(h)-g,1.e-8,z-1.e-8) if g>2 else 0.0
    return left,right

C=(1-rf(z)**2)/(z*abs(-1+z-z*z/2))
check(abs(C-0.856975420961165)<1e-12)
for g, expected_left,expected_right in [(2,0,1.90050234550749),(4,1.30829119357053,1.77263140475421),(10,1.50139443280599,1.67479277490165)]:
    left,right=boundaries(g)
    check(abs(left-expected_left)<1e-10 and abs(right-expected_right)<1e-10,'boundary values')
    for h in [left,right]:
        if h>0: check(abs(phi(h)-g)<1e-8,'sharp equality')
for g in [100.,1000.,10000.]:
    l,u=boundaries(g)
    check(abs((z-l)*g-C)<0.025,'left high-g asymptotic')
    check(abs((u-z)*g-C)<0.025,'right high-g asymptotic')
for g in [2.000001,2.0001,2.01]:
    left,_=boundaries(g)
    check(abs(left/sqrt(3*(g-2))-1)<0.008,'small bifurcation asymptotic')

def norm2(h,g):
    a=rf(h); d=g*h*qf(h)
    return (sqrt(4*a*a+d*d)+abs(d))/2

for j in range(1,1101):
    h=3*j/1100
    r0=rf(h)
    for g in [0,.25,1,1.9,2,2.01,2.1,3,4,10,20,100]:
        direct=norm2(h,g)<=1
        predicted=(h<=beta and (g==0 or (abs(h-z)<1e-13 or (g*h*abs(qf(h))<=1-r0*r0))))
        check(direct==predicted, f'norm mismatch h={h}, g={g}')
# Exact rational independent determinant characterization for a few finite cases.
for h in [Q(1,10),Q(1,2),Q(1),Q(3,2),Q(2),Q(5,2),Q(3)]:
    for g in [Q(0),Q(1),Q(2),Q(4),Q(10)]:
        rr0=evaluate(r,h); qq0=evaluate(q,h); d=g*h*qq0
        pos=(1-rr0**2)>=0 and (1-rr0**2)**2>=d**2
        check(pos==(float((sqrt(4*float(rr0)**2+float(d)**2)+abs(float(d)))/2)<=1+1e-12),'rational 2x2 criterion')
# Exact exponential grows arbitrarily with g at the blind spot even though numerical matrix is scalar.
for g in [3,10,1000]:
    check(qf(z)**2<1e-28,'derivative zero')
    check(norm2(z,g)<1,'blind spot contraction')
    exact_norm=exp(-z)*(sqrt((g*z)**2+4)+g*z)/2
    check(exact_norm>1 if g>=10 else exact_norm>0,'physical flow')
print('VERIFIER_PASS',CHECKS,'assertions',f'zeta={z:.15f}',f'beta={beta:.15f}',f'C={C:.15f}')
