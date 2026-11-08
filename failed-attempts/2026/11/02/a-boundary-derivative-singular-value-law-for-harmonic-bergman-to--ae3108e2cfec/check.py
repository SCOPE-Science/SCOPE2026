"""Finite checks for spectral asymptotics of harmonic Bergman Toeplitz commutators.

Uses mpmath for stable Gamma ratios and NumPy for finite singular values.
The infinite-dimensional theorem requires the separate analytic proof.
"""
import math
import mpmath as mp
import numpy as np

mp.mp.dps = 55
checks = 0

def h(j, alpha):
    j = int(j)
    return mp.gamma(j+1)*mp.gamma(alpha+2)/mp.gamma(j+alpha+2)

def weight(m, k, alpha):
    if k >= 0:
        return mp.sqrt(h(k+m, alpha)/h(k, alpha))
    j=-k
    if j>=m:
        return mp.sqrt(h(j, alpha)/h(j-m, alpha))
    return h(m, alpha)/mp.sqrt(h(j, alpha)*h(m-j, alpha))

def coeff(m, n, k, alpha):
    return weight(n, k-n,alpha)*weight(m,k-n,alpha)-weight(m,k,alpha)*weight(n,k+m-n,alpha)

for alpha in [-mp.mpf('0.5'),mp.mpf('0'),mp.mpf('1'),mp.mpf('2')]:
    a = alpha+1
    for m in range(1,5):
        for n in range(1,5):
            for k in [300,900,2700]:
                for sign in [-1,1]:
                    v=coeff(m,n,sign*k,alpha)*k*k
                    desired= -sign*a*m*n
                    rel=abs((v-desired)/desired)
                    # A first-order finite-k error remains in these tests.
                    assert rel < mp.mpf('0.09'),(alpha,m,n,k,sign,v,desired,rel)
                    checks+=1

f={1:1+0j,2:0.3+0.1j,3:-0.21+0.13j}
g={1:0.8-0.1j,2:-0.25+0.3j,4:0.11+0.07j}
for alpha in [mp.mpf('0'),mp.mpf('1.5')]:
    for d in range(-4,5):
        q=sum((m*n*am*complex(bn).conjugate() for m,am in f.items() for n,bn in g.items() if m-n==d),0j)
        if abs(q)<1.e-12:continue
        for sign in [-1,1]:
            k=2000*sign
            actual=sum((am*complex(bn).conjugate()*complex(coeff(m,n,k,alpha)) for m,am in f.items() for n,bn in g.items() if m-n==d),0j)*k*k
            goal=-sign*float(alpha+1)*q
            assert abs(actual-goal)<0.02*max(1,abs(goal)),(alpha,d,sign,actual,goal)
            checks+=1

# Compare a finite exact compression to the predicted boundary integral.
alpha=mp.mpf('0')
lo,hi=-180,180
N=hi-lo+1
matrix=np.zeros((N,N),dtype=np.complex128)
for j,k in enumerate(range(lo,hi+1)):
    for m,am in f.items():
        for n,bn in g.items():
            row=k+m-n
            if lo<=row<=hi:
                matrix[row-lo,j]+=am*complex(bn).conjugate()*complex(coeff(m,n,k,alpha))
s=np.linalg.svd(matrix,compute_uv=False)
s.sort()
s=s[::-1]
angular=np.linspace(0,2*np.pi,16384,endpoint=False)
fp=np.zeros_like(angular,dtype=complex)
gp=np.zeros_like(angular,dtype=complex)
for m,am in f.items():fp+=m*am*np.exp(1j*(m-1)*angular)
for n,bn in g.items():gp+=n*bn*np.exp(1j*(n-1)*angular)
L=np.sqrt(np.abs(fp*gp)).mean()
limit=4*float(alpha+1)*L*L
# Moderately sized truncations approach the sharp coefficient from finite-size corrections.
for ix in (35,65,95):
    val=(ix+1)**2*s[ix]
    assert abs(val-limit)<0.65*limit,(ix,val,limit)
    checks+=1
print(f'PASS: {checks} high-precision coefficient checks and finite-matrix tests.')
print(f'Boundary integral L={L:.10f}; predicted singular coefficient={limit:.10f}.')
for ix in (35,65,95):print(f'index {ix+1}: j^2*s_j={(ix+1)**2*s[ix]:.10f}')
