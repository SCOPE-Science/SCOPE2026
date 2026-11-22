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

# Reproduction

Run `python3 verify_heawood_quotient.py` with Python 3.10+ and the standard library. The verifier requires no additional downloaded data, certificate file or package dependencies.

Expected exact outputs:

- Matching face counts: `(21, 168, 644, 1218, 1050, 336, 24)`.
- Orbit flag cells: `(29, 311, 1400, 3051, 3375, 1800, 360)`.
- Integer unit-pivot counts: `(28, 283, 1117, 1934, 1440, 360)`.
- Original one-skeleton triangular presentation: 148 generators eliminated in waves `(96, 38, 14)`.
- Edge-fixing symmetry generators close to all 336 automorphisms.
- Terminal success text: `HEAWOOD_MATCHING_FULL_AUT_QUOTIENT_S4_OK`.

The code checks the complete integral boundary-square identities before cancellations and after each elimination stage. The final result is a two-generator reduced chain complex in degrees zero and four, with all differentials zero. These are finite exact assertions, not floating-point ranks. Armstrong's orbit-space fundamental-group theorem and Hurewicz–Whitehead are used as explicitly stated in the proof; the script does not attempt to certify general infinite homotopy-theoretic theorems.

No independent external mathematical audit is represented by this file.
