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

Run `python check.py` from the directory containing that file (no third-party dependencies). Exact rational arithmetic checks normalization, identical first and second reset-amplitude moments, identical second multiplier moment, the fourth multiplier moments, fourth growth-exponent signs, and the finite B fourth moment. Additional finite numerical checks test the ordering at sample scales and integer orders and compare root limits. Actual program output from the packaged file is recorded separately at package creation.

The continuous-real-power inequality is proved via the third-divided-difference mean-value theorem in `RESULT.md`; the real-order moment iff follows from an infinite perpetuity with a strict necessity step. Finite checker loops cannot replace either argument. Independent audit has not been performed.
