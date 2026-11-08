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

# Reproducibility

Run `python3 check_alternating.py` using Python 3 and its standard library. The checker computes alternating-form rank distributions for \(q\in\{2,3,4,5\}\) across multiple small dimensions; for selected small cases it enumerates the vector-pair update distribution, evaluates every additive character, and compares exact rational chi-square divergences for times one, two and three. On success it prints `ALTERNATING_WEDGE_WALK_SPECTRAL_CHI2_CHECKS_PASS`.

The checker is a finite diagnostic only. The proof establishes the character identity, multiplicity count, dominated-convergence profiles, and uniform-radical bound for all prime-power fields and unbounded dimensions. No external independent audit, publication-priority certification, or fixed-offset total-variation limit has been performed.
