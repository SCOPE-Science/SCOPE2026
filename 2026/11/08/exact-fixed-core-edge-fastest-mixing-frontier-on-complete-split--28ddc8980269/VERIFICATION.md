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

The derivation is analytic: permutation averaging is justified by convexity of the centered symmetric spectral norm; the invariant matrix has three nontrivial eigenvalue classes; interval feasibility translates into seven explicit lower bounds for the optimum. These steps cover all integers \(s,m\ge2\) and all real \(0\le t\le1/(s-1)\).

The supplied `verify.py` uses only the Python standard library and exact rational arithmetic. It independently minimizes a piecewise-affine spectral envelope at every endpoint and every pairwise breakpoint, checking the theorem against 3332 exact test instances. It constructs 180 full matrices and checks all rows, nonnegative entries and the three predicted eigenvector classes. It checks the explicit four-regime witness at 3001 exact rational points. Replay: `python verify.py`.

No finite sample, no matter how large, establishes the all-parameter result; the written proof supplies the universal quantifiers. No claim of independent audit or formal certification is made.
