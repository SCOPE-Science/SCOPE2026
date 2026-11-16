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

The analytical result follows from the three-sector decomposition of trace-zero \((1,1)\) projective harmonics, conditional Haar moments, and exact Beta-integral identities. A finite checker is included solely as corroboration.

Run `python3 check_projective_cap.py`. The checker uses Python 3 standard-library rational arithmetic and no external dependencies. It constructs all coordinate trace-zero Gram matrices from conditional second moments of the Dirichlet distribution and confirms sector scalar action, cross-sector orthogonality, exact spectral differences, and multiplicity-weighted trace identities. The recorded output was:

`PROJECTIVE_CAP_EXACT_MOMENT_PASS dimensions=3..8 threshold_cases=42`

It tests dimensions \(3\) through \(8\) and seven rational cutoffs in each dimension. Finite checks do not establish the theorem for untested dimensions or real thresholds; those cases are addressed by the derivation in RESULT.md. No independent mathematical audit has been performed.
