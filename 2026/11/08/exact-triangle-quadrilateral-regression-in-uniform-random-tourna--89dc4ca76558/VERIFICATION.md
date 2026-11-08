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

`verify.py` exhaustively iterates the independent edge orientations for all tournaments on 4, 5 and 6 labeled vertices, then computes strong connectivity by explicit directed reachability. It uses exact Python integer and `fractions.Fraction` arithmetic rather than floating-point sampling. The checks compare both means, both variances, cross-covariance, the linear residual variance and the squared correlation against the displayed formulas.

Reproduce with `python verify.py`. The test output must contain `All rational complete-enumeration checks passed`. All 3 tested graph orders passed when run against this package. Only graph orders at most 6 are exhaustively enumerated. The proof in `RESULT.md`, not the finite checks, covers every integer graph order at least 4.

The key nonstandard local calculation has a direct eight-orientation argument: given a cyclic triple, six of eight orientations of a fourth vertex yield a strong tournament; given a transitive triple, two of eight yield a strong tournament. Every other needed nonzero covariance is obtained by conditioning on the shared vertices.

Independent audit has not been performed.
