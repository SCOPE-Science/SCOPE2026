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

# Mathematical verification
The files `certificate.json` and `verify_cube_prism.py` provide complete, standalone finite tour and rational-cone evidence. Execute `python3 verify_cube_prism.py` in their directory. It checks all 247 subsets through 32 symmetry orbits, with two tour/inequality certificates per orbit; no floating point or external packages are used for replay. The analytic part proves the cone-generating inequalities for all positive aspect ratios and determines both sharp crossing values. Strictness of noncandidate orbits follows because their certificate differences contain a positively weighted inequality strict at every allowed positive aspect ratio, after excluding only the two established witness orbits. This check does not address points off the prism corners or historical research priority. Independent audit: not performed.
