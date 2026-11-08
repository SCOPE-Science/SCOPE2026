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

The proof uses weighted matrix-tree determinants, the elementary Poisson kernel, Cauchy--Schwarz, nonnegative relative entropy, and a sharp scalar-root limit. No infinite statement rests on finite checking.

Execute `python3 verify.py` from this package. The included standalone standard-library code independently enumerates all \(m\)-edge subsets of a \(2m\)-edge wheel and checks spanning-tree connectivity, spoke counts, individual edge marginal symmetry and Kirchhoff cofactor polynomials for \(3\le m\le8\). It additionally checks the analytic root equation, monotonicity and limits numerically for a bounded range. Exact integer determinant and enumeration comparisons are separate from numerical tolerance checks. Replay on the final extracted file yielded `VERIFY_OK 1626 exact and numerical assertions`.

Exact computational coverage ends at \(m=8\); numerics do not certify the stated asymptotic constant. The symbolic proof supplies all-order guarantees, and independent review has not been performed.
