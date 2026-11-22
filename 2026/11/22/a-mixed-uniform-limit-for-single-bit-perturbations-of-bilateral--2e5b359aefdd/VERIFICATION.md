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

# Reproduction and checks

Run `python3 verify_flashback_sensitivity.py` beside `verification_output.txt`; use Python 3 with only the standard library. The source constructs the transform by two implementations: explicit repeated stripping of maximal end runs and direct pairing of run-length encoded runs, including terminal split normalization. All binary source words of lengths 1–14 (32,766 words), and all 360,456 ordered interior one-bit edits, were checked. In the unchanged-run-count case, at most two depth-aligned content tokens differ. In both regimes the two token constructors agree. Exact finite sums verify token counts and report the finite empirical expectations.

The captured output records fixed-seed simulations at lengths 256, 1024, 4096, each with 3000 random words and interior positions. The analytic target is an asymptotic mean of 1/24, a skeleton-changing probability of 1/2, and a conditional median of 1/12. The finite checks and simulations are corroborating evidence only. The proof of the all-length distribution appears in RESULT.md, using run-index shift structure, strong laws for two-dependent geometric run-length comparisons and uniform edit location. No external independent audit has been performed.
