"""Reproducibility checks for cardinal cubic spline variation coefficient.

Python standard library only. The theorem and its infinite-dimensional
argument are proved in RESULT.md; finite checks are supplementary.
"""
from decimal import Decimal, getcontext
from math import sqrt
from random import Random

getcontext().prec = 70
one = Decimal(1)
s3 = Decimal(3).sqrt()
qD = Decimal(2) - s3
rD = qD.sqrt()
AD = Decimal(3) * (one - qD)
tD = (one - rD) / (one + qD)
HD = tD * (one - tD) * ((Decimal(2) - qD) - (one + qD)*tD)
KD = (Decimal(2)+s3+Decimal(2)*rD)/Decimal(3)
assert abs(qD*qD-4*qD+1) < Decimal('1e-65')
assert Decimal(0)<qD<Decimal('0.5')
assert Decimal(0)<tD<1
assert abs(HD-(s3-1+2*rD)/6) < Decimal('1e-65')
assert abs(KD-(1+2*HD)) < Decimal('1e-65')
assert abs(KD-(1+4*(AD/6)*HD/(1-qD))) < Decimal('1e-65')
assert 1-AD/6>0
print('ALGEBRAIC_COEFFICIENT_AND_PEAK_IDENTITIES_PASS')

q=float(qD); A=float(AD); K=float(KD)
def second_derivative_step(i, jump_edge= -1):
    # Unit step at knot jump_edge+1, zero on its left.
    if i <= jump_edge:
        return A*(-q)**(jump_edge-i)
    return -A*(-q)**(i-jump_edge-1)

def diff_step(i, edge=-1):
    return 1.0 if i==edge else 0.0

for e in [-5,-1,0,4]:
    for i in range(e-24,e+25):
        lhs=(second_derivative_step(i-1,e)+4*second_derivative_step(i,e)
             +second_derivative_step(i+1,e))
        rhs=6*(diff_step(i,e)-diff_step(i-1,e))
        assert abs(lhs-rhs)<1e-10, (e,i,lhs,rhs)
print('CARDINAL_SECOND_DERIVATIVE_GREEN_RECURRENCE_PASS')

def cubic_tv_in_cell(y0,y1,M0,M1):
    # S(t)=y0 + c*t + b*t**2 + a*t**3 on [0,1].
    a=(M1-M0)/6.0
    b=M0/2.0
    c=(y1-y0)-(2*M0+M1)/6.0
    roots=[]
    if abs(a)>1e-15:
        disc=(2*b)**2-12*a*c
        if disc>=0:
            roots=[(-2*b-sqrt(disc))/(6*a),(-2*b+sqrt(disc))/(6*a)]
    elif abs(b)>1e-15:
        roots=[-c/(2*b)]
    pts=sorted(set([0.0,1.0]+[z for z in roots if 1e-13<z<1-1e-13]))
    val=lambda x:y0+c*x+b*x*x+a*x**3
    return sum(abs(val(t)-val(s)) for s,t in zip(pts,pts[1:]))

def total_variation_of_finite_steps(weights, edge_min=-48, edge_max=48):
    out=0.0
    for i in range(edge_min,edge_max):
        y0=sum(v for e,v in weights.items() if e<i)
        y1=sum(v for e,v in weights.items() if e<i+1)
        M0=sum(v*second_derivative_step(i,e) for e,v in weights.items())
        M1=sum(v*second_derivative_step(i+1,e) for e,v in weights.items())
        out+=cubic_tv_in_cell(y0,y1,M0,M1)
    return out

for edge in [-6,-1,0,6]:
    tv=total_variation_of_finite_steps({edge:1.0})
    assert abs(tv-K)<2e-10, (edge,tv,K)
print('DIRECT_PIECEWISE_CUBIC_STEP_VARIATION_VS_CLOSED_FORM_PASS')

rng=Random(11991)
for _ in range(500):
    weights={e:rng.uniform(-1,1) for e in range(-7,8) if rng.random()<0.4}
    if not weights:
        continue
    observed=total_variation_of_finite_steps(weights)
    bound=K*sum(abs(v) for v in weights.values())
    assert observed <= bound+1e-9,(observed,bound)
print('RANDOM_FINITE_STEP_SUPERPOSITION_VARIATION_BOUND_PASS 500')
print('SHARP_BV_CONSTANT',format(KD,'.15f'))
print('ALL_CARDINAL_SPLINE_BV_CHECKS_PASS')
