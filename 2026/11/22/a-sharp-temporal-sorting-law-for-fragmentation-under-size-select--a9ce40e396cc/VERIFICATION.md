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

# Verification record

The complete proof is in `RESULT.md`; the accompanying reproducibility file is `verify.py`. Run `python verify.py` with Python 3 and no additional packages. The checker tests exact coefficients of the full adjacent-swap commutator for classes 2 through 7, nonnegative mass ordering across every distinct permutation of four-interval schedules at sampled rational parameters, and explicit strict examples for both monotonicity directions. The observed output is `PASS: 28153 exact-rational coefficient and permutation assertions`.

The decisive infinite-dimensional-parameter statement is established symbolically: \(T(p)T(q)-T(q)T(p)\) has only subdiagonal coefficients \((p-q)s_{j+1}(s_j-s_{j+1})\). Nonnegative transition products propagate that componentwise sign through every adjacent swap; a two-interval point-mass input proves necessity. The numerical checker is not an exhaustive proof of the real-valued parameter domain. No field measurements, independent external validation, or priority certificate are provided.
