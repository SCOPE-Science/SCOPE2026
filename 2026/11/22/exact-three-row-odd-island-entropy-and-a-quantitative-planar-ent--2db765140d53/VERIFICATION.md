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

The standalone `checker.py` builds the states and matrix directly from the parity-frontier definition; it does not rely on a stored matrix or historical artifact. Executing `python checker.py` reports exact integer characteristic-polynomial agreement, a certified real-root bracket, matrix primitivity by explicit empty-state returns, an independent exhaustive finite-board census up to five columns, and the strict two-row entropy-bound comparison. Arbitrarily long strip configurations are covered by the mathematical frontier invariant and four-column completion proof, not by finite enumeration. No independent audit or external validation has been carried out.
