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

The analytical proof is in RESULT.md. The independently evaluated *finite* checks use Python 3 and mpmath, with no network resources. Run `python verify_rocking_resonance.py` beside these files.

The checker validates six small-critical-parameter scaling cases, four phase-closure roots for winding numbers 3, 5, 8, and 12 at relative energy 1/2, two fixed-parameter near-saddle values yielding a logarithmic finite-difference slope, and five exact nearly circular frequency identities.

The exact singular limits and the existence statements for every sufficiently large integer winding follow from the quadrature proof, not from finite numerical tests. No independent audit or machine-checked formal proof is asserted. The period and phase use the original dimensionless time and the actual positive complex radius; the physical impacting-block limit is not tested.
