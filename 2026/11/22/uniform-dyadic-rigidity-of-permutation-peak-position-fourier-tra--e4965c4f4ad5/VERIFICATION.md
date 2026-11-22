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

# Verification notes

Run `python3 peak_profile_verify.py` using only the Python standard library. The script checks the complete Fourier multiplier vector for every size \(3\le n\le15\) by two distinct methods: exact rational joint-peak probabilities computed from the alternating-block recurrence and exact integer descent-set Möbius inversion followed by a Walsh transform. For \(3\le n\le9\), brute-force permutation enumeration supplies a third independent calculation. It checks, for every character, integrality, equality, nonvanishing, the exact dyadic residue and singleton sharpness. The original all-order proof is in `RESULT.md`; no exhaustive computation proves a statement beyond its tested finite range.

No independent audit has been performed. The exact multiplier values outside the finite checked ranges and their odd parts are not tabulated.
