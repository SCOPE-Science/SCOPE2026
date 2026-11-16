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

Run `python3 CHECK.py` with Python 3.8 or later. The checker uses only the Python standard library. It checks direct graph enumeration versus signed transfer traces at all sign patterns for \(3\le n\le10\), runs complete integer Walsh--Hadamard transforms through \(n=16\), verifies five zero seeds and the sharp positive seeds, and verifies the characteristic-two seven-step and modulo-four fourteen-step transfer identities. It enumerates all 128 seven-sign blocks, identifying fourteen whose transfer matrices square to the identity and confirming all corresponding fourteen-sign extensions. It also checks the modulo-four count and vertex-marginal obstruction in lengths 6, 13, 20, 27, 34, and 41.

A passing run prints `CYCLE_SQUARE_FOURIER_EXACT_PASS`. Integer checks at finite lengths are not a proof of an unrestricted classification. The all-length proof depends on the explicit identities, recurrence, and witnesses given in `RESULT.md`; the standalone checker audits their finite prerequisites. The zero-frequency count is a lower bound, not a complete nullity census. Independent mathematical audit has not been performed.
