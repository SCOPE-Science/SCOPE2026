---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof establishes exact diagonalization and graph reconstruction for every finite simple graph with no isolated vertices and every \(0<p,q,\omega<1\). Its central identities are the universal eigenvalue equation, the pair gap \(\omega(1-r)^2/N>0\) and the triangle/claw gap \(\omega(1-r)^3/N>0\).

To reproduce the explicit seven-vertex witness, run `python check.py` using Python 3's standard library. The checker constructs two 64-by-64 transition matrices in exact fractions, verifies every row sum and the independent Bernoulli invariant law, tests all 63 nonempty subset eigenrelations on each graph (126 eigenfunction checks over all 64 states), compares every subset of one or two observed edge IDs, and confirms the exact triple gap \(9/224\). The verified output is:

```
PASS: exact 64-state matrices, invariant laws, all 63 eigenrelations on each graph
PASS: all order-one and order-two stationary-lag signatures match
PASS: third-order claw/triangle separation is 9/224
Parameters p=1/2 q=1/4 omega=2/3 N=7; no isolated vertices.
```

Finite exact computations certify the named witness only; infinite graph-family and parameter quantifiers rely on the symbolic derivation in RESULT.md and the classical line-graph theorem. The classification is an exact stationary-law identifiability result, not a finite-sample statistical procedure. No independent audit has been performed.
