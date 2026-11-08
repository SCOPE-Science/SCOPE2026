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
# Verification and limits

For the precisely defined family \(P_d=\operatorname{conv}(\operatorname{Av}_d(132,213))\), the following mathematical steps were reconstructed: (i) complete facet systems and projected Euclidean normal norms; (ii) the exact nonnegative Dirichlet path Green kernel; (iii) the sharp inball bound from its first row; (iv) construction of equality with all facet distances; (v) uniqueness from strictly positive first row; and (vi) the antipodal-pair outer-sphere lower bound with strict convexity ruling out nonvertex contacts.

## Reproducible checks

Run `python3 verification/verify_avoiding_inball.py`. It prints exactly:

```
PASS: exact vertex/facet signatures 8194
PASS: high-precision inball/facet/Laplacian checks 14850
PASS: total checks 23044
```

These tests cover all reverse-layered vertices through \(d=10\) and 99 consecutive dimensions from \(d=2\) through \(d=100\), including end ranks and strict interior ranks. The proof applies to all integers \(d\ge2\). A separate SciPy HiGHS linear-programming check of the primal inball optimization agreed for all \(2\le d\le32\); the standalone program itself has no nonstandard dependencies.

## What is not established by finite tests

Enumeration through \(d=10\) is not a classification proof for arbitrary \(d\); the cited full facet theorem and the derived Green-matrix argument supply the infinite-dimensional reasoning. High-precision checks cannot certify strict inequalities at all dimensions; the symbolic inequality \(k(d-k)\ge d-1\), with equality only at the endpoints, does. The record is reviewed by the same model only; independent audit has not been performed. Historical originality is provisional.
