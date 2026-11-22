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

# Verification scope

The proof is analytical: support-function integration, differentiation through a moving contact arc, strict height-crossing monotonicity, the complete-elliptic endpoint asymptotic, and the compact minimax threshold argument are described in `RESULT.md`. The transition exists for every radius and height after scaling, without claims of unique oblique minimizers.

Run `python check_cone_shadow.py` with NumPy and SciPy. This checker uses actual projected convex hulls of finely sampled rim vertices and apex points, contrasts them with elliptic quadrature and checks finite parameter grids, local stability, derivative signs and the illustrative numerical transition root. It passed 738 assertions on the examined environment. Its finite diagnostics do not replace the proof or furnish an interval certificate for the indicated decimal root.

The first precisely dated archival reference used is arXiv:1212.5946v1 (2012-12-24); a relevant 2001 projected-geometry paper was checked but its original day of public release was not established. No independent mathematical audit or separate external validation has been performed.
