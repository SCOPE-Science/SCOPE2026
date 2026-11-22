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

# Reproducible checks

Run `python3 verify.py` using only the standard Python library. The code independently enumerates all partial permutations and all ordered vertex pairs at orders \(1\)–\(4\), then verifies the full exact squared-distance polynomial, every conditional falling-factorial shared-cell moment and the exact mean formula. At orders \(10\), \(20\), and \(40\), an exact rational coefficient recurrence verifies integrality, nonnegativity and total-count normalization. A successful run emits `PARTIAL_PERMUTATION_METRIC_EXACT_PASS`.

# Logical boundaries

The finite checks are not an infinite proof. The full theorem follows from conditional factorial moments and a published Laguerre Perron asymptotic valid locally uniformly near the relevant positive argument, combined with the dominated conditional probability generating function and the delta method. The one-variable Gaussian deficiency input is classical. No external or independent audit was performed.
