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

# Verification record

The proof is analytical: eight vertex heights, a finite cube-edge incidence count, spherical coarea on three transverse great-circle arcs, pairwise strip intersection geometry, and strict Jensen convexity. This resolves the \(O(|t|^3)\) normalization locally for every fixed positive aspect ratio.

For a separate numerical diagnostic, run `python check_near_center.py` from the same directory. It uses a fixed seed and NumPy, enumerates the 12 box edges, and compares five-edge intersections to the one-strip condition. Successful local execution returned:

`VERIFY_OK boxes=4 offsets=12 plane_sections=16800000 independent_edge_count_equivalence=16800000`

A Monte Carlo tolerance incorporates sampling uncertainty and an allowed third-order remainder. It is not a certificate for the asymptotic coefficients or mathematical uniqueness. No external independent audit has been performed.
