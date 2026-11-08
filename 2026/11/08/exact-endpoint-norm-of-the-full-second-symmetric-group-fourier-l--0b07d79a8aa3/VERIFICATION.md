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

# Reproducible checks and limitations

Run `python3 verify.py` from the extracted standalone package. Python 3 standard library is sufficient; no data files or external services are required. The checker enumerates every permutation of order four through nine and computes both cycle characters, the central weighted sum, its strict sign locus, the direct exact endpoint norm and the independent derangement expression. It additionally checks inclusion-exclusion for derangement numbers through size sixty and compares normalized values with the proved constant.

The expected terminal marker is `VERIFY_OK exact_all_permutations_n4_to9 full_second_level_n4_to60`.

The finite checks do not prove an infinite-family assertion. That relies on the exact character decomposition, the sign-case inequalities, fixed-point/marked-transposition counting, and elementary alternating-series bounds established in `RESULT.md`. They do not determine historical priority or independently validate the theorem.
