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

# Reproducibility

Execute `python3 verify.py` with the standard library. The program verifies all 98 canonical coefficients from independent exact-integer algorithms, 77 seven-color shifts through degree 27 (2,156 coefficient comparisons), the full two-sample table and unique eligible pairs, and the sharp one-sample counterexample. Output begins with `VERIFY_OK`.

The finite checks certify precisely the 49 canonical residue-pair exclusions, not the full infinite vanishing by themselves. The unrestricted conclusion uses (i) the proved characteristic-seven color-shift relation and its invertibility and (ii) the five infinite positive congruences previously established in Hirschhorn–Sellers Theorem 1.3. No independent mathematical review has been performed.
