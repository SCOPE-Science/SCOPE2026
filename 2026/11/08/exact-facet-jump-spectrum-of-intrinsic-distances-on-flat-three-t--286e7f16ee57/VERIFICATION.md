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

The analytical proof establishes the identity for every rank-three Euclidean lattice. The reproducibility script `check.py` independently evaluates the exact spherical-cap truncation formula on a rectangular Voronoi cell, numerically checks the first two jumps, and compares five exact cumulative probabilities with a Sobol sample of size \(2^{20}\). The script uses Python 3 with the `numpy` and `scipy` dependencies listed in `requirements.txt`, and completed with `TORUS_FACET_CHECK_OK`.

The use of a box tests normalization, signs, powers, and factor-of-two conventions; it is not an exhaustive verification over lattices. The key global lemma is analytical: the first derivative of spherical-cap union area is continuous at any parameter that is not a cap birth, including simultaneous changes in exposed cap arcs. No experiment proves that infinite-dimensional or non-Euclidean analogues hold, and none is claimed.
