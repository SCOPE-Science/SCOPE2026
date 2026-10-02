from __future__ import annotations

import math
import numpy as np
import sympy as sp

mu, x, y = sp.symbols('mu x y', real=True)
P = 3 - 3*mu + 3*mu**2 - 2*mu**3
F = 18 + 3*mu*(mu**2-6)*x + 2*mu**2*(6-6*mu+3*mu**2-mu**3)*x**2
b0 = sp.Integer(18)
b1 = 3*(6-6*mu+mu**3)
b2 = 2*(2*mu**2-3*mu+3)*P
bern = sp.expand(b0*(1-y)**2 + 2*b1*y*(1-y) + b2*y**2)
assert sp.expand(bern - F.subs(x, 2*y)) == 0
assert sp.simplify(sp.diff(P, mu) + 3*(2*mu**2 - 2*mu + 1)) == 0
assert P.subs(mu, 1) > 0
assert P.subs(mu, sp.Rational(4,3)) < 0
assert (6-6*mu+mu**3).subs(mu, sp.Rational(4,3)) == sp.Rational(10,27)

roots = [r for r in sp.nroots(2*mu**3-3*mu**2+3*mu-3, n=40, maxsteps=100) if abs(sp.im(r)) < sp.Rational(1,10)**30]
assert len(roots) == 1
mu_star = float(sp.re(roots[0]))
assert 1.0 < mu_star < 4/3

def R3(z):
    return 1 + z + z*z/2 + z*z*z/6

assert abs(R3(-2*mu_star) + 1) < 1e-12

# Direct boundary scan of the origin-tangent disk D(-mu,mu).
for m in [1.0, mu_star, mu_star + 1e-4]:
    theta = np.linspace(0.0, 2*math.pi, 200001)
    z = m*(np.exp(1j*theta)-1.0)
    mx = np.abs(R3(z)).max()
    if m <= mu_star + 1e-14:
        assert mx <= 1 + 2e-11
    else:
        assert mx > 1

# A finite sparse-grid matrix check in two dimensions.
def haar_blocks(N: int):
    n = 2**N
    blocks = []
    q0 = np.ones((n,1))/math.sqrt(n)
    blocks.append(q0)
    for p in range(1, N+1):
        cols=[]
        block_len = 2**(N-p+1)
        half = block_len//2
        for j in range(2**(p-1)):
            v=np.zeros(n)
            start=j*block_len
            v[start:start+half]=1.0/math.sqrt(block_len)
            v[start+half:start+block_len]=-1.0/math.sqrt(block_len)
            cols.append(v)
        blocks.append(np.column_stack(cols))
    return blocks

def sparse_basis_2d(N: int):
    W=haar_blocks(N)
    cols=[]
    for p in range(N+1):
        for q in range(N+1-p):
            K=np.kron(W[p],W[q])
            cols.append(K)
    Q=np.column_stack(cols)
    assert np.linalg.norm(Q.T@Q-np.eye(Q.shape[1]),2)<1e-12
    return Q

def backward_difference(n: int):
    D=np.eye(n)
    for j in range(n):
        D[j,(j-1)%n]-=1.0
    return D

N=3
n=2**N
Q=sparse_basis_2d(N)
D=backward_difference(n)
Ax=np.kron(D,np.eye(n))
Ay=np.kron(np.eye(n),D)
c1,c2=1.0,0.6
B=Q.T@(c1*Ax+c2*Ay)@Q
H=np.eye(B.shape[0])-B/max(c1,c2)
assert np.linalg.norm(H,2) <= 1+2e-12
for m in [mu_star, mu_star+1e-3]:
    Z=m*(H-np.eye(H.shape[0]))
    Aamp=np.eye(H.shape[0])+Z+Z@Z/2+Z@Z@Z/6
    op=np.linalg.norm(Aamp,2)
    if m <= mu_star+1e-14:
        assert op <= 1+2e-10
    else:
        assert op > 1

print(f"mu_star = {mu_star:.15f}")
print(f"negative_real_endpoint = {2*mu_star:.15f}")
print(f"improvement_over_SSP_coefficient_1 = {(mu_star-1)*100:.9f}%")
print("symbolic_bernstein_identity = verified")
print("finite_sparse_grid_matrix_check = verified")
