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

The standalone `prism_verifier.py` uses exact integer recursive pairing of vertices to enumerate all perfect matchings on prism graphs with 3–7 columns. For every one of those lengths, an exact Walsh–Hadamard transform computes all Boolean-frequency multipliers and verifies the zero-frequency existence criterion, the least positive absolute multiplier, and the maximum. All multiplier formulas are checked at each frequency for 3–5 columns and at 2000 deterministic/pseudorandom frequencies for 6–7 columns. Exact transfer-matrix trace identities and explicit zero witnesses are checked for lengths 3–300. Run with `python prism_verifier.py` and NumPy installed; no other files are needed.

The derivation for all lengths is in `RESULT.md`. Finite checks do not establish the infinite theorem, nor do they independently audit novelty. The mathematical limitations and remaining source-comparison risks are stated in `RESULT.md` and `REVIEW.md`.
