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

# Reproduction and mathematical limits

The package includes `checker.py`. Running `python checker.py` from the extracted file directory completed 195 exact independent checks: 90 complete spin-configuration enumeration comparisons for \(5\le n\le14\), and 105 cyclic two-run coefficient comparisons computed directly from words against the proposed binomial formula. All checks passed. No randomized inputs or external dependencies are used.

The analytical proof in `RESULT.md` checks the flip-energy signs for the hub and each rim site, treats all marginal field equalities separately, and derives the entropy values from transfer-matrix eigenvalues. Exhaustive finite tests are supporting evidence only and are not an infinite certificate. Neutral-energy flips at equality fields may remain dynamically allowed under zero-temperature Glauber rules; weak local minima are the sole object being counted.
