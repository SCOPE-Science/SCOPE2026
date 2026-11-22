"""Independent numerical and finite combinatorial checks of discrete path heat BV-L1 theory.
Requires numpy and scipy. Run: python check.py
The analytical proof, not these finite checks, establishes all-size claims.
"""
import numpy as np
from scipy.linalg import expm
from math import sin, pi


def laplacian(n):
    L=np.zeros((n,n))
    for i in range(n-1):
        L[i,i]+=1;L[i+1,i+1]+=1
        L[i,i+1]-=1;L[i+1,i]-=1
    return L


def coefficient(n,t,k):
    r=np.arange(1,n)
    lam=4*np.sin(np.pi*r/(2*n))**2
    return 4/n*np.sum(np.sin(np.pi*r*k/n)**2*(-np.expm1(-lam*t))/lam)


def walk_counts(n,m,k):
    A=np.zeros((n-1,n-1),dtype=object)
    for i in range(n-2): A[i,i+1]=A[i+1,i]=1
    power=np.eye(n-1,dtype=object)
    for _ in range(m): power=power@A
    return int(power[k-1,k-1])

count=0
for n in range(2,32):
    L=laplacian(n)
    for t in (0.003,0.04,0.3,1.2,6.0):
        P=expm(-t*L)
        errs=[]
        for k in range(1,n):
            u=np.arange(n)>=k
            a=np.sum(np.abs(P@u-u))
            b=coefficient(n,t,k)
            assert abs(a-b)<2e-10,('spectral mismatch',n,t,k,a,b)
            errs.append(a)
            count+=1
        center=(n-1)//2
        assert max(errs)-errs[center]<2e-10,(n,t,errs)
        assert all(errs[j]<errs[j+1]+2e-10 for j in range(center-1))
        if n%2 and n>=3:
            assert abs(errs[center]-errs[center-1])<2e-10
    # test arbitrary signed inputs against best step bound
    t=0.25
    P=expm(-t*L)
    C=coefficient(n,t,n//2)
    rng=np.random.default_rng(1000+n)
    for _ in range(300):
        f=rng.normal(size=n)
        assert np.sum(np.abs(P@f-f)) <= C*np.sum(np.abs(np.diff(f)))+1e-9
        count+=1
print('FINITE_MATRIX_SPECTRAL_SHARPNESS_AND_BV_INEQUALITY_PASS',count)

count=0
for n in range(3,13):
  for m in range(0,17):
    vals=[walk_counts(n,m,k) for k in range(1,n)]
    assert vals==vals[::-1]
    for k in range(1,(n-1)//2):
      assert vals[k-1] <= vals[k]
    count+=1
print('EXACT_INTEGER_ADJACENCY_BRIDGE_CHECK_PASS',count)

for t in (.003,.05,.25,1.,4.):
  continuum=4/np.pi**2*sum((1-np.exp(-np.pi**2*(2*j+1)**2*t))/(2*j+1)**2 for j in range(15000))
  ratios=[coefficient(n,n*n*t,n//2)/n for n in [16,32,64,128,256]]
  assert abs(ratios[-1]-continuum)<0.003,(t,ratios,continuum)
  print('CONTINUUM_SCALING',t,'coefficient',continuum,'finite',ratios)
print('ALL_NEW_DISCRETE_REFLECTING_HEAT_CHECKS_PASS')
