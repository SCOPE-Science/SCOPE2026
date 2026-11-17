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

The included `check.py` was executed in Python 3 without third-party dependencies. It enumerated all 4,845 unordered four-vertex selections, computed exact signed determinants in \(\mathbb Z[\varphi]\), verified 4,845 independent Gram determinant identities, and checked the eleven-shell count and two geometric equality biconditionals. Its successful output begins with:

`DODECAHEDRON_TETRAHEDRON_SPECTRUM_PASSED vertices=20 configurations=4845 levels=11 runners_up=120 maxima=10 gram_checks=4845`

The finite test is exhaustive because the object has exactly twenty vertices and the checker uses the entire set of four-element index subsets. The assertion about arbitrary *contained* tetrahedra is limited to the global maximum and follows separately from affine multilinearity; there is no claimed discrete second-best threshold for continuously placed vertices. Historical novelty is provisional. The standard Euclidean metric and the displayed coordinate normalization are essential for the numerical volumes.
