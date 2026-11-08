#!/usr/bin/env python3
"""Exact-rational spot checks for a randomized theta-method stability result.

The accompanying mathematical proof, not these finite checks, establishes
universal assertions and the infinite-domain stability statements.
"""
from fractions import Fraction as Q

checks = 0

def check(condition, label='identity'):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(f'{label} (check #{checks})')


def modulus_squared(x, y, theta):
    # z=-x+iy, R=(1+(1-theta)z)/(1-theta*z)
    return ((1-(1-theta)*x)**2+(1-theta)**2*y*y)/((1+theta*x)**2+theta*theta*y*y)


def two_point_factor(x,y,a,b,p):
    return p*modulus_squared(x,y,a)+(1-p)*modulus_squared(x,y,b)


def pcritical(a,b):
    alpha = 2*b-1
    beta = 1-2*a
    return alpha*a*a/(beta*b*b+alpha*a*a)

# For complex z=-x+iy, |R|^2-1 equals
# (-2x+(1-2theta)*(x^2+y^2))/(1+2theta*x+theta^2*(x^2+y^2)).
T = (Q(0),Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(1))
for theta in T:
    for x in (Q(0),Q(1,17),Q(1,2),Q(3)):
        for y in (Q(0),Q(1,7),Q(3,2),Q(20)):
            qq=x*x+y*y
            D=1+2*theta*x+theta*theta*qq
            check(modulus_squared(x,y,theta)-1 == (-2*x+(1-2*theta)*qq)/D, 'one-stage identity')

# Two-atom imaginary-axis numerator is A+B*y^2 exactly.
for a,b in ((Q(1,4),Q(3,4)),(Q(1,10),Q(3,5)),(Q(1,3),Q(1)),(Q(2,5),Q(9,10))):
    pc=pcritical(a,b)
    pm=(2*b-1)/(2*(b-a))
    check(0<pc<pm<1, 'strict comparison p_critical < p_mean')
    for p in (Q(0),pc/2,pc,(pc+pm)/2,pm,Q(1)):
        A=p*(1-2*a)+(1-p)*(1-2*b)
        B=p*(1-2*a)*b*b+(1-p)*(1-2*b)*a*a
        for y in (Q(1,10),Q(1),Q(7),Q(100)):
            q=y*y
            f=two_point_factor(Q(0),y,a,b,p)
            check(f-1 == q*(A+B*q)/((1+a*a*q)*(1+b*b*q)), 'imaginary-axis identity')
        check((B<=0) == (p<=pc), 'sharp probability cutoff')
        # At the cutoff, the large-frequency mean-square gain is exactly one.
    check(pc*((1-a)/a)**2+(1-pc)*((1-b)/b)**2 == 1, 'high-frequency equality')

# Entire finite grid is stable for p at/below the threshold; this is
# only a finite check (the proof uses a subharmonic maximum principle).
a=Q(1,4);b=Q(3,4);pc=Q(1,10)
check(pcritical(a,b)==pc, 'example probability')
for p in (Q(0),Q(1,20),pc):
    for x in (Q(1,1000),Q(1,10),Q(1),Q(10),Q(100)):
        for y in (Q(0),Q(1,100),Q(1),Q(10),Q(100)):
            check(two_point_factor(x,y,a,b,p)<1, 'stable parameter sample')
for p in (Q(11,100),Q(1,2),Q(3,4)):
    check(two_point_factor(Q(1),Q(1000),a,b,p)>1, 'unstable high-frequency sample')

# For symmetric centered Bernoulli theta values a=1/2-d, b=1/2+d:
# N=4*d^2*q^2+(4*d^2-1)*x*q-4*x*(1+x),
# where 2*(F-1)*D_a*D_b=N.
for d in (Q(1,20),Q(1,8),Q(1,4),Q(2,5)):
    a=Q(1,2)-d;b=Q(1,2)+d
    for x in (Q(0),Q(1,100),Q(1,2),Q(3)):
        for y in (Q(0),Q(1,10),Q(1),Q(5)):
            q=x*x+y*y
            Da=1+2*a*x+a*a*q
            Db=1+2*b*x+b*b*q
            N=4*d*d*q*q+(4*d*d-1)*x*q-4*x*(1+x)
            check(2*(two_point_factor(x,y,a,b,Q(1,2))-1)*Da*Db==N,'centered exact boundary')
    # The local boundary coefficient equals d^2.
    M2=(a*a+b*b)/2
    M3=(a*a*a+b*b*b)/2
    check(M3-M2/2 == d*d, 'weak-damping boundary coefficient')

# Every tested nonconstant rational distribution with mean 1/2 has
# F(iy)>1, and positive coefficient kappa=2E[theta^3]-E[theta^2].
centred_laws=(
    ((Q(1,4),Q(3,4)),(Q(1,2),Q(1,2))),
    ((Q(0),Q(1)),(Q(1,2),Q(1,2))),
    ((Q(1,5),Q(1,2),Q(4,5)),(Q(1,4),Q(1,2),Q(1,4))),
    ((Q(1,10),Q(7,10)),(Q(1,3),Q(2,3))),
)
for nodes, weights in centred_laws:
    check(sum(weights)==1 and sum(t*w for t,w in zip(nodes,weights))==Q(1,2),'centering')
    kap=sum(w*(2*t**3-t**2) for t,w in zip(nodes,weights))
    check(kap>0, 'positive fourth-order coefficient')
    for y in (Q(1,100),Q(1,4),Q(1),Q(100)):
        F=sum(w*modulus_squared(Q(0),y,t) for t,w in zip(nodes,weights))
        check(F>1,'imaginary-axis instability')

# Uniform theta has fourth-order coefficient kappa=1/6,
# reproducing the previously established x~y^4/12 law.
check(2*Q(1,4)-Q(1,3)==Q(1,6), 'uniform coefficient')
print(f'PASS: {checks} exact-rational assertions; no infinite claim relies on grid sampling.')
