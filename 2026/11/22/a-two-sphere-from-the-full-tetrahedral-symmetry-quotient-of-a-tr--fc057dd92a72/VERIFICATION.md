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

The complete finite certificate is `collapse_pairs.json`. The standalone Python 3 verifier `verify.py`, using no nonstandard libraries, recomputes the graph, its twenty-four label permutations, all 162 nonempty independent faces, all 3,342 nonempty strict flags, all 146 orbit cells and the codimension-one incidences. It checks every one of the 60 declared elementary collapse pairs on the evolving remaining complex, rather than merely verifying the total number of pairs. It confirms the six-vertex, twelve-edge, eight-triangle residual, every edge's two triangle incidences, each vertex's cyclic link (including multiplicity of parallel link edges), connectedness and Euler characteristic two.

Run: `python3 verify.py` in the directory containing both artifacts. The successful output is in `verify_output.txt` and begins `PASS_TRUNCATED_TETRAHEDRON_FULL_QUOTIENT_SPHERE`.

Finite verification is exhaustive for the specified twelve-vertex graph and complete symmetry group. It is not a proof about any larger truncated simplex, and it does not establish publication priority or independent mathematical validation.
