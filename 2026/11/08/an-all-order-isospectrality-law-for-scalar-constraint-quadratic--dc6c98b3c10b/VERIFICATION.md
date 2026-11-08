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

The standalone `verify.py` uses only Python's standard library and rational arithmetic. Execute `python3 verify.py` from this directory. Its recorded standard output appears in `verification_output.txt`. The verifier directly constructs the sequential ADMM sweep and computes characteristic coefficients by an independent Faddeev–LeVerrier recurrence.

Verified: 200 exact-arithmetic assertions; fixed-order permutation counts \(2,6,24,120,4,4\) for block counts \(2,3,4,5,6,7\), respectively; three-block Schur factorizations over sampled rational triples; and two explicitly different finite-time error vectors and squared norms for an identical spectrum.

The exhaustive statement is only about the finite sets of permutations checked. The all-dimensional identity and all-parameter Schur conclusion depend on the analytic determinant and inequalities, not on computer enumeration. Independent scientific audit was not performed. Specialist publication precedence remains subject to later review.
