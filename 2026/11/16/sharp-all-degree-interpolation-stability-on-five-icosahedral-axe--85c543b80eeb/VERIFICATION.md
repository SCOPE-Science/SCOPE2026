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

Reproduce with `python verify.py` (requires Python, NumPy and SciPy). The checker uses exact fractions for all 19 finite degrees through 18, including the exceptional ranks and sharp equality cases. A separate implementation uses complex spherical harmonics from SciPy to build the five-point normalized sampling matrix and compares its Gram eigenvalues with the exact Legendre formulas at degrees zero through twelve. Its strict high-degree certificate is based on the published Legendre Bernstein inequality; the code verifies its rational endpoint inequalities but does not purport to prove the published lemma independently.

Only the quoted result for the five-point grid and the explicitly stated all-degree theorem is reviewed here. No independent audit has been performed.
