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

# Reproducibility and limits

The bundled `verify.py` was executed from its package directory using Python 3 with SymPy and mpmath. It passed seven exact identities and 24 high-precision arc-lifetime integrations on six concrete test tuples, including both signs of the rotation parameters. The lifetime theorem for all admissible real parameters is proved analytically in `RESULT.md`; these finite computations are only consistency checks.

No continuation across the singular set is defined or tested. No independent audit has been performed.
