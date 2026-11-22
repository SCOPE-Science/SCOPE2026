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

# Mathematical verification record

For the theorem in `RESULT.md`, exact covariance integration gives \(\operatorname{Var}(J_d)=3^{-d}\), \(\operatorname{Cov}(J_d,A_{j,x})=3^{-(d-1)}c(x)\), and for distinct axes \(\operatorname{Cov}(A_{j,x},A_{k,y})=3^{-(d-2)}c(x)c(y)\). Subtracting the common scalar projection produces independent Gaussian residuals. Conditional Gaussian precision additivity, a one-crossing derivative in each slice coordinate, and strict Jensen concavity give the **global**, not merely stationary, design theorem. The signed-polynomial proof of strict concavity is printed in `RESULT.md`.

## Reproducible checks

Run `python3 verify.py` with Python 3 and only its standard library. In the current science package it passed 125 exact rational full-covariance/posterior-precision comparisons, exact cross-orientation residual-covariance cancellation, 99 positive-root and optimum-risk formula checks, 4,950 supplementary random alternative designs, and noiseless limits in dimensions two through seven. These checks were conducted against the packaged `verify.py` contents and not an unrelated computation file.

## Scope and limits

Exact arithmetic validates only tested finite instances; randomized comparisons do not certify universal optimality, and no assertion of independent validation is made. The all-dimensional theorem follows from the written analytical proof; it assumes the specified Brownian-sheet tensor kernel, one complete slice per axis, independent Gaussian errors and a sum-of-precisions budget. The original article comparisons address publication priority only as far as inspected materials establish; no external independent assessment has been performed.
