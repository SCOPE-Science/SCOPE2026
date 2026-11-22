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

The proof uses the BV measure decomposition, the two-binomial exact identity and a triangular-array central limit theorem. The standalone script `verify_genuine_bd.py` checks the low-degree polynomial identities, the exact center formula and boundary values through degree 14, independently integrates 112 step responses and compares them to the two-binomial expectation, and checks convergence of central values. The script does not attempt to certify every finite maximizer or prove infinite-degree claims numerically.

Run `python3 verify_genuine_bd.py` with SymPy and SciPy. The original subscription-only papers were not inspected in full; no independent audit has been performed.
