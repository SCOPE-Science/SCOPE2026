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

Reproduce with `python3 check_cardinal_bv.py` (standard library). Its high-precision algebraic assertions check \(q^2-4q+1=0\), the critical point \(t_*\), the peak value \(H\), and the radical expression for the sharp coefficient. The explicit bilateral Green recurrence is checked at translated jumps; cubic-cell variation uses derivative roots rather than a sampling grid; deterministic random finite superpositions check compatibility with the claimed upper bound. Expected terminal marker: `ALL_CARDINAL_SPLINE_BV_CHECKS_PASS`.

The all-integer support and infinite-tail equality are proved symbolically by the geometric series in RESULT.md, not inferred from the finite numerical range. The universal bound uses an absolutely summable jump decomposition. No independent mathematical audit is claimed.
