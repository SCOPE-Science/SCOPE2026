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

# Reproducibility and limits

Execute `python verify_antiphase.py` with `mpmath` installed. The script finds the unique threshold root by high-precision transcendental equations, reconstructs the equal-amplitude and two exchanged unequal-amplitude cycles, and directly checks two successive original-map updates for \((L,c)=(3,0.15)\) and \((4,0.2)\) at 65 digits. The checker verifies finite examples, not the universal three-cycle theorem. That conclusion follows from the exact logarithmic reduction, monotone threshold equation and intermediate-value sign argument in RESULT.md.

The source literature contains qualitative antiphase multistability. Absolute historical priority is not certified. There is no independent proof verification or expert validation.
