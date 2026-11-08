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

The exact formula and optimum classification are proved analytically in RESULT.md. Reproduce finite rational checks with Python 3 and SymPy: `python verify_two_rungs.py`. The program constructs an independent Laplacian and evaluates the rational Kirchhoff trace identity for all placements through seven vertices per rail, and enumerates all two-rung positions for path lengths through 100. These finite checks do not establish all-order truth, which is supplied by the displayed proof. No independent audit has been performed.
