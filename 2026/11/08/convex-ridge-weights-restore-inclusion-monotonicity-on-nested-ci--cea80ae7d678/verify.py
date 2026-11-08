"""Numerical diagnostic checks for weighted perimeters of nested disks.
Only Python standard library; finite checks are not a proof.
"""
import math
import random

N = 1024
COS = [math.cos(2*math.pi*j/N) for j in range(N)]

def projected_relu(a, r, threshold):
    t=(threshold-a)/r
    if t>=1: return 0.0
    if t<=-1: return 2*math.pi*r*(a-threshold)
    return 2*r*r*(math.sqrt(1-t*t)-t*math.acos(t))

def direct_relu(a,r,threshold):
    return 2*math.pi*r*sum(max(a+r*u-threshold,0) for u in COS)/N

def power_perimeter(c,r,p):
    return 2*math.pi*r*sum((max(0,c*c+r*r+2*c*r*u))**(p/2) for u in COS)/N

rng=random.Random(20261103)
number=0
for _ in range(800):
    a=rng.uniform(-3,3);r=rng.uniform(.1,3);threshold=rng.uniform(-5,5)
    exact=projected_relu(a,r,threshold)
    approx=direct_relu(a,r,threshold)
    assert abs(exact-approx)<.00025*max(1,exact), (exact,approx)
    number+=1

for _ in range(1200):
    a=rng.uniform(-5,5); r=rng.uniform(.15,3)
    delta=rng.uniform(.0005,1.5); shifted=a+rng.uniform(-delta,delta)
    threshold=rng.uniform(-6,6)
    assert projected_relu(shifted,r+delta,threshold)+1e-10>=projected_relu(a,r,threshold)
    number+=1

for _ in range(700):
    a=rng.uniform(0,6);r=rng.uniform(.1,2);delta=rng.uniform(.01,1.5)
    shifted=abs(a+rng.uniform(-delta,delta))
    p=rng.choice([1,1.25,1.5,2,2.5,3,4,5,8,12])
    assert power_perimeter(shifted,r+delta,p)+1e-8>=power_perimeter(a,r,p)
    number+=1

# Spherical-cap truncation genuinely reverses the comparison.
r,t,a=1.,1.,2.
epsilon=.01
b=a-epsilon
R=r+epsilon
q=(t*t-b*b-R*R)/(2*b*R)
length_B=2*R*math.acos(q)
length_A=2*math.pi*r
assert length_B < length_A
# Asymptotic sqrt-epsilon coefficient for the cap loss.
for eps in [1e-4,1e-6,1e-8]:
    b=a-eps;R=r+eps
    q=(t*t-b*b-R*R)/(2*b*R)
    ratio=(2*R*math.acos(q)-2*math.pi*r)/math.sqrt(eps)
    assert abs(ratio+4*math.sqrt(r*t/a))<.08, ratio
    number+=1
print('passed',number,'diagnostics; negative cap difference',length_B-length_A)
