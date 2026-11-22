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

The complete proof is in `RESULT.md` and the standalone checker is `check.py`.

Replay with `python3 check.py --max-n 18` in a directory containing that file. The checker uses only the Python standard library and constructs the legal-flip graph directly, not from the particle-transfer representation. It validates every component's equal-edge count, size, and number of induced flip edges, as well as the complete list of components for each length from 3 through 18. A separate independent-set enumeration validates the numerical gap count through length 13.

These are finite consistency tests; the theorem for arbitrary length follows from the difference representation, token-slide connectivity, an explicit closed slide walk that lifts to complementation, and elementary counting. The verification does not decide prior-art priority, independent audit, diameters, or Hamiltonicity.
