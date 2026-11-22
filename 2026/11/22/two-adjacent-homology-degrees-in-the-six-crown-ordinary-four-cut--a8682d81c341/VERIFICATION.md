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

Run `python3 verify.py` with Python 3.9+; no third-party package is required. The program enumerates all 495 four-sets, applies induced-connectivity testing to construct 165 forbidden sets, builds every nonempty simplex in the Alexander dual, and performs the deterministic matching described in `RESULT.md`. It checks all 2,832 directed Hasse incidences for cycles, then recursively computes signed integral gradient-path coefficients from the unique critical four-cell into 66 critical three-cells. The result is identically zero, not merely zero modulo a prime. Independently it computes all simplicial mod-two boundary ranks, finding 11, 55, 165, 99, 20.

The recorded execution output is `verification_output.txt`. This finite certificate supports the stated dual homotopy decomposition via Forman theory and the Hurewicz map. It has not been independently externally audited, and finite verification does not establish an analogous theorem for all crown sizes.
