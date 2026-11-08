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

# Reproduction and verification

Run `python3 verify.py` from the package root using only the Python standard library. An exact rational event-chain recurrence independently computes the final two-strain allocation distributions of 75 small trees, with positive heterogeneous side-branch transmission rates and three choices of common path-rate ratios. All distributions agree coefficient by coefficient with the weighted binomial theorem. A second calculation enumerates the 4,970 off-path weight compositions for \(1\le m\le7\), \(1\le B\le5\), checks the stated mean/variance and sharp bounds, and verifies all equality cases. A full symbolic proof for arbitrary \(m,B\) is provided in `RESULT.md`; the finite tests are not asserted to prove the infinite-parameter theorem. No claims of independent audit or empirical validation are made.
