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

# Reproduction and limitations

Run `python3 verify.py` with Python 3 and no third-party packages. The checker independently creates all prime-representative subgroups by closing prime generators, compares the complete set with the theorem for exponents 1 through 14 and exponent 17, checks subgroup sizes, and explicitly confirms the order-four examples at 32 and 512. It reports 33 subgroup instances in the tested range. This confirms finite computations, not the all-exponents theorem. The all-exponents argument is reconstructed in `RESULT.md`; no separate independent mathematical audit has been performed.
