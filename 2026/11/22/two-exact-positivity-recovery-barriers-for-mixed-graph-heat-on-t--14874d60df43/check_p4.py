"""Numerical corroboration of exact spectral identities for four-vertex path heat."""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq

L=np.array([[1.,-1.,0.,0.],[-1.,2.,-1.,0.],[0.,-1.,2.,-1.],[0.,0.,-1.,1.]])
sq2=math.sqrt(2.0)
g=1/math.sqrt(2.0)
def rates(eta):
    return ((2-sq2)*(1+eta*(2-sq2)),2+4*eta,(2+sq2)*(1+eta*(2+sq2)))
def spectral(eta,t):
    a,b,c=rates(eta)
    A,B,C=math.exp(-a*t),math.exp(-b*t),math.exp(-c*t)
    return 1+B-(1+g)*A-(1-g)*C,1-B-g*(A-C),1-B+g*(A-C),1-A+B-C+g*(A-C)
def root(eta,i):
    lo=max(eta*1e-5,1e-12) if eta<1 else 1e-9/eta
    # If formula cancellation near 0, find stable negative point by sampling
    ts=np.logspace(-9,3,1600)/max(1,eta)
    negative=[t for t in ts if spectral(eta,t)[i] < -1e-13]
    assert negative, (eta,i)
    lo=negative[-1]; hi=lo*1.25
    while spectral(eta,hi)[i] <=0: hi*=1.5
    return brentq(lambda t: spectral(eta,t)[i],lo,hi,xtol=1e-15)

rng=np.random.default_rng(42324)
n=0
for eta in [0.005,0.03,0.2,0.5,1,3,20,100]:
    Q=L+eta*L@L
    for t in np.geomspace(0.002/max(1,eta),12/max(1,eta),50):
        S=expm(-t*Q)
        f,gg,edge1,edge2=spectral(eta,t)
        assert np.max(abs(4*np.array([S[0,3],S[0,2],S[0,1],S[1,2]])-np.array([f,gg,edge1,edge2])))<2e-11
        assert edge1>0 and edge2>0
        assert np.min(np.diag(S))>0
        n+=1
    t2,t3=root(eta,1),root(eta,0)
    for i,r in [(1,t2),(0,t3)]:
        assert spectral(eta,r*0.9)[i]<0 and spectral(eta,r*1.1)[i]>0
    print('eta',eta,'distance_two_zero',round(t2,9),'end_to_end_zero',round(t3,9))
assert abs(root(0.005,1)/0.005-2)<0.2
assert abs(root(0.005,0)/0.005-6)<0.3
print('EXACT_SPECTRAL_FORMULAS_NUMERICALLY_REPLAYED',n)
print('TWO_DISTINCT_SIGN_CROSSING_TESTS_PASS')
print('ASYMPTOTIC_SMALL_PARAMETER_SANITY_PASS')
