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

# Verification performed

Direct exhaustive verification of the original matrix-unit anti-automorphism and involution equations is provided by `check.py`. The script uses exact prime-field arithmetic, constructs every upper-triangular unit for the listed cases, identifies scalar multiples, and checks all pairs of basis matrix units. `CHECKS.txt` is the output from the actual execution, including seven PASS cases. The proof of the scheme coordinate ring, its nilpotent support, tangent excess and nonliftable dual-number direction is given algebraically in `RESULT.md`. No finite enumeration purports to establish the assertions for arbitrary dimension or arbitrary base field. Independent auditing has not been performed.
