#!/usr/bin/env python3
"""Exact checks and independently sampled diagnostics for a stochastic pollen donor-run model.

All exact claims use Fraction; simulations are illustrative only.
"""
from fractions import Fraction as F
from math import comb
from random import Random

checks=0

def test(condition, message):
    global checks
    if not condition: raise AssertionError(message)
    checks += 1

def geo_moment(rho, tau, m):
    z=(1-rho)**m
    return tau*z/(1-(1-tau)*z)

def all_same(rho,tau,m):
    moments=[geo_moment(rho,tau,j) for j in range(m+1)]
    num=sum(((-1)**j)*comb(m,j)*moments[j] for j in range(m+1))
    return num/(1-moments[m])

def geometric_parameters(rho,tau):
    alpha=rho/(rho+tau*(1-rho))
    h=(2*alpha-rho)/(2-rho)
    return alpha,h

for ir in range(1,24):
    rho=F(ir,25)
    for it in range(1,22):
        tau=F(it,23)
        a,h=geometric_parameters(rho,tau)
        mu=geo_moment(rho,tau,1)
        nu=geo_moment(rho,tau,2)
        hp=a/(2-a)
        test(0<rho<a<1, "interior donor concentration")
        test(a/(2-a)<h<a, "sharp attainable wedge")
        test(a==1-mu, "mean first-donor mass")
        test(h==(1-2*mu+nu)/(1-nu), "same-sire moment law")
        test(h-hp==2*(nu-mu*mu)/((1-nu)*(1+mu)), "variance correction")
        test(h==all_same(rho,tau,2), "second moment from general spectrum")
        recover_rho=2*(a-h)/(1-h)
        recover_tau=recover_rho*(1-a)/(a*(1-recover_rho))
        test(recover_rho==rho and recover_tau==tau, "two-statistic inverse")
        for m in (1,2,3,4,5,6):
            mm=geo_moment(rho,tau,m)
            exact=all_same(rho,tau,m)
            test(0<exact<=1, "higher same-sire probability bounds")
            test(exact==(sum((-1)**j*comb(m,j)*geo_moment(rho,tau,j) for j in range(m+1)))/(1-mm), "higher-moment recurrence")
            test(exact*(1-mm)==sum((-1)**j*comb(m,j)*geo_moment(rho,tau,j) for j in range(m+1)), "higher-moment balance")

# Arbitrary iid positive run lengths, not just geometric: nonnegative exact variance correction.
for w in range(1,15):
    for r in range(1,15):
        rho=F(r,16)
        q=1-rho
        # independent run lengths in {1,2,4}, all with positive probabilities
        probs=[F(w,20),F(15-w,20),F(5,20)]
        mom=lambda m: sum(probs[j]*q**(m*L) for j,L in enumerate((1,2,4)))
        mu,nu=mom(1),mom(2)
        a=1-mu
        H=(1-2*mu+nu)/(1-nu)
        pooled=a/(2-a)
        test(sum(probs)==1, "probabilities")
        test(H-pooled==2*(nu-mu*mu)/((1-nu)*(1+mu)),"general variance correction")
        test(H>pooled, "strict gap for variable residence")
        for m in (2,3,4,5):
            numer=sum((-1)**j*comb(m,j)*mom(j) for j in range(m+1))
            exact=numer/(1-mom(m))
            test(0<exact<1, "nongeometric all-same bound")
            for k in (1,2,3):
                truncated=numer*sum(mom(m)**i for i in range(k))
                test(exact-truncated==exact*mom(m)**k,"exact finite-prefix remainder")

# Deterministic run length is the exact equality case.
for length in range(1,10):
    for numerator in range(1,14):
        q=F(numerator,15)
        y=q**length
        a=1-y
        H=(1-2*y+y*y)/(1-y*y)
        test(H==a/(2-a), "deterministic equality")

# Independent Monte Carlo checks with one simulated actual residence history per fruit.
rng=Random(0x2A3B4C)
for rho,tau in ((.5,.5),(.2,.7),(.75,.3)):
    target_alpha,target_h=(float(z) for z in geometric_parameters(F(str(rho)),F(str(tau))))
    empirical_1=empirical_h=0.
    trials=24000
    for _ in range(trials):
        residual=1.
        rank=0
        sumsq=0.
        first=0.
        while residual>1e-11:
            L=1
            while rng.random()>tau:
                L+=1
            Y=(1-rho)**L
            w=residual*(1-Y)
            if rank==0: first=w
            rank+=1
            sumsq+=w*w
            residual*=Y
        empirical_1+=first
        empirical_h+=sumsq
    empirical_1/=trials
    empirical_h/=trials
    test(abs(empirical_1-target_alpha)<0.014,"independent randomized first-donor diagnostic")
    test(abs(empirical_h-target_h)<0.014,"independent randomized same-sire diagnostic")

print('PASS',checks,'assertions; geometric inversion, arbitrary residence laws, higher moments, simulations')

def extremal_nu(q,mu):
    assert 0<mu<=q<1
    k=1
    while not q**(k+1)<=mu<=q**k:
        k+=1
    return k, (q**k+q**(k+1))*mu-q**(2*k+1), q*mu

def H_of(mu,nu):
    return (1-2*mu+nu)/(1-nu)

# Sharp lower/upper laws for fixed pooled donor profile and fixed carryover.
for iq in range(2,14):
    q=F(iq,15)
    for k in range(1,11):
        for iw in range(1,10):
            w=F(iw,10)
            mu=w*q**k+(1-w)*q**(k+1)
            actual_nu=w*q**(2*k)+(1-w)*q**(2*k+2)
            ka,low,up=extremal_nu(q,mu)
            test(actual_nu==low, 'two-adjacent-residence exact extremizer')
            test(low<=up, 'extremal window')
            test(H_of(mu,low)>= (1-mu)/(1+mu),'lower bound at least pooled match')
            test(H_of(mu,low)<H_of(mu,up), 'positive sharp variation window')
            for N in (k+3,k+7):
                p=(mu-q**N)/(q-q**N)
                # N>k+1 means q**N<mu, so p is physical
                nuN=p*q*q+(1-p)*q**(2*N)
                test(0<p<1 and low<=nuN<up, 'distant-residence legal upper approach')
                test(H_of(mu,low)<=H_of(mu,nuN)<H_of(mu,up), 'exact risk interval')

# Finite discrete distributions arbitrary support: verify lattice lower envelope.
for q in (F(1,4), F(1,2), F(2,3), F(4,5)):
    for i in range(1,10):
        probs=[F(i,20),F(10-i,20),F(5,20),F(5,20)]
        lengths=[1,3,5,9]
        mu=sum(p*q**n for p,n in zip(probs,lengths))
        nu=sum(p*q**(2*n) for p,n in zip(probs,lengths))
        k,lo,hi=extremal_nu(q,mu)
        test(lo<=nu<hi, 'arbitrary residence lattice bounds')
        test(H_of(mu,lo)<=H_of(mu,nu)<H_of(mu,hi), 'arbitrary residence paternity bounds')

# The fixed q=1/2, fixed mu=1/3 example has exact distinct lower, geometric, upper values.
q=F(1,2); mu=F(1,3)
_,lo,hi=extremal_nu(q,mu)
test(H_of(mu,lo)==F(11,21), 'illustrative sharp minimum')
test(H_of(mu,hi)==F(3,5), 'illustrative unattained supremum')
test(geometric_parameters(F(1,2),F(1,2))[1]==F(5,9), 'illustrative geometric mechanism')
print('PASS', checks, 'total assertions including sharp integer-residence extremal bounds')
