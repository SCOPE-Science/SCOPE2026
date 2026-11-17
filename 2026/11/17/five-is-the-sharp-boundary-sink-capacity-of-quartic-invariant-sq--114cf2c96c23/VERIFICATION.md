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

The reproducibility script `check_boundary_sinks.py` uses only the Python standard library. Its exact quadratic-field arithmetic verifies the four edge-root formulas, all root bounds, the two Jacobian eigenvalues at each of the eight open-edge equilibria, and the two diagonal eigenvalues at each corner. Its asserted classification is five sinks, six saddles, and one source, with no zero eigenvalues.

The universal five-sink bound is proved in `RESULT.md` using a boundary equilibrium count, one-dimensional sign alternation, and common leading-coefficient signs across opposite sides. It does not rely on the finite checker. The degeneracy argument uses structural persistence of hyperbolic equilibria within this invariant-square coefficient family.

The literature comparison concerns statements and their logical implications: interior limit-cycle counts and boundary-equilibrium counts for a constrained subfamily do not furnish the all-factor maximal boundary-sink count. Equivalent statements in unindexed literature remain possible. Independent mathematical verification has not been performed.
