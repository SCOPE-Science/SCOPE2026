"""Numerical and algebraic checks for the marked rare-obtuse ball-triangle law.
Run: python verify_ball_obtuse.py. Requires numpy and scipy.
Finite tests support, but do not replace, the proof in RESULT.md.
"""
import math
import numpy as np
from scipy.special import gammaln

RNG = np.random.default_rng(196982)
S = np.array([[1., 1/3, 1/3], [1/3, 1., -1/3], [1/3, -1/3, 1.]])
SINV = np.array([[1.5, -.75, -.75], [-.75, 1.5, .75], [-.75, .75, 1.5]])
M = np.array([[45/8, 27/8, 27/8], [27/8, 9/2, 9/4], [27/8, 9/4, 9/2]])
assert np.allclose(S @ SINV, np.eye(3), atol=1e-14)
assert abs(np.linalg.det(S)-16/27) < 1e-14
assert abs(np.linalg.det(M)-2187/64) < 1e-12
assert np.linalg.eigvalsh(M).min() > 0
assert np.allclose(2*np.linalg.inv(M)[0,0],8/9)
assert abs(math.sqrt(6)/4 - (3 * (16/27)**(-2) * (4/3)**3 * (32*math.sqrt(3)*math.pi**1.5/81) / (8*(2*math.pi)**1.5))) < 1e-12
print('GRAM_DETERMINANT_HESSIAN_CONSTANT_OK')

for dimension, acute_expected in [(2, 4/math.pi**2-1/8), (3,33/70)]:
    sample_size=400000
    g=RNG.standard_normal((sample_size,3,dimension))
    g /= np.linalg.norm(g, axis=2)[:,:,None]
    radius=RNG.random((sample_size,3))**(1/dimension)
    vertices=g*radius[:,:,None]
    a,b,c=vertices[:,0,:],vertices[:,1,:],vertices[:,2,:]
    obt_a=np.einsum('ij,ij->i',b-a,c-a) < 0
    obt_b=np.einsum('ij,ij->i',a-b,c-b) < 0
    obt_c=np.einsum('ij,ij->i',a-c,b-c) < 0
    assert not np.any((obt_a.astype(int)+obt_b.astype(int)+obt_c.astype(int))>1)
    acute=np.mean(~(obt_a | obt_b | obt_c))
    print('dimension',dimension,'acute simulation',acute,'published',acute_expected)
    assert abs(acute-acute_expected)<.008
print('FINITE_DIMENSION_SANITY_OK')

# Independent finite-d importance integral of exact Gram density. Proposal is
# precisely the limiting six-mark density, with a truncation preserving t>=0.
# This is not an asymptotic proof and does not assert finite-d accuracy.
d=10000
N=250000
cov=2*np.linalg.inv(M)
tpq=RNG.multivariate_normal(np.zeros(3),cov,size=N)
tpq[:,0]=np.abs(tpq[:,0])
t,p,q=tpq.T
z,u,v=RNG.exponential(scale=4/3,size=(3,N))
a=1-t/np.sqrt(d); b=1-u/d; c=1-v/d
ab=1/3+p/np.sqrt(d); ac=1/3+q/np.sqrt(d)
bc=-a+ab+ac-z/d
D=a*b*c+2*ab*ac*bc-a*bc**2-b*ac**2-c*ab**2
Q=45*t*t/8+27*t*(p+q)/4+9*(p*p+p*q+q*q)/2
ok=(D>0)&(a>0)&(b>0)&(c>0)
weight=np.zeros(N)
weight[ok]=np.exp(((d-4)/2)*(np.log(D[ok])-math.log(16/27))+.75*(z[ok]+u[ok]+v[ok])+Q[ok]/4)
J=(4/3)**3*32*math.sqrt(3)*math.pi**1.5/81
log_Id=(math.log(8*math.pi**1.5)-3*math.log(d)+gammaln((d-1)/2)+gammaln((d-2)/2)-2*gammaln(d/2))
ratio=math.exp(math.log(3*J)-4.5*math.log(d)-2*math.log(16/27)-log_Id-math.log(math.sqrt(6)/4))*np.mean(weight)
# Numeric rearrangement above normalizes by the prediction, while avoiding tiny exponents.
relerr=np.std(weight)/np.mean(weight)/np.sqrt(N)
print('importance d',d,'ratio to asymptotic',ratio,'relative MC standard error',relerr)
assert 0.97 < ratio < 1.22 and relerr < .02
print('EXACT_GRAM_IMPORTANCE_CHECK_OK')
