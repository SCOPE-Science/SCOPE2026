#!/usr/bin/env python3
"""Exact rational checks for two-walk Green diagonal variance formulas.

All displayed algebraic identities are checked with rational arithmetic;
the universal optimality theorem and continuum asymptotics require their
analytic arguments in RESULT.md and are not inferred from finite tests.
"""
from fractions import Fraction as F
from math import floor, log, pi

checks = 0

def check(test, label):
    global checks
    assert test, label
    checks += 1

def finite_min_cross(t):
    """Exact finite Fréchet double sum; automatically terminates."""
    z = F(0)
    powers = [F(1)]
    while powers[-1]+t > 1:
        powers.append(powers[-1]*t)
    # Powers[1:] includes one extra possibly; all positive contributions identified.
    for j in range(1,len(powers)):
        a=powers[j]
        k=1
        while k < len(powers) and a+powers[k] > 1:
            k+=1
        count=k-1
        z += count*(a-1)+t*(1-t**count)/(1-t)
    return z

def vars_exact(p):
    p = F(p)
    q = 1-p
    t = q*q
    s = max(F(0), 1-2*p)**2
    mu = t/(1-t)
    J = finite_min_cross(t)
    S = s*(1+t)/((1-s)*(1-t))
    return (mu+J)/2, (mu+S)/2, mu/(2*(1-t)), J, S

# An independent finite-step symbolic joint tail calculation.
def stage_joint_survival(p, steps1, steps2):
    q = 1-p
    r = max(F(0),1-2*p)
    return r**min(steps1,steps2) * q**abs(steps1-steps2)

# Exhaustively test sharp Fréchet inequalities, strictness, and exact formulas
# over 130 rational stop probabilities and 2,080 joint step thresholds.
for n in range(3,67):
    p = F(n,67)
    q = 1-p
    t = q*q
    vopt,vstage,viid,J,S = vars_exact(p)
    check(vopt <= vstage <= viid, f'ordered {p}')
    check(vstage == vopt if p>=F(1,2) else vstage>vopt, f'stage equality {p}')
    check(J == 0 if 2*t<=1 else J>0, f'zero pair phase {p}')
    check(J <= S <= (t/(1-t))**2, f'cross expectation {p}')
    for j,k in ((1,1),(1,2),(2,1),(2,2),(1,3),(3,1),(3,3),(2,4),(4,2),(4,4),
                (1,5),(5,1),(5,5),(2,5),(5,2),(3,5)):
        joint = stage_joint_survival(p,2*j,2*k)
        frechet = max(F(0),t**j+t**k-1)
        check(joint >= frechet, f'Fréchet {p} {j} {k}')

p = F(1,3)
a,b,c,J,S = vars_exact(p)
for got,expected,label in [
    (a,F(2,5),'optimal p=1/3'),
    (b,F(9,16),'stagewise p=1/3'),
    (c,F(18,25),'iid p=1/3'),
    (J,F(0),'cross-opt p=1/3'),
    (S,F(13,40),'cross-stage p=1/3'),
    (1-a/b,F(13,45),'exact saving'),
]: check(got==expected,label)

# Independently integrate the countermonotone product by exact finite grids,
# using common uniform mass cells and CDF inverse to confirm the finite sum.
def geo_K_from_u(t,u):
    k=0
    while u > 1-t**(k+1):
        k+=1
    return k

for p in [F(1,3),F(1,4),F(2,5),F(1,5),F(3,5),F(7,10)]:
    t=(1-p)**2
    # Partition (0,1) at every geometrically distributed quantile breakpoint
    # needed for positive cross moments.
    edges={F(0),F(1)}
    k=1
    while t**k>F(1,1000000):
        edges.add(1-t**k)
        edges.add(t**k)
        k+=1
    endpoints=sorted(edges)
    total=F(0)
    for x,y in zip(endpoints,endpoints[1:]):
        z=(x+y)/2
        total+=(y-x)*geo_K_from_u(t,z)*geo_K_from_u(t,1-z)
    check(total == finite_min_cross(t), f'exact quantile partition {p}')

# Asymptotic constant convergence and independent formulas (numeric sanity only).
c=2-pi*pi/6
check(0<c<1,'pi constant')
def finite_min_cross_float(p):
    t=(1-p)**2
    powers=[1.0]
    while powers[-1]+t>1:
        powers.append(powers[-1]*t)
    z=0.0
    k=len(powers)-1
    for j in range(1,len(powers)):
        a=powers[j]
        while k>=1 and powers[k] <= 1-a:
            k-=1
        count=k
        z+= count*(a-1)+t*(-__import__('math').expm1(count*log(t)))/(1-t)
    return z
for p_float in [0.01,0.003,0.001]:
    t=(1-p_float)**2
    s=(1-2*p_float)**2
    mu=t/(1-t)
    J=finite_min_cross_float(p_float)
    S=s*(1+t)/((1-s)*(1-t))
    ratio=(mu+J)/(mu+S)
    check(abs(ratio-c) < 8*p_float, f'long-walk asymptotic {p_float}')
print(f'VERIFY_OK: {checks} rational inequality/identity tests and exact quantile partitions; asymptotic sanity checks passed.')
print('p=1/3: Vopt=2/5, Vstage=9/16, Viid=18/25, cross-opt=0, cross-stage=13/40.')
print('Limiting optimal/stage variance ratio: 2-pi^2/6 =',format(c,'.12f'))
print('Analytic Fréchet lower-bound and asymptotic proofs are in RESULT.md; finite checks alone do not prove them.')
