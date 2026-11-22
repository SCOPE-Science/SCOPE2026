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

# Exact reproducibility

From the directory containing this file and `verify.py`, execute `python3 verify.py` in Python 3. The program requires only the standard library and prints `VERIFY_OK exact_resolvent_vector_identities=16 all_dyadic_blocks=17 index_comparisons=131071` when all checks succeed.

The checker generates the eight-state matrix directly from the bit carry rule; it verifies all eight coordinates of both exact polynomial-vector identities that algebraically imply the infinite generating-function identity. It separately enumerates the valuation-zero and valuation-one coefficients using Legendre's digit-sum formula for each dyadic interval through length \(16\). These are exact finite arithmetic checks; their interpretation as an unrestricted theorem depends on the proof of the Kummer transition model and the formal inverse argument recorded in `RESULT.md`. No external mathematical audit was performed.
