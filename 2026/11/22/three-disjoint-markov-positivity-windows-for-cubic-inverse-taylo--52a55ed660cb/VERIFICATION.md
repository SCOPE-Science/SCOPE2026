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

Execute `python check.py` using Python 3.10+ with `sympy>=1.12`. Exact rational operations reproduce the displayed coefficient formulas, each polynomial sign certificate, the Sturm sign-variation pairs, rational isolating brackets, and independent exact inverses of six sample step matrices for the seven-state chain. The script prints `VERIFICATION_OK` on success and stops on any failed assertion.

The finite rational matrix examples verify the implementation and identities only; the all-steps classification follows from the exact generating-function identity, positivity of nine numerator polynomials, absence of positive roots of \(U\), and exact Sturm root counts and bracket signs for \(P\) and \(V\). At step zero the update is the identity. Neither arbitrary Markov generators nor floating-point behavior are assessed.
