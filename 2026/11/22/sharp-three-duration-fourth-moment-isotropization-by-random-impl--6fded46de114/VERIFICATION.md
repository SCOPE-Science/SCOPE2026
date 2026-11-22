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

# Verification scope

The proof uses two nonnegative-polynomial certificates: the rational mean-duration identity and the degree-two circular-cap inequality. Reproducing the symbolic checks requires `python verify.py` after installing `requirements.txt`.

The script tests exact midpoint orthogonality, exact rational factorization, three-point moment cancellation, sharp duration normalization, and strictly positive phase rotations. An optional finite linear program discretizes the possible phases as a diagnostic only. The theorem's statements for all probability laws, support lower bound, and boundary uniqueness are justified analytically in `RESULT.md`; finite computations do not certify infinite-dimensional optimality.

The checked source comparison was performed against the original random-time-step paper and the full theorem of the closest published second-moment result. Historical priority remains a qualified self-review. No independent audit has been conducted.
