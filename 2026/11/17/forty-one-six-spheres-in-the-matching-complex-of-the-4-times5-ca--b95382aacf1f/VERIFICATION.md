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

# Verification procedure

Install Python 3.10+ and SymPy, then execute `python verify_grid_4x5.py`. This standalone program constructs the complete \(P_4\square P_5\) graph with a fixed 31-edge ordering, and independently verifies the matching generating function by both face enumeration and vertex-deletion recursion. It enumerates the full face poset, applies the ordered edge matching to all nonempty faces, constructs the full oriented Hasse graph and verifies its acyclicity by topological sorting. It computes every coefficient of the integral signed Morse boundaries by recursive gradient-path elimination, checks a concrete \(-1\) determinant minor, the primitive seven-cell boundary, and the chain identity.

The expected exact console output is `expected_grid_4x5.txt`. These are finite exhaustive checks for one grid; the proof of the topological conclusion uses the standard acyclic discrete-Morse theorem and the fact that attaching maps to wedges of equal-dimensional spheres are classified by degree at their first nontrivial homotopy dimension.

The first motivating public preprint was posted on 2026-09-23 (arXiv:2609.27366). Its publicly accessible abstract is limited to three-row grids. The initial results have not been independently audited or validated by an outside mathematician. No claim of classification for other four-row widths is made.
