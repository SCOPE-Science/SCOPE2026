"""Symbolic identities and finite-horizon checks for a killed resetting walk.
Scientific scope: finite checks support, but do not prove, the asymptotic theorem.
"""
from fractions import Fraction
import math
import sympy as sp

h,t=sp.symbols('h t', positive=True)
p=4/(4+h*h)
q=h*h/(4+h*h)
R=(4+h*h)/(4*h)
eps=2-h
lam=1/R
z=R*sp.sqrt(1-t*t)
H=(1-t)/(2*q*z)
F=p*(h-1)*z/(2-H)+q*z*H
assert sp.simplify(F.subs(t,0)-1)==0
assert sp.simplify(sp.diff(F,t).subs(t,0)+h/(2*(h-1)))==0
assert sp.simplify((p*eps*R/(R-1))-4/eps)==0
assert sp.simplify(H.subs(t,0)-2/h)==0
G_sqrt_amplitude=sp.sqrt(2)*(h-1)/h
single_amplitude=sp.simplify((p*eps*R/(R-1))*G_sqrt_amplitude/sp.sqrt(sp.pi))
uniform_amplitude=sp.simplify(single_amplitude/(2-H.subs(t,0)))
assert sp.simplify(single_amplitude-4*sp.sqrt(sp.Rational(2,1)/sp.pi)*(h-1)/(eps*h))==0
assert sp.simplify(uniform_amplitude-2*sp.sqrt(sp.Rational(2,1)/sp.pi)/eps)==0

# Exact arithmetic on the finite set of states reachable in n steps from a fixed state.
# Note resetting to arbitrarily large states is infinite; use exact recurrence for mass at 0,
# via first-return generating coefficients truncated at n (not a cut-off state space).
def exact_survival_masses(eps, nmax):
    p=Fraction(4,1)/(4+(2-eps)**2)
    q=1-p
    # h[z] is the first-hitting generating function from state 1 to 0.
    # h(z)=p z + q z h(z)^2, hence h[2m+1]=Catalan(m)*p^(m+1)*q^m.
    hit=[Fraction(0)]*(nmax+1)
    for m in range((nmax-1)//2+1):
        hit[2*m+1]=Fraction(math.comb(2*m,m),m+1)*p**(m+1)*q**m
    # Compute G(z) from F(z)=p(1-eps)z/(2-H(z))+q z H(z).
    # geometric series 1/(2-H)=sum_{k>=0}H^k/2^{k+1}.
    geom=[Fraction(0)]*(nmax+1)
    geom[0]=Fraction(1,2)
    for n in range(1,nmax+1):
        geom[n]=sum(hit[j]*geom[n-j] for j in range(1,n+1))/2
    F=[Fraction(0)]*(nmax+1)
    for n in range(1,nmax+1):
        F[n]=p*(1-eps)*geom[n-1]+q*hit[n-1]
    G=[Fraction(0)]*(nmax+1)
    G[0]=1
    for n in range(1,nmax+1):
        G[n]=sum(F[j]*G[n-j] for j in range(1,n+1))
    S=[Fraction(1)]*(nmax+1)
    for n in range(1,nmax+1):
        S[n]=S[n-1]-p*eps*G[n-1]
    # Separately build mass at state 0 from exact transitions
    # (truncation of resets beyond n is irrelevant for return by time n).
    state=[Fraction(0)]*(nmax+2)
    state[0]=1
    independent=[Fraction(1)]
    killed=Fraction(0)
    assert G[0]==state[0]
    for n in range(1,nmax+1):
        killed += p*eps*state[0]
        nxt=[Fraction(0)]*(nmax+2)
        for i,m in enumerate(state):
            if m==0: continue
            if i>0: nxt[i-1]+=p*m
            if i+1<len(nxt): nxt[i+1]+=q*m
            if i==0:
                for j in range(len(nxt)):
                    nxt[j]+=p*(1-eps)*m*Fraction(1,2**(j+1))
        state=nxt
        # Mass that can reach 0 in n steps never requires resets to states >n.
        independent.append(1-killed)
        assert state[0]==G[n], (n,state[0],G[n])
        assert independent[n]==S[n], (n,independent[n],S[n])
    # State truncation omits mass in distant reset states, but cannot change
    # return probabilities within nmax steps or the separately accumulated escape mass.
    assert all(S[n]-S[n-1]==-p*eps*G[n-1] for n in range(1,nmax+1))
    return S,G

for e in (Fraction(1,2),Fraction(1,3),Fraction(4,5)):
    S,G=exact_survival_masses(e,13)
    assert all(0<S[n]<S[n-1] for n in range(1,len(S)))

# An independent moving-window mass computation, with no time-series generating functions.
# State tail is truncated after n+140: tails reaching 0 are beyond machine precision.
import numpy as np
for eps_num in (0.5,0.8):
    hnum=2-eps_num; pnum=4/(4+hnum*hnum); qnum=1-pnum
    lnum=4*hnum/(4+hnum*hnum)
    nmax=750 if eps_num==0.5 else 280
    M=nmax+150
    geometric=2.0**(-np.arange(M)-1)
    state=np.zeros(M)
    state[:min(1075,M)]=geometric[:min(1075,M)]
    S0=state.sum()
    assert abs(S0-1)<1e-13
    amplit=2*math.sqrt(2/math.pi)/eps_num
    checks=[]
    for n in range(1,nmax+1):
        nxt=np.zeros_like(state)
        nxt[:-1] += pnum*state[1:]
        nxt[1:] += qnum*state[:-1]
        nxt += pnum*(1-eps_num)*state[0]*geometric
        state=nxt
        if n in (100,200,nmax):
            estimate=amplit*lnum**n/math.sqrt(n)
            checks.append((n, float(state.sum()/estimate)))
    assert abs(checks[-1][1]-1)<.04, checks
    print('uniform_eps',eps_num,'asymptotic_ratios',checks)
print('VERIFY_OK symbolic_critical_identities=6 exact_renewal_cases=3 floating_mass_cases=2')
