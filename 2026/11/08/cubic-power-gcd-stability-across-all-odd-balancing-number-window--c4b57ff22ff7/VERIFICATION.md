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

# Verification

The standalone reproducibility script `check_cubic_balancing.py` uses only Python's standard library. Its supplied output `checks.json` checks the exact cubic window identity for 70 lengths and 13 initial positions per length, the analytic coefficient recurrence, 70 two-value gcd instances, and a contrasting seventh-power length-three gcd. The checker can be run with `python3 check_cubic_balancing.py`.

These are finite calculations, not an infinite proof. The universal claim is proved in `RESULT.md` via the cubic Binet identity, modular-seven residue cycles, the exact primitive gcd at balancing values one and six, and invertibility of the recurrence modulo any integer. This verification makes no claim of independent audit or external certification.
