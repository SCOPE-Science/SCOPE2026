#!/usr/bin/env python3
"""Diagnostics for Gaussian triangle laws; not an infinite proof.
The accompanying analytic inequalities are the proof.
"""
import math
from scipy.integrate import quad
from scipy.special import erf, gamma, ndtri
from scipy.stats import qmc
import numpy as np
mu=math.sqrt(2/math.pi)
a=mu-1/math.sqrt(math.pi)
var=1/6+(math.sqrt(3)-2)/math.pi
f=lambda z: math.exp(-z*z/2)/math.sqrt(math.pi)+(z/math.sqrt(2))*math.erf(z/math.sqrt(2))
fp=quad(lambda z:2*math.exp(-z*z/2)/math.sqrt(2*math.pi)*f(z)**3,0,12,epsabs=1e-12)[0]
fm=3/(2*math.sqrt(2*math.pi))
lb=mu**3+(3*mu-a)*var
assert lb>fm+0.08
assert 0.14914<fp-fm<0.14917
# One signed triangle, with all-positive versus one-negative links.
z=ndtri(qmc.Sobol(d=3,scramble=True,seed=210).random_base2(18))
u=z/np.linalg.norm(z,axis=1)[:,None]
w_bal=np.abs(u[:,0]-u[:,1])+np.abs(u[:,1]-u[:,2])+np.abs(u[:,2]-u[:,0])
w_unbal=np.abs(u[:,0]-u[:,1])+np.abs(u[:,1]-u[:,2])+np.abs(u[:,2]+u[:,0])
observed=float(np.mean(w_unbal**3-w_bal**3))
expected=6*float(gamma(1.5)/gamma(3))*(fp-fm)
assert abs(observed-expected)<0.004,(observed,expected)
print('SIGNED_ACYCLOTOPE_THIRD_MOMENT_PASS', 'Fplus',round(fp,12),'Fminus',round(fm,12),'observed',round(observed,7),'expected',round(expected,7))
