"""Reproducible exact finite-depth and limiting-moment checks for scalar paired Neumann sums.

Uses only the Python standard library. All finite-depth checks use exact rational
arithmetic; numerical bisection is diagnostic, not a substitute for uniqueness proofs.
"""
from fractions import Fraction as F
from itertools import product
from math import isclose, sqrt


def theoretical_finite(a, s, tau, depth):
    """Return variance of half sum by exact second-moment recursions."""
    mu, qplus, qminus, cross = F(0), F(0), F(0), F(0)
    for _ in range(depth):
        new_plus = 1 + 2*a*mu + (a*a+s)*qplus
        new_minus = 1 + 2*a*mu + (a*a+tau*tau*s)*qminus
        new_cross = 1 + 2*a*mu + (a*a-tau*s)*cross
        mu, qplus, qminus, cross = 1+a*mu, new_plus, new_minus, new_cross
    return (qplus+qminus+2*cross)/4-mu*mu


def exact_enumeration(a, support, tau, depth):
    """Support is [(probability, centered perturbation)]."""
    mean=F(0); second=F(0)
    for sample in product(support, repeat=max(0,depth-1)):
        prob=F(1); plus=minus=F(1); sumplus=summinus=F(1)
        for p,e in sample:
            prob *= p
            plus *= a+e
            minus *= a-tau*e
            sumplus+=plus
            summinus+=minus
        val=(sumplus+summinus)/2
        mean+=prob*val
        second+=prob*val*val
    return second-mean*mean


def theoretical_infinite(a,s,tau):
    B=1-a*a
    assert s>0 and B>s and 0<=tau<=1
    return s/(4*(1-a)**2) * (1/(B-s) + tau*tau/(B-s*tau*tau) -2*tau/(B+s*tau))


def tau_opt(a,s):
    nu=float(s/(1-a*a))
    lo,hi=0.,1.
    for _ in range(90):
        u=(lo+hi)/2
        if nu*u**4+nu*u**3+u-1<0: lo=u
        else: hi=u
    return ((lo+hi)/2)**2


def run():
    cases=[(F(1,2),[(F(1,2),F(1,4)),(F(1,2),-F(1,4))]),
           (F(1,3),[(F(1,3),F(2,5)),(F(2,3),-F(1,5))])]
    count=0
    for a,support in cases:
        assert sum((p for p,e in support),F(0))==1
        assert sum((p*e for p,e in support),F(0))==0
        s=sum((p*e*e for p,e in support),F(0))
        assert s>0 and s<1-a*a
        for depth in range(1,9):
            for tau in [F(0),F(1,4),F(1,2),F(4,5),F(1)]:
                lhs=exact_enumeration(a,support,tau,depth)
                rhs=theoretical_finite(a,s,tau,depth)
                assert lhs==rhs, (a,support,tau,depth,lhs,rhs)
                count+=1
        for tau in [F(0),F(1,4),F(1,2),F(4,5),F(1)]:
            assert abs(float(theoretical_finite(a,s,tau,400)-theoretical_infinite(a,s,tau))) < 1e-12
            count+=1
        t=tau_opt(a,s)
        B=float(1-a*a); sv=float(s)
        derivative=2*B*(t/(B-sv*t*t)**2-1/(B+sv*t)**2)
        assert 0<t<1 and abs(derivative)<2e-12
        tvar=float(theoretical_infinite(a,s,F(t)))
        assert tvar < float(theoretical_infinite(a,s,F(1)))
        assert tvar < float(theoretical_infinite(a,s,F(0)))
        count+=3
    # A coupled (perfectly correlated across modes) diagonal-Hessian test:
    # squared Euclidean risk still sums the modewise variance formulas.
    a1,a2=F(1,2),F(1,3)
    e1,e2=F(1,4),-F(1,5)
    m=6
    for tau in [F(0),F(1,3),F(3,4),F(1)]:
        expected=4*theoretical_finite(a1,e1*e1,tau,m)+theoretical_finite(a2,e2*e2,tau,m)
        observed=F(0)
        means=(2*sum(a1**j for j in range(m)),
               -sum(a2**j for j in range(m)))
        for signs in product((-1,1),repeat=m-1):
            sums=[]
            for a,e,b in ((a1,e1,2),(a2,e2,-1)):
                pp=pm=F(1);sp=sm=F(1)
                for sign in signs:
                    pp*=a+e*sign; pm*=a-tau*e*sign
                    sp+=pp; sm+=pm
                sums.append(b*(sp+sm)/2)
            observed+=sum((x-y)**2 for x,y in zip(sums,means))/2**(m-1)
        assert observed==expected
        count+=1
    # Nontrivial concrete example and strict optimum, with exact endpoints.
    a=F(1,2); s=F(1,16)
    opt=tau_opt(a,s)
    assert isclose(opt,0.7908174685347105,rel_tol=0,abs_tol=2e-12)
    assert theoretical_infinite(a,s,F(1))==F(4,143)
    assert theoretical_infinite(a,s,F(0))==F(1,11)
    assert isclose(float(theoretical_infinite(a,s,F(opt))),0.02223659007176057,rel_tol=0,abs_tol=2e-12)
    count+=4
    # Golden-ratio endpoint; polynomial at unit variance ratio factors
    # exactly as (u^2+1)(u^2+u-1).
    golden_tau=(3-sqrt(5))/2
    for nu in [0.9,0.99,0.999,0.99999]:
        # choose a=1/2; s=nu*(1-a^2)
        t=tau_opt(F(1,2),F(nu)*(F(3,4)))
        assert t>golden_tau and t<1
        count+=1
    near=tau_opt(F(1,2),F('0.99999999')*F(3,4))
    assert abs(near-golden_tau)<5e-9
    count+=1
    print('PASS:', count, 'exact-enumeration, recurrence, limiting, optimizer and boundary checks')
    print('example mirror strength:',f'{opt:.15f}')
    print('example variances:',f'{float(theoretical_infinite(a,s,F(opt))):.15f}',
          f'{float(theoretical_infinite(a,s,F(1))):.15f}')

if __name__=='__main__':
    run()
