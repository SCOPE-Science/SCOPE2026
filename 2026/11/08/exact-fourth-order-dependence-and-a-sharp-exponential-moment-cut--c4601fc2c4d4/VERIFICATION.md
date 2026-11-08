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

# Reproducibility and checks

Run `python3 check.py` (Python standard library only). The executable independently enumerates uniform-coordinate selectors to form the second-, fourth-, and cross-fourth-order coefficient expectations for all tested dimensions and exact rational steps. It checks the proposed stationary moment identities and the geometric-age second and fourth moments at the complete-reset step, and additionally compares a truncated Gaussian-mixture MGF with the closed formula away from the threshold. The attached `check_output.txt` records the actual execution.

The correct general proof is in `RESULT.md`. The finite assertions do not prove a statement about all dimensions, all admissible real step sizes, asymptotic stationarity, or convergence/divergence of the infinite MGF series. Those claims rest on the explicit coupling, stationary series, invariant moment equations, and exact geometric-series calculation. No independent audit was performed.
