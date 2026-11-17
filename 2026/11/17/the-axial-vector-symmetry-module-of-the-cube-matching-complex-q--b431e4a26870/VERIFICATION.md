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
# Reproducibility and scientific boundaries

Execute `python3 verify_cube_matching.py` from this package in a Python 3 environment. The verifier requires only the standard library and regenerates the cube graph and all its matchings from binary-coordinate definitions. It computes three boundary ranks by exact mod-two bit elimination, enumerates all 48 signed coordinate permutations and all 107 nonempty faces, and evaluates all signed Lefschetz traces. It checks the proposed character identity on each element and all ten conjugacy classes, exact character norms and five subgroup averages. A complete run terminates with `Q3_MATCHING_EQUIVARIANT_PASS`; the recorded output is `verification_output.txt`.

The mod-two elimination proves characteristic-zero ranks because the chain-complex inequalities supply matching upper bounds, as justified in RESULT.md. The 48-element trace check is exhaustive for the specified cube, not a heuristic random sample. Integral homology torsion, integral symmetry splitting, equivariant homotopy equivalence and higher-dimensional hypercubes are outside the theorem. Quotient calculations refer to ordinary topological quotients with rational coefficients. No independent mathematical audit has been performed.
