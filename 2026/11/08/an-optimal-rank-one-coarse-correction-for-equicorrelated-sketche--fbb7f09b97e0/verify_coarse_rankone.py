"""Exact-rational and floating-point checks for the compound-symmetry coarse-correction theorem.

Run with Python 3 and NumPy. All decimal displays are ancillary; the proof is analytic.
"""
from fractions import Fraction as F
import itertools
import numpy as np

checks = 0

def insist(test, explanation):
    global checks
    if not bool(test):
        raise AssertionError(explanation)
    checks += 1

def rational_parameters(q, s, rho, lam, t=2):
    m = q*s
    n = t*m
    a = 1-rho
    c = a+s*rho
    b = a+m*rho
    ha = n*a*(a/F(m)+lam)
    hb = n*b*(b/F(m)+lam)
    da = n*q*a*(a/F(s)+lam)
    dc = n*q*c*(c/F(s)+lam)
    between, within, glob = ha/dc, ha/da, hb/dc
    low = da*hb/ha-dc
    high = dc*(hb/ha-1)
    return (m,n,a,b,c,ha,hb,da,dc,between,within,glob,low,high)

for q,s,rho,lam,t in itertools.product(range(2,8),range(2,7),
    [F(1,10),F(2,5),F(3,4)], [F(1,50),F(1,3),F(2,1)], [2,4]):
    m,n,a,b,c,ha,hb,da,dc,e0,e1,e2,lo,hi = rational_parameters(q,s,rho,lam,t)
    insist(0<e0<e1<e2, 'three spectral levels')
    insist(lo>0 and hi>=lo, 'coarse correction interval')
    insist(e2/e0==hb/ha, 'condition-number nonimprovement')
    insist(e1/e0==dc/da, 'optimal rank-one ratio')
    insist(hb/(dc+lo)==e1, 'lower equality')
    insist(hb/(dc+hi)==e0, 'upper equality')
    insist(hb/(dc+(lo+hi)/2)>=e0 and hb/(dc+(lo+hi)/2)<=e1,
           'interior equality')

for q,s,rho,lam in itertools.product(range(2,5),range(2,5),
    [F(1,4),F(3,5)], [F(1,10),F(2,3)]):
    m,n,a,b,c,ha,hb,da,dc,e0,e1,e2,lo,hi = rational_parameters(q,s,rho,lam)
    # Source-prescribed H and B are formed explicitly, independent of formulas.
    r,l = float(rho),float(lam)
    K = (1-r)*np.eye(m)+r*np.ones((m,m))
    H = (n/m)*(K@K)+l*n*K
    Bs = []
    for j in range(q):
        Q = K[j*s:(j+1)*s,j*s:(j+1)*s]
        Bs.append(n*q*((Q@Q)/s+l*Q))
    B=np.zeros((m,m))
    for j in range(q):B[j*s:(j+1)*s,j*s:(j+1)*s]=Bs[j]
    def condition(M):
        L=np.linalg.cholesky(M)
        eig=np.linalg.eigvalsh(np.linalg.solve(L, H)@np.linalg.inv(L.T))
        return eig
    raw = condition(B)
    target=sorted([float(e0)]*(q-1)+[float(e1)]*(m-q)+[float(e2)])
    insist(np.allclose(raw,target,rtol=2e-12,atol=2e-12),'full eigenvalue list')
    P=np.ones((m,m))/m
    for tau in [float(lo),float((lo+hi)/2),float(hi)]:
        eig = condition(B+tau*P)
        insist(np.isclose(eig[-1]/eig[0],float(dc/da),rtol=2e-12),
               'PSD rank-one attainability')
        inverse_exact=np.linalg.inv(B+tau*P)
        inverse_update=np.linalg.inv(B)-(tau/(float(dc)*(float(dc)+tau)))*P
        insist(np.allclose(inverse_exact,inverse_update,atol=2e-12),
               'Woodbury application identity')
    # Random PSD rank-one choices must respect the proved universal bound.
    for k in range(5):
        vec=np.sin(np.arange(1,m+1)*(k+1.23))
        W=(1+k/2)*np.outer(vec,vec)
        eig=condition(B+W)
        insist(eig[-1]/eig[0] >= float(dc/da)-1e-9,
               'arbitrary PSD rank-one lower bound')

# A small complete rational spectral certificate for the source matrices.
from sympy import Matrix, Rational, eye, ones
for q,s,rho,lam in [(2,2,F(1,2),F(1,10)),(3,2,F(1,4),F(1,3))]:
    m,n,a,b,c,ha,hb,da,dc,e0,e1,e2,lo,hi=rational_parameters(q,s,rho,lam)
    r=Rational(rho.numerator,rho.denominator)
    L=Rational(lam.numerator,lam.denominator)
    K=(1-r)*eye(m)+r*ones(m,m)
    H=Rational(n,m)*(K*K)+L*n*K
    B=Matrix.zeros(m,m)
    for j in range(q):
        S=K[j*s:(j+1)*s,j*s:(j+1)*s]
        T=n*q*(S*S/s+L*S)
        for i in range(s):
            for k in range(s):B[j*s+i,j*s+k]=T[i,k]
    e=((B.inv()*H).eigenvals())
    expected={Rational(z.numerator,z.denominator):k for z,k in
              [(e0,q-1),(e1,m-q),(e2,1)]}
    insist(e==expected,'exact spectrum using sympy')
    t=Rational(lo.numerator,lo.denominator)
    P=ones(m,m)/m
    eigen_corr=((B+t*P).inv()*H).eigenvals()
    insist(set(eigen_corr)=={Rational(e0.numerator,e0.denominator),
           Rational(e1.numerator,e1.denominator)},'exact endpoint degeneracy')

print('PASS',checks,'checks, including exact rational and exact symbolic matrix spectra')
print('example m=4 s=2 rho=1/2 lambda=1/10:')
p=rational_parameters(2,2,F(1,2),F(1,10))
for key,v in zip(['m','n','a','b','c','h_a','h_b','d_a','d_c',
                  'eta_between','eta_within','eta_global','tau_low','tau_high'],p):
    print(key,'=',v)
print('raw condition number',p[6]/p[5],'; optimized',p[8]/p[7])
