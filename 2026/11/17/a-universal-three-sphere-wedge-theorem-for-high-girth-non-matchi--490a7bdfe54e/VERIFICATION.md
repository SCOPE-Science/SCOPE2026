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
Run `python3 checks/verify.py` in a Python 3 standard-library environment. Its captured exact stdout appears in `checks/verify_output.txt`. The checker independently enumerates the full face sets by forbidden matchings and two-vertex covers, reconstructs reduced chain boundaries and ranks over the field with two elements, and verifies every purported simplicial edge-link and intersection equality at each prescribed chord insertion for nine test graphs (including cycle-rank-two tests). These finite tests corroborate but do not establish the all-parameter or integral theorem. The integral theorem follows from the explicit cover and homotopy arguments in `RESULT.md`, rather than extrapolation from mod-two ranks. An independent mathematical audit has not been performed.
