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

The standalone `verify.py` exhaustively enumerated all binary inputs and nonempty erased-edge masks for lengths 3 through 10. It checked all inverse-list counts, both sharp mask-placement capacity bounds, the all-mask generating polynomial, and the cyclic nonadjacent-erasure criterion. Recorded result: `VERIFY_OK n=3..10 all_masks=2032 direct_source_instances=1396040 adjacent_erasures=1725 algebraic_sums_extrema_and_birthday_counts=all`.

For the infinite-domain claims, the mathematical proof uses binary path reconstruction, disjoint-component factorization, strict discrete log concavity, marked cyclic compositions, and an elementary logarithmic product limit. Numerical checks cannot validate infinite quantifiers or priority. This artifact contains no independent assessment.
