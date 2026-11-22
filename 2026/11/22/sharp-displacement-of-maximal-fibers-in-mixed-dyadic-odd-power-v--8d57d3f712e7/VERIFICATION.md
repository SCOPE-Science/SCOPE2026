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

The theorem has an all-depth mathematical proof in `RESULT.md`; the checker is finite corroboration. Run `python3 verify_mixed_power_values.py` using Python's standard library. It independently builds both odd-power value sets by modular exponentiation, counts every ordered cross-sum, compares every fiber to the valuation-shell formula, and checks the sharp maximum, its valuation-\(d\) attaining witness, the count of all ordered pairs, and the strict odd-target minimum. Tested pairs are \((3,5),(3,7),(3,9),(3,11),(5,7),(5,9),(7,9)\); tested depths are \(0\) through \(10\), with 14,637 exact assertions. The expected marker is `MIXED_CHECK_OK 14637`. Neither finite testing nor self-review is an independent mathematical audit. The energy formula is a direct identity from the valuation partition and does not rely on numerical extrapolation.
