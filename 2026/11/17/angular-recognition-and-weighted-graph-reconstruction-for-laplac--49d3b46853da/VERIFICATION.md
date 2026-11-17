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

# Reproducibility and scientific limits

The proof is contained in `RESULT.md`. A separate numerical checker, `checker.py`, uses NumPy eigendecompositions to compute graph Laplacians, their pseudoinverses, facet-normal cosine matrices, and the proposed inverse. Execute `python checker.py` in the directory containing the checker, with Python 3 and NumPy.

The checked version ran successfully and printed `GRAPH_LAPLACIAN_ANGULAR_INVERSE_PASS connected_simple=770 rational_weighted=770`, `NON_GRAPH_POSITIVE_OFFDIAGONAL_REJECT_PASS`, and `CHECKER_PASS`. The 770 simple graphs exhaust the connected labeled loopless graphs on 3, 4, and 5 vertices; each was tested both with unit weights and with a deterministic assignment of positive rational weights. Tests checked reconstruction up to one scalar, equality of the full reconstructed angular Gram, nonedge zeros, and equal unit-edge conductances. One non-graph centered positive-semidefinite matrix with positive off-diagonal was rejected by the sign criterion.

Computational enumeration here is finite. The general proof uses positivity, the one-dimensional kernel, exact facet normal products, and the positive-semidefinite functional calculus. The checker uses nonzero tolerances for eigenvalue truncation and matrix comparisons. Exact recognition of whether a weight equals zero is a mathematical sign condition, not a certified floating-point decision. No third-party independent mathematical audit has been performed.
