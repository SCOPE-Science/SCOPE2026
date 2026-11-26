"""Exact and numerical verification of quadratic spherical gradient-cap spectra.

Requires Python 3 with sympy, scipy, and numpy. Run: python verify.py
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.special import beta
from numpy.polynomial.legendre import leggauss

u, d = sp.symbols('u d', real=True, positive=True)
a, b = sp.Rational(1, 2), (d-1)/2
q = {
    'Z': u*(1-u),
    'M': 1+(d-6)*u+4*u**2,
    'T': (1-u)*(d-1+2*u),
}
mu_n = lambda n: sp.prod((a+j)/(a+b+j) for j in range(n))
mean = {k: sp.factor(sum(sp.expand(p).coeff(u,n)*mu_n(n) for n in range(3))) for k,p in q.items()}
for k, target in {
    'Z': (d-1)/(d*(d+2)),
    'M': 2*(d-1)/(d+2),
    'T': (d-1)*(d+1)/(d+2),
}.items():
    assert sp.factor(mean[k]-target)==0,(k,mean[k],target)
normalized={k: sp.factor(q[k]/mean[k]) for k in q}
expected={
    ('Z','M'): ((d+2)/(d-1), -2*(d+2)/(d-1)),
    ('Z','T'): (2*(d+2)/(d+1), -2*(d+2)/(d+1)),
    ('M','T'): ((d-3)*(d+2)/((d-1)*(d+1)), 4*(d+2)/((d-1)*(d+1))),
}
# The equality below directly verifies the beta-density derivative antiderivative.
for (i,j),(c0,c1) in expected.items():
    A,B=-c0,-c1
    symbolic_density_derivative = sp.Rational(1,2)*A + (
        sp.Rational(3,2)*B-d/2*A)*u - ((d+2)/2)*B*u*u
    assert sp.factor(symbolic_density_derivative - (normalized[i]-normalized[j])) == 0
print('PASS: all symbolic means and exact spectral gap identities')

def eval_branch(D,s,key):
    aa,bb=0.5,(D-1)/2
    poly=sp.lambdify(u,normalized[key].subs(d,D),'numpy')
    den=beta(aa,bb)
    def integrand(y):
        # y=1-u handles concentration intervals near the polar poles.
        return poly(1-y)*(1-y)**(aa-1)*y**(bb-1)/den
    return quad(integrand,0,1-s,epsabs=2e-12,epsrel=1e-12)[0]

for D in (3,4,5,7,12):
    for s in (0.08,0.36,0.5,0.71,0.91):
        E={k:eval_branch(D,s,k) for k in q}
        W=s**0.5*(1-s)**((D-1)/2)/beta(0.5,(D-1)/2)
        gaps={
            ('Z','M'):W*(D+2)/(D-1)*(1-2*s),
            ('Z','T'):W*2*(D+2)/(D+1)*(1-s),
            ('M','T'):W*(D+2)/((D-1)*(D+1))*(D-3+4*s),
        }
        for (i,j),right in gaps.items():
            assert abs(E[i]-E[j]-right)<3e-11,(D,s,i,j,E[i]-E[j],right)
        assert E['Z']>E['T'] and E['M']>E['T']
        if s<0.5:assert E['Z']>E['M']
        if s>0.5:assert E['M']>E['Z']
print('PASS: 125 numerical beta-integral branch evaluations and all gap signs')

# Independent coordinate-level Gram calculation on S^2. Not based on q-polynomials.
# Basis: x_3^2-1/3, x_3 x_1, x_3 x_2, x_1^2-x_2^2, 2 x_1 x_2.
A=np.zeros((5,3,3))
A[0]=np.diag([-1/3,-1/3,2/3]); A[1,0,2]=A[1,2,0]=0.5
A[2,1,2]=A[2,2,1]=0.5
A[3]=np.diag([1,-1,0]); A[4,0,1]=A[4,1,0]=1.

nodes,weights=leggauss(96)
phis=(np.arange(128)+0.3)*2*np.pi/128


def gram_coordinate(intervals):
    G=np.zeros((5,5))
    for lo,hi in intervals:
        zs=(hi-lo)*nodes/2+(hi+lo)/2
        wz=(hi-lo)*weights/2
        for z,w in zip(zs,wz):
            r=np.sqrt(1-z*z)
            x=np.column_stack((r*np.cos(phis),r*np.sin(phis),np.full(128,z)))
            Ax=np.einsum('kij,nj->kni',A,x)
            f=np.einsum('kij,ni,nj->kn',A,x,x)
            gradient=2*(Ax-f[:,:,None]*x[None,:,:])
            G+=(w/(2*128))*np.einsum('kni,lni->kl',gradient,gradient)
    return G
G0=gram_coordinate([(-1.,1.)]);
assert np.max(np.abs(G0-np.diag(np.diag(G0))))<3e-13
for t in (0.2,0.5,2**-0.5,0.8,0.95):
    G=gram_coordinate([(-1.,-t),(t,1.)])
    ev=np.linalg.eigvalsh(G/np.sqrt(np.diag(G0))[:,None]/np.sqrt(np.diag(G0))[None,:])
    s=t*t
    theory=sorted([eval_branch(3,s,'Z')]+[eval_branch(3,s,'M')]*2+[eval_branch(3,s,'T')]*2)
    assert np.max(np.abs(ev-theory))<5e-12,(t,ev,theory)
print('PASS: 5 independent 5x5 direct spherical-gradient Gram integrations')

for D in (3,4,6,10):
    s=1-1e-5
    E={key:eval_branch(D,s,key) for key in q}
    ratio=E['M']/E['T']
    predicted=(D+1)/(2*(1-s))
    assert abs(ratio/predicted-1)<2e-4,(D,ratio,predicted)
print('PASS: sharp thin-cap condition-number coefficient')
