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

# Verification notes

The proof rests on the exact identity \(B=DM^{-1}D^{\mathsf T}\), positivity of the inverse of \(I+BA\) for every nonnegative diagonal \(A\), its weighted-column inequality under \(w^{\mathsf T}B\ge0\), the convex divided-difference optimality identity, and an explicit one-edge quadratic necessity witness. The nonlinear-flow statement follows from the same cooperative edge matrices and implicit-Euler approximation. The finite-dimensional limit for nonsmooth finite convex potentials is via smooth convex approximations/strongly convex minimizers.

Run the standalone Python 3 standard-library script `python check.py`. Its exact Fraction arithmetic checks:

- 126 random positive rational mass arrays and \(w=B^{-1}\mathbf1\) weight vectors, confirming exact positivity of edge resolvents and all column inequalities.
- 504 random exact rational pairs of quartic convex energy minimizers, with data reconstructed from first-order optimality, confirming the genuine nonlinear two-input bound.
- The exact four-site unstable-weight quadratic witness, yielding output variation \(5/6\) from input variation \(1/2\).

Finite tests serve as normalization and implementation cross-checks. They do not constitute a proof for infinitely many dimensions, arbitrary convex functions, or nonlinear-flow limits. Historical priority and the validity of sources have not been independently certified.
