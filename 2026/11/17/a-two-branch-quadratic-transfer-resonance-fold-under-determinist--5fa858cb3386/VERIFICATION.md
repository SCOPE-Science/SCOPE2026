---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Direct inverse-branch PF computation on mean-zero u=x-1/2, v=x^2-x+1/6 yields a triangular 2x2 matrix for P_bP_a with diagonal g(a)g(b), h(a)h(b), and off-diagonal C=-a(1-a)g(b)-h(a)b(1-b)<0. At λ1=λ2 the Jordan power is exact, and orthogonal u,v moments 1/12,1/180 give Cov(X^2,F^n(X)^2)=(4/45)λ^n+(C/12)nλ^(n-1). R=g/h increases then decreases on b∈(2/3,1), maximum 2/sqrt(3) at b*, proving 0/1/2 resonance roots at a*. Symbolic substitution independently recovers b±=207/254±sqrt(9213)/762 for a=13/20 and sign-thresholds ≈0.7853 and ≈1.29286; high-degree polynomial diagonal moduli are bounded strictly by h(a)h(b)=λ. No global BV spectral-isolation claim is made.

## originality

PASS

Existing random skew-tent Jordan resonance concerns annealed convex combinations; this is the deterministic ordered product with a different algebraic fold and exact two-return covariance. General transfer-operator Jordan existence and polynomial-time decay are prior knowledge; the sharp deterministic parameter classification and two distinct negative-lag thresholds survive the implication comparison on a best-of-knowledge basis.

## value

PASS

Deterministic periodic forcing of a natural full-branch expanding interval map creates a defective leading polynomial mode despite two nonresonant seasons. The exact onset fold, two branches and opposing first-negative-return lags are measurable rigidity/relaxation distinctions beyond the routine Jordan-block identity. The mathematical object and covariance are motivated independently of a one-off rational parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
