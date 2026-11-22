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

The exact finite-system proof is in `RESULT.md`, and the standalone no-dependency checker is `verify_frucht.py`. It enumerates every one of the 4096 vertex subsets and every one of the 531441 spin assignments for the explicit 18-edge graph. The checks include the independence polynomial, the population-resolved monochromatic-edge minima and their counts, the deterministic sitewise favoured-color support on both sides of the first field transition, and ground-sector tests at rational witness fields. The verifier prints `EXACT_FRUCHT_POTTS_CERTIFICATE_OK 531441 configurations 4096 subsets` when every assertion passes. Uncountably many real field values are covered by the symbolic inequalities and strict comparisons in the proof, not by the finite witness fields.

No independent audit of these mathematical claims has been performed. The historical-priority assessment remains provisional.
