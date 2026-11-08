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
# Reproducible mathematical verification

The main proof is the natural integral homology spectral sequence of the sphere-and-simplex cover, with its action on suspension apices and six-cycle orientations. The uniform isomorphisms do not rely on any finite test.

The standalone standard-library program `verify_crown_forest.py` independently uses depth-first search for acyclicity on every vertex subset of crown graphs with \(3\leq n\leq7\). It reconstructs boundary matrices over \(\mathbb F_2\), checks the predicted ranks, constructs the \(\binom n3\) integral four-cycle chains and checks their signed boundaries. For all \(S_n\times C_2\) group elements for \(3\leq n\leq6\), it computes fixed oriented simplicial-chain supertraces from vertex orbits, then compares them with the two module-character formulas. The actual output is included as `verification_output.txt`, ending `CROWN_FOREST_EQUIVARIANT_CHECK_PASS`.

The finite verification covers 1,740 individual actions and does not prove the whole infinite family, identify integral third-degree chain bases computationally, or establish equivariant homotopy equivalence. Its use of mod-two arithmetic for the numerical homology cross-check is not an integral torsion proof; the independent integral cover argument and prior integral homotopy classification provide that part. The original homotopy type and sphere multiplicities are established in Carnero Bravo's Proposition 41, rather than first found here.
