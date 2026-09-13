"""Script W: block-triangular certificate. Order modes: low (|.|<=K) + high.
M = [A B; C D] with D = high-high block. If ||D|| < 0.9 - margin in a SUITABLE
(anisotropic) norm, resonances >= 0.9 come only from A (finite matrix, rigorous
perturbation). The correct high-block norm: high modes are those with large
STABLE frequency (contracted by dynamics => P SMOOTHS them: ||D|| small in
anisotropic norm). Quantify with diagonal weight W(j) = (1+|ju|)^p (1+|js|)^q...:
for OUTPUT high-stable modes, weight large => W D W^{-1} small IFF P maps high-stable
outputs to ... hmm P e_k has output at j with M[j,k]; high-stable j outputs come from
inputs k with k ≈ Df^T j (large, since Df^T EXPANDS stable covectors? NO: Df^T
contracts stable covectors: |Df^T j_s| <= 0.22|j_s| -- small input k produces HIGH
stable output j: those matrix elements are LARGE (order 1), not decaying!
So in fact ||D|| is NOT small in ANY diagonal Fourier weight: anisotropic spaces use
CANCELLATION (integration along stable leaves), not diagonal weights. A diagonal-weight
certificate is impossible in principle. Record this structural fact + pivot:
finite-section needs off-diagonal (leafwise-averaging) correction = Ulam-on-foliation.
Practical rigorous alternative within budget: certify via COUPLED-MAP / covering
relations? Also insufficient for explicit 0.9.
Honest quantitative statement: compute high-stable mass explicitly: for input
k=0 (constant), |M[j,0]| = |int conj(e_j(f(y)))dy|: j=(j1,0,0)-type stable-heavy
outputs. Evaluate row for a few j to show mass ~ O(1) at high stable modes."""
import numpy as np, math
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
w,P=np.linalg.eigh(Amat); es=P[:,0]
a,b=0.03,0.02
def f(y):
    z=np.stack([y[...,0]+a*np.sin(2*np.pi*y[...,1]),y[...,1]+b*np.sin(2*np.pi*y[...,2]),y[...,2]],axis=-1)%1
    return (z@Amat.T)%1
N=28
g=np.linspace(0,1,N,endpoint=False)
X,Y,Z=np.meshgrid(g,g,g,indexing='ij'); grid=np.stack([X,Y,Z],axis=-1); Fy=f(grid)
def Mj0(j):
    return abs(np.exp(-2j*np.pi*np.einsum('...d,d->...',Fy,np.array(j,float))).mean())
print("stable covector direction ~",np.round(es,3))
for j in [(1,0,0),(2,0,0),(3,0,0),(4,0,0),(0,1,0),(0,0,1),(5,0,0),(6,0,0),(1,1,0),(2,2,0)]:
    print(f"  j={j}: |M[j,0]|={Mj0(j):.4f}")
