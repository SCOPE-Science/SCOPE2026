"""Standalone exact and numerical diagnostics for a sigmoid-memory recurrence.

All rigorous conclusions are proved algebraically in RESULT.md; finite trials
exercise identities and boundary cases but are not substitutes for proofs.
Requires Python 3 standard library only.
"""
from fractions import Fraction as Q
import math


def p(y, eta):
    return eta*y*abs(y)/2-y


def step(x, y, z, s1, s2, s3, eta, beta):
    t = beta*x
    if t >= 0:
        sig = 1.0/(1.0+math.exp(-t))
    else:
        et = math.exp(t)
        sig = et/(1.0+et)
    return (s1*sig+s2*s3*x*(eta*abs(y)-1)*(z*z-1),
            y+x, z+s2*x*(eta*abs(y)-1))


def test_exact_coboundary():
    s2, eta = Q(-17,10), Q(7,20)
    total=0
    for y in [Q(-3,2), Q(-1), Q(-1,8), Q(0), Q(1,8), Q(1), Q(3,2)]:
        for x in [Q(-1), Q(-1,4), Q(0), Q(1,4), Q(1)]:
            if y*(y+x)<0:
                continue
            for z in [Q(-5,4), Q(0), Q(9,7)]:
                zp=z+s2*x*(eta*abs(y)-1)
                dq=(zp-s2*p(y+x,eta))-(z-s2*p(y,eta))
                expected=-s2*eta*x*x/2 if y>=0 and y+x>=0 else s2*eta*x*x/2
                assert dq==expected, (y,x,dq,expected)
                total+=1
    return total


def test_sign_and_escape():
    s1,s2,s3,eta,beta=-0.2,-1.7,1.15,0.35,1.0
    state=(0.01,0.01,0.01)
    signs=set()
    maxnorm=0
    for j in range(20000):
        state=step(*state,s1,s2,s3,eta,beta)
        assert all(math.isfinite(v) for v in state)
        maxnorm=max(maxnorm,max(map(abs,state)))
        if state[1]>0: signs.add('+')
        if state[1]<0: signs.add('-')
    assert signs=={'+','-'} and maxnorm<3, (signs,maxnorm)
    for beta in [-3.,-1.,0.,1.,3.]:
        for s1 in [-.2,.2]:
            delta=abs(s1)/(1+math.exp(abs(beta*s1)))
            state=(0.3,-1.7,0.4)
            for j in range(200):
                state=step(*state,s1,-1.7,0.,.35,beta)
                if j>=1: assert state[0]*s1>0 and abs(state[0])>=delta-1e-14
    return maxnorm


def main():
    total=test_exact_coboundary()
    maxnorm=test_sign_and_escape()
    print('exact one-sided coboundary identities: PASS',total,'rational tests')
    print('finite bounded and zero-feedback diagnostics: PASS; maximum sampled norm',round(maxnorm,6))
    print('Proof of the theorem is analytic, not computational.')

if __name__=='__main__':main()
