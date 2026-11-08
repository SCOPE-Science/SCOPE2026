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

# Verification

The included `check_surface.py` is a standalone Python 3 verifier requiring NumPy, SciPy, and NetworkX. Invoke with `python check_surface.py`. The successful checked execution printed `TREE_ZONOTOPE_SURFACE_EXTREMAL_CAYLEY_CHECKS_PASSED`.

The verifier reconstructs incidence-column Gram determinants and omitted-column facet volumes for all unlabeled trees up to nine vertices; enumerates every unlabeled tree from five through eleven vertices to check the exact unique top two and bottom two surface areas; enumerates all Prüfer sequences in dimensions two through six for the exact Cayley mean; and evaluates the normalized expectation for several larger dimensions. All comparisons are numerical with explicit floating-point tolerances, except combinatorial counts. The infinite statement follows from the proof in `RESULT.md`, not from enumeration or numerical asymptotic checks.

The proof's combinatorial equality classification is independent of this executable. No claim of independent audit or formal proof certification is made.
