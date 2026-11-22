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

The standalone `verify.py` uses no nonstandard Python libraries. Execute `python3 verify.py` and check for the exact terminal string `DODECA_THREE_TORI_LENGTH_TEN_OK`.

The program constructs all 20 vertices and 30 edges, 1,168 canonical undirected simple cycles, and exhaustively checks all 56 pairwise vertex-disjoint cycle triples. It uses the reduced weight-three graph-configuration chain groups with ranks \(C_3=9,120\) and \(C_2=22,800\). It checks the exact integral boundaries of every signed torus product, computes the boundary rank 9,094 over \(\mathbb F_2\), and finds determinant-one minors of sizes 20 and 26 for the short-cycle and full-cycle integral lattices respectively.

Every one of the 30 octagon-containing torus chains is proved to be the sum/difference of two pentagon torus chains by checking the resulting integer vector in **all 9,120** coordinates. This certifies \(L_5=L_8\) while the 26x26 unit minor and rank bound certify \(L_{10}=H_3\cong\mathbb Z^{26}\). The 20x20 unit minor certifies that \(H_3/L_8\cong\mathbb Z^6\), not a finite-index quotient with undetected torsion.

The calculation is exhaustive for this graph only. Mod-two rank alone does not establish the integral conclusion; the integer unit minors are essential. The comparison of reduced chains with continuous graph-configuration homology is an established external published theorem, not implemented as a geometric homeomorphism in the program. The included execution output supports reproducibility but is not an independent review.
