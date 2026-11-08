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

# Reproducibility and scope

Run `python3 verify.py` with Python 3, without external dependencies. Its tests use exact integer arithmetic and a fixed deterministic seed. It compares direct finite enumeration with the closed norm formula and checks all optimal height patterns. Full enumeration is performed for every labeled qualifying four- and five-vertex graph. Samples for six and seven vertices are not exhaustive. The square-completion and complement biclique arguments in `RESULT.md` establish the theorem in every admissible dimension, independently of finite evidence. There is no independent mathematical audit.

Expected success markers include `EXHAUSTIVE_ALL_LABELED_COMPLEMENTS_OK`, `SEEDED_VALID_C4_FREE_DIAMETER_TWO_OK`, `COMPLEMENT_CYCLE_THRESHOLD_OK`, `EXACT_QUADRATIC_ENVELOPE_OK`, and `ALL_C4_FREE_SPREAD_CHECKS_OK`.
