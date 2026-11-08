"""Standalone checks of an intrinsic distance-histogram inversion theorem.
Run: python torus_distance_verifier.py
Uses only standard library, mpmath and numpy; numerical tests supplement the proof.
"""
import math
from fractions import Fraction as F
import numpy as np
import mpmath as mp

# Exact scalar moments of W=U^2, U uniform on [-1,1].
r=[F(1,2*j+1) for j in range(1,4)]
k1=r[0]
k2=r[1]-r[0]**2
k3=r[2]-3*r[1]*r[0]+2*r[0]**3
assert (k1,k2,k3)==(F(1,3),F(4,45),F(16,945))

# Distinct rectangular 3-tori with identical first two even-distance moments.
p=[F(1),F(2),F(3)]
q=[F(17,7),F(19,7),F(6,7)]
assert sum(p)==sum(q) and sum(x*x for x in p)==sum(x*x for x in q)
assert sum(x**3 for x in p)!=sum(x**3 for x in q)

# First three cumulants recover the three positive s_i exactly via Newton identities.
def cumulants(s):
    return (k1*sum(s), k2*sum(t*t for t in s),k3*sum(t**3 for t in s))
def polynomial(s):
    a,b,c=cumulants(s)
    v1=a/k1; v2=b/k2; v3=c/k3
    return (v1,(v1*v1-v2)/2,(v1**3-3*v1*v2+2*v3)/6)
for s in [p,q,[F(1),F(1),F(1)],[F(1,5),F(9,7),F(41,2)]]:
    a,b,c=polynomial(s)
    for t in s: assert t**3-a*t*t+b*t-c==0

# MGF identity 2z F'(z)+F(z)=exp(z); all complex zeros are simple.
mp.mp.dps=50
def fun(z):
    return mp.hyp1f1(mp.mpf('.5'),mp.mpf('1.5'),z)
def der(z):
    return mp.diff(fun,z)
assert abs(2*mp.mpc('1.3','0.7')*der(mp.mpc('1.3','0.7'))+fun(mp.mpc('1.3','0.7'))-mp.e**mp.mpc('1.3','0.7')) < mp.mpf('1e-35')
roots=[]
for re in range(-7,9,2):
    for im in range(1,26,2):
        try:
            root=mp.findroot(fun,(mp.mpc(re,im),mp.mpc(re+mp.mpf('.2'),im+mp.mpf('.2'))),tol=mp.mpf('1e-38'),maxsteps=80)
        except (ValueError,ZeroDivisionError): continue
        if abs(fun(root))>mp.mpf('1e-25'):continue
        if root.imag<0: root=mp.conj(root)
        if not any(abs(root-w)<mp.mpf('1e-17') for w in roots): roots.append(root)
roots.sort(key=abs)
assert roots and all(abs(der(z))>mp.mpf('1e-7') for z in roots)

# Independent Monte Carlo direct nearest-integer torus distances vs independent centered coordinates.
rng=np.random.default_rng(21721)
n=120000
lengths=np.array([1.7,2.2,3.6])
x=rng.random((n,3))*lengths
y=rng.random((n,3))*lengths
z=np.abs(x-y)
z=np.minimum(z,lengths-z)
d2=np.sum(z*z,axis=1)
s=np.square(lengths/2)
theo=[float(sum(s)/3),float((4/45)*sum(s*s))]
emp=[float(np.mean(d2)),float(np.var(d2))]
assert abs(emp[0]-theo[0])<.025 and abs(emp[1]-theo[1])<.05,(theo,emp)
print('VERIFY_OK exact_cumulants=3 exact_inverse_shapes=4 exact_two_moment_counterexample=1 complex_zero_samples=%s monte_carlo_pairs=%s'% (len(roots),n))
print('NEAREST_FOUND_ZERO=',mp.nstr(roots[0],24))
print('POPULATION_MEAN_VARIANCE=',theo)
print('SAMPLED_MEAN_VARIANCE=',emp)
