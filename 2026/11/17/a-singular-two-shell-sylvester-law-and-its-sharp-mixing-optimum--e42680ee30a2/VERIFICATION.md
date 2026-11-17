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

The derivation is self-contained. To run the finite numerical diagnostic, install dependencies from `requirements.txt` and execute `python verify_two_shell.py`. The checker uses deterministic pseudorandom sampling and the strict barycentric inclusion test for four-point planar convexity; no external datasets are required. Its finite estimates are nonproof diagnostics. Exact critical proof checks are the almost-sure limiting inclusion criteria, the independent uniform direction of the difference of two circular points, the random semicircle origin criterion, uniform convergence of five Bernstein weights, and calculus for the unique minimizer. No independent audit or external mathematical certification was performed.
