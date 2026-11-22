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

# Reproducibility and mathematical limits
Run `python3 verify_hypergraph.py`. The program is self-contained and builds the intersection partition lattice and candidate nerve from the given nine edges, not from stored expected faces. It verifies every announced strict-lower-interval type and every one of the 18 explicitly stored elementary-collapse pairs. It independently checks triangle incidence, all vertex links, connectedness, orientability and Euler characteristic of the remaining closed surface. Its terminal message is `HYPERGRAPH_COLORING_TORUS_WEDGE_VERIFIED`.

The verification supplies the finite combinatorial input to the published Wedge Lemma/Proposition 19 and does not independently reprove that general theorem. The known integral cohomology ranks provide an external cross-check of the resulting homotopy type, but homology alone is not used to infer the wedge decomposition. No independent audit has been performed.
