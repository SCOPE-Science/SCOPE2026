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

# Verification and limits

The full proof uses the hypercube's triangle-free adjacency graph, exact integration over a simplex, and torus Parseval. No outside lemma requires a computational black box.

Executable check: `python clipped_hypercube_check.py` with NumPy. It enumerates corner-removal decisions on 15 finite meshes in dimensions 2 through 4, compares empirical multiplicity frequencies with exact formulas, verifies the variance, and checks the planar consistency identity. Expected terminal marker: `CLIPPED_HYPERCUBE_THREE_LEVEL_PASS dimensions=2,3,4 cases=15`. The check was executed successfully from the included script. Approximate grids alone do not certify arbitrary real depths or unbounded dimensions; those follow from the proof.

The historical-priority check is necessarily bounded: some polytope Fourier formulas are accessible only through summaries. No claim of independent audit or mathematical certification is made.
