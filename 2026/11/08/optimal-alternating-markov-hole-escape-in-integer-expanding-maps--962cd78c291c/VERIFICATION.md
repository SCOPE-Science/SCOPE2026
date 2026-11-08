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

# Reproducibility and verification

The complete proof is in `RESULT.md`; `checker.py` supplies finite checks independent of the proof's induction step. Run `python checker.py` using Python 3.9 or newer, with no third-party dependencies. The checker enumerates all digit words for bases two through four at short lengths, all binary hole schedules up to length eleven for bases two through eight, and tests the count recurrence, strict fixed-hole comparison, and characteristic-root behavior. It reported:

`PASS: 2174 finite exact/computational assertions; no infinite claims inferred.`

Infinite-horizon convergence follows from the displayed characteristic equation, not from numerical fitting. Uniqueness over arbitrarily long schedules follows from strict order preservation of finite count-matrix products, not from the enumerated horizons. No independent mathematical audit has been performed.
