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

The delivered `CHECK.py` uses only Python's standard library and represents prime-power fields by polynomial residues. It counts additive-quadruple collisions directly from the distinct union of the two quadratic graphs, not by the claimed closed formula. All 240 admissible curvature ratios across the prime fields \(3,5,7,11,13,17,19,23,29,31\) and the extension fields \(9,25,27,49\) passed the exact-integer equality check; the final console line was `DIRECT_ENERGY_CHECK_OK 240`. Separate checks evaluate the full quadratic-character sign-pair counts and compare actual extrema against the stated sharp large-field formulas.

To reproduce: run `python3 CHECK.py` in the directory containing this document and the checker. No downloads, generated secrets or ancillary data are required.

The checker does not exhaust all finite fields and does not prove the infinite family. The all-field theorem is proved by character-convolution orthogonality; Hasse's standard elliptic curve point-count bound is the only non-elementary input used to certify extremal sign configurations in all sufficiently large fields. No independent verification or audit has been performed.
