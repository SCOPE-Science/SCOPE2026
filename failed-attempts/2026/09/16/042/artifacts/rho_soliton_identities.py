"""Verify rho-soliton coefficient algebra (Lemma A of DRAFT.md) numerically/symbolically.

Identities (n=4): Ric + Hess f = (rho R + lambda) g
  trace:        dF := Delta f = (4 rho - 1) R + 4 lambda
  contracted:   Ric(grad f) = c grad R,  c = (1 - 6 rho)/2
  drift scalar: Delta_f R = (6 rho/(1-6 rho)) <grad f, grad R>
                         + 2 ((rho R + lambda) R - |Ric|^2)/(1-6 rho)
Checks:
  1. coefficient derivation c from (4 rho - 1) vs (rho - 1/2): c = (rho-1/2)-(4 rho-1) = (1-6 rho)/2.
  2. drift formula reduces to 2 lambda R - 2 |Ric|^2 at rho = 0.
  3. denominators vanish exactly at rho = 1/6 (c = 0) and trace degeneracy at rho = 1/4.
  4. numeric evaluation of the drift identity residual on random data satisfying
     the contracted relation by construction.
"""
import numpy as np

def c_of(rho):
    return (1 - 6*rho)/2

# 1. algebraic derivation check over a grid
rhos = [-1.0, -0.5, 0.0, 0.1, 0.2, 0.24, 0.26, 1/6 + 0.01, 0.5, 1.0]
for rho in rhos:
    c = c_of(rho)
    c2 = (rho - 0.5) - (4*rho - 1)  # (rho-1/2) - (4 rho - 1)
    assert abs(c - c2) < 1e-12, (rho, c, c2)
print("check 1 passed: c = (1-6 rho)/2 consistent")

# 2. rho = 0 reduction: drift = 2 lam R - 2 |Ric|^2 (no <df,dR> term since 6 rho = 0)
rng = np.random.default_rng(7)
for trial in range(200):
    A = rng.normal(size=(4,4)); Ric = (A + A.T)/2
    R = float(np.trace(Ric))
    lam = float(rng.normal())
    norm2 = float((Ric**2).sum())
    drift0 = 2*lam*R - 2*norm2
    rho = 0.0
    c = c_of(rho)
    gradf = rng.normal(size=4); gradR = rng.normal(size=4)
    # enforce contracted identity at rho=0: Ric.gradf = 0.5 gradR by projecting gradR
    gradR = 2*Ric.dot(gradf)
    drift = (6*rho/(1-6*rho))*gradf.dot(gradR) + 2*((rho*R+lam)*R - norm2)/(1-6*rho)
    assert abs(drift - drift0) < 1e-9
print("check 2 passed: rho=0 reduction matches Chen Delta_f R formula")

# 3. degeneracy locations
assert abs(c_of(1/6)) < 1e-15
assert abs((4*(1/4) - 1)) < 1e-15
print("check 3 passed: degeneracies at rho=1/6 (c=0) and rho=1/4 (Delta f coeff=0)")

# 4. drift identity residual with contracted relation enforced, general rho
for rho in [-0.75, -0.1, 0.0, 0.05, 0.13, 0.3, 0.8]:
    c = c_of(rho)
    for trial in range(300):
        A = rng.normal(size=(4,4)); Ric = (A + A.T)/2
        R = float(np.trace(Ric))
        lam = float(rng.normal())
        gradf = rng.normal(size=4)
        gradR = (2/(1-6*rho))*Ric.dot(gradf)  # enforce Ric(gradf) = c gradR
        norm2 = float((Ric**2).sum())
        # divergence-of-contraction derivation: c Delta R = 0.5 <dR,df> + (rho R+lam) R - |Ric|^2
        # pick random Delta R? Instead verify self-consistency: define DeltaR from that relation,
        # then check drift formula reproduces DeltaR - <dR,df>.
        dot = float(gradR.dot(gradf))
        DeltaR = (0.5*dot + (rho*R+lam)*R - norm2)/c
        drift = DeltaR - dot
        drift2 = (6*rho/(1-6*rho))*dot + 2*((rho*R+lam)*R - norm2)/(1-6*rho)
        assert abs(drift - drift2) < 1e-9, (rho, drift, drift2)
print("check 4 passed: drift-scalar identity holds given contracted identity")
print("ALL RHO-IDENTITY CHECKS PASSED")
