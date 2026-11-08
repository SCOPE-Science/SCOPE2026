"""Exact rational checks for two-community optimal coordinate sampling.

Run: python3 verify.py
Uses only the Python standard library. Numerical experiments are not a proof
of the formula for arbitrary parameters or dimensions.
"""
from fractions import Fraction as Q
from itertools import product
import random


def design(p, q, a, b, c):
    a, b, c = Q(a), Q(b), Q(c)
    assert p >= 2 and q >= 2 and 0 < a < 1 and 0 < b < 1 and c > 0
    u, v = (1-a)/p, (1-b)/q
    r, s = a+u, b+v
    delta = r*s-c*c
    assert delta > 0
    t0 = v/(u+v)
    tq = (s+c)/(r+s+2*c)
    rq = delta/(r+s+2*c)
    if c*c <= a*b:
        t, rho, phase = t0, u*t0, 'contrast'
    elif tq < t0 and rq > u*tq:
        t = (a*s-c*c)/(a*s-c*c+a*u)
        rho, phase = u*t, 'first-contrast/radial'
    elif tq > t0 and rq > v*(1-tq):
        t = b*v/(b*r-c*c+b*v)
        rho, phase = v*(1-t), 'second-contrast/radial'
    else:
        t, rho, phase = tq, rq, 'radial'
    assert 0 < t < 1 and rho > 0
    return t, rho, phase


def correlation(p,q,a,b,c):
    n=p+q
    return [[Q(1) if i==j else Q(a) if i<p and j<p else
             Q(b) if i>=p and j>=p else Q(c) for j in range(n)]
            for i in range(n)]


def pencil(C, probs, rate):
    n=len(probs)
    return [[probs[i]*probs[j]*C[i][j] - (rate*probs[i] if i==j else Q(0))
             for j in range(n)] for i in range(n)]


def is_psd(M, require_strict=False):
    M=[list(row) for row in M]
    while len(M):
        if any(M[i][i]<0 for i in range(len(M))): return False
        pivot=next((i for i in range(len(M)) if M[i][i]>0),None)
        if pivot is None:
            return not require_strict and all(z==0 for row in M for z in row)
        d=M[pivot][pivot]
        keep=[i for i in range(len(M)) if i!=pivot]
        M=[[M[i][j]-M[i][pivot]*M[pivot][j]/d for j in keep] for i in keep]
    return True


def verify():
    rng=random.Random(104729)
    values=[Q(1,6), Q(1,5), Q(1,4), Q(1,3), Q(2,5), Q(1,2), Q(3,5), Q(2,3), Q(3,4)]
    phase_counts={}
    checked=0
    exact_inequalities=0
    all_examples=[]
    for p in range(2,7):
        for q in range(2,7):
            for a,b,c in product(values, repeat=3):
                u,v=(1-a)/p,(1-b)/q
                if (u+a)*(v+b)<=c*c: continue
                t,rho,phase=design(p,q,a,b,c)
                phase_counts[phase]=phase_counts.get(phase,0)+1
                n=p+q
                C=correlation(p,q,a,b,c)
                probs=[t/p]*p+[(1-t)/q]*q
                if not is_psd(pencil(C,probs,rho)):
                    raise AssertionError(('attainment',p,q,a,b,c,phase,t,rho))
                checked+=1
                # Strictly better rates are impossible at sampled feasible designs.
                for k in (1,2,3,7,11,17,23):
                    t_test=Q(k,29)
                    probs_test=[t_test/p]*p+[(1-t_test)/q]*q
                    if is_psd(pencil(C,probs_test,rho),require_strict=True):
                        raise AssertionError(('block bound',p,q,a,b,c,k))
                    exact_inequalities+=1
                if checked % 37 == 0:
                    # Test a non-block-invariant law against the global certificate.
                    ints=[rng.randrange(1,30) for _ in range(n)]
                    z=sum(ints)
                    ps=[Q(j,z) for j in ints]
                    if is_psd(pencil(C,ps,rho),require_strict=True):
                        raise AssertionError(('global bound',p,q,a,b,c))
                    exact_inequalities+=1
                if p==q==2 and (a,b,c) in (
                    (Q(1,5),Q(1,5),Q(1,5)),
                    (Q(1,5),Q(1,5),Q(1,4)),
                    (Q(1,5),Q(2,5),Q(1,3)),
                    (Q(2,5),Q(1,5),Q(1,3))):
                    all_examples.append((str(a),str(b),str(c),str(t),str(rho),phase))
    # Independent unbounded-gain sequence; full SPD and uniform attainability.
    for q in range(2,25):
        a,b,c=1-Q(1,q*q),Q(1,2),Q(1,4)
        t,rho,phase=design(2,q,a,b,c)
        assert phase=='contrast' and rho==Q(1,2*q*(q+1))
        C=correlation(2,q,a,b,c)
        assert is_psd(pencil(C,[Q(1,q+2)]*(q+2),Q(1,q*q*(q+2))))
    return checked,exact_inequalities,phase_counts,all_examples

if __name__=='__main__':
    n,ineq,phases,examples=verify()
    print('Exact attainment cases:',n)
    print('Exact non-improvement checks:',ineq)
    print('Phase coverage:',phases)
    print('Four rational witnesses:',examples)
    print('Unbounded-gain sequence checked for 2 <= q <= 24')
    print('PASS')
