"""Numerical and symbolic consistency checks for Gaussian one-step sketched projection laws.

The theorem is proved analytically in RESULT.md; these checks test identities,
constants, distributional predictions, and finite Gaussian simulations.
"""
import math
from fractions import Fraction
import numpy as np
from scipy.special import gamma, betainc
from scipy.integrate import quad

assertions=0

def verify(condition, message):
    global assertions
    assert condition, message
    assertions+=1

# Exact Schur/orthogonal decomposition for a non-eigenvector on a 2x2 SPD matrix.
A=np.array([[2.,1.],[1.,2.]])
b=np.array([1.,0.])
alpha=float(b@A@b)
r=A@b-alpha*b
beta=np.linalg.norm(r)
gamma2=float((A@b)@(A@b))
verify((alpha,beta,gamma2)==(2.,1.,5.),'example parameters')
verify(np.linalg.eigvalsh(A).min()>0,'SPD')
verify(np.isclose(gamma2,alpha**2+beta**2),'orthogonal energy')

# Density, sign probability and tail constant (s=3 have elementary closed forms).
for s in [1,2,3,4,5,8,15]:
    eta=beta**2/gamma2
    f0=gamma((s+1)/2)/(math.sqrt(math.pi)*gamma(s/2)*beta) * eta**((s+1)/2)
    def f(h):
        return gamma((s+1)/2)/(math.sqrt(math.pi)*gamma(s/2)*beta) * (1+((h-alpha)/beta)**2)**(-(s+1)/2)
    pn=0.5*betainc(s/2,0.5,eta)
    numeric_p=quad(f,-math.inf,0,epsabs=1e-11)[0]
    verify(abs(numeric_p-pn)<2e-10,f'wrong sign s={s}')
    for threshold in [50.,500.,5000.]:
        prob=quad(f,-1/threshold,1/threshold,epsabs=1e-12)[0]
        verify(abs(threshold*prob/(2*f0)-1)<1e-2,f'tail asymptotic s={s}')
    if s==3:
        verify(abs(f0-2/(25*math.pi))<1e-12,'exact density at zero')
        exact_p=(math.asin(1/math.sqrt(5))-2/5)/math.pi
        verify(abs(pn-exact_p)<1e-12,'exact sign probability')
    if s>2:
        var_c=beta**2/(gamma2**2*(s-2))
        risk=beta**2/gamma2*(s-1)/(s-2)
        verify(abs(risk-(beta**2/gamma2+gamma2*var_c))<1e-12,'variance-residual identity')

# Cross-check direct sketched two-dimensional FOM and GMRES computations, including
# normal regression decompositions and perturbation of sketch normalization.
rng=np.random.default_rng(20260319)
s=5
N=300000
S=rng.normal(size=(N,s,2))
X=S[:,:,0]
W=2*X+S[:,:,1]
D=np.sum(X*W,axis=1)
c_f=np.sum(X*X,axis=1)/D
c_g=np.sum(X*W,axis=1)/np.sum(W*W,axis=1)
R=np.linalg.norm(X,axis=1)
Z=np.sum(X*S[:,:,1],axis=1)/R
verify(np.allclose(c_f,1/(alpha+beta*Z/R),rtol=1e-10,atol=1e-10),'FOM regression identity')
verify(abs(np.mean(c_g)-alpha/gamma2)<0.004,'GMRES coefficient mean')
verify(abs(np.var(c_g)-beta**2/(gamma2**2*(s-2)))<0.003,'GMRES coefficient variance')
resid=(1-alpha*c_g)**2+(beta*c_g)**2
verify(abs(np.mean(resid)-(beta**2/gamma2*(s-1)/(s-2)))<0.012,'GMRES residual risk')
wrong=np.mean(D<0)
expect=0.5*betainc(s/2,0.5,beta**2/gamma2)
verify(abs(wrong-expect)<0.003,'wrong-sign probability')
verify(np.all(np.isfinite(c_f)) and np.all(np.isfinite(c_g)),'well defined almost surely in finite draws')

# Elementary infinite-moment witness: symmetric density remains bounded below
# near h=0, while integral h^{-p} dh diverges for p>=1.
s=3
c0=gamma((s+1)/2)/(math.sqrt(math.pi)*gamma(s/2)*beta)*(beta**2/gamma2)**((s+1)/2)
for p in [1,2,3]:
    divergent=[2*c0*math.log(1/d) if p==1 else 2*c0*(d**(1-p)-1)/(p-1) for d in [1e-2,1e-3,1e-4]]
    verify(divergent[0]<divergent[1]<divergent[2],f'p={p} divergence')

print('PASS:',assertions,'assertions; exact density/sign/tail and Gaussian solver checks')
print('example alpha=2 beta=1 gamma2=5; s=3 sign probability=',(math.asin(1/math.sqrt(5))-2/5)/math.pi)
print('example s=3 FOM tail constant=',4/(25*math.pi))
print('example s=3 GMRES expected squared residual=',2/5)
print('simulation s=5 negative Ritz probability=',wrong,' theoretical=',expect)
print('simulation s=5 GMRES risk=',float(np.mean(resid)),' theoretical=',4/15)
