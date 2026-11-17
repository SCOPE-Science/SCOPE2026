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

The verifier `verification/verify_prime_associahedral_quotient.py` is self-contained apart from the open-source SymPy Python package. Execute it with `python verification/verify_prime_associahedral_quotient.py` and compare the complete output to `verification/verified_output.txt`. It enumerates every simplex of each diagonal complex at the two tested prime sizes, applies all rotations to oriented simplices, and forms the cellular boundaries of the free face-orbit quotient, with permutation signs. It checks the chain identities and computes integer Smith invariants.

For the seven-gon it verifies 14 original vertices, 56 edges, 84 triangular faces and 42 tetrahedral facets; quotient cell counts are 2, 8, 12 and 6. The reduced first boundary has Smith invariants 1,1,1,1,1,1,7, confirming the cyclic first homology of order seven. All five nonzero Smith invariants of the third boundary are units, excluding hidden second-homology torsion once the rational ranks agree. The fifth polygon quotient is a circle.

The general proof instead uses the classical secondary-polytope model, its explicit three affine relations, the full Fourier decomposition of the remaining real representation and standard weighted-lens-space topology. Computations of two polygons do not imply the infinite-prime statement. The complete homeomorphism claim has not been independently audited.
