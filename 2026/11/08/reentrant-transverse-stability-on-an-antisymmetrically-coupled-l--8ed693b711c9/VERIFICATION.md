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

# Reproduction and limits

With Python 3 and SymPy available, run `python verify.py` in the extracted directory. The verifier uses exact symbolic and rational arithmetic to check the full coordinate map, both Floquet identities, the quadratic discriminant and derivative/minimum, direct period-two equations, all three witness multipliers, and strict unsaturated-coordinate bounds. Its expected success marker is `VERIFY_OK`.

The analytic proof in `RESULT.md` is responsible for the all-parameter conclusions. The verifier does not exhaust a continuum of parameters, prove a global attractor theorem or determine nonlinear dynamics at multiplier \(-1\). It gives a reproducible symbolic cross-check of the identities and one exact rational collection of physical witnesses; independent audit is not performed.
