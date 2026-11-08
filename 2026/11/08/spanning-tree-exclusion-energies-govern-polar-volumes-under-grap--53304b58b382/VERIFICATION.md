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
# Reproducibility and verification

Execute `python artifacts/verify.py` with Python 3 and SymPy installed. The program uses integer and rational arithmetic for graph Laplacian cofactors, fundamental cycle matrices, transfer-current diagonal identities, exact binomial box-spline central densities, and exact integrated cubic spline products.

The checked set comprises triangle, four-cycle, diamond, complete bipartite \(K_{2,3}\), complete graph \(K_4\), a triangle with a bridge, and a figure-eight cactus. Four uniform subdivision factors were checked per graph for spanning-tree scaling (28 graph tests). Central-box-spline calculations included 12 cycle-length profiles, 4 two-pole three-path products and 5 additional triangle subdivision profiles, totaling 21 exact-volume profiles. Its completion marker is `GRAPH_POLAR_SUBDIVISION_CHECKS_PASSED graph_checks=28 exact_volume_checks=21 graphs=7`.

The code verifies finite samples and separate exact finite-dimensional formulas. It cannot by itself certify the asymptotic remainder for arbitrary fixed graphs or uniqueness relative to all historical literature. The analytical Fourier-dominance argument and graph-identification proof are in `RESULT.md`. No independent mathematical audit has been performed.
