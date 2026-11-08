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

# Exact finite-chain verification

Run `python3 verify.py` from the directory containing `certificate.json`. All calculations are deterministic and use only Python 3's standard library. Every oriented simplex of \(\Delta_{5,5}\) is explicitly generated. The program computes the complete mod-three boundary matrices by sparse Gaussian elimination, verifies the eight-triangle cycle is not a boundary, and checks the row, column, and board-transpose actions. The separately stored sixty-tetrahedron \(\mathbb F_3\)-chain has boundary equal to the transpose of the stated cycle plus the cycle; each coefficient is recomputed from the displayed simplex ordering. The program also confirms the rank calculation giving one-dimensional degree-two mod-three homology.

The recorded output appears in `verification_output.txt`. The noncomputational premise \(\widetilde H_2(\Delta_{5,5};\mathbb Z)\cong\mathbb Z/3\) is from Shareshian–Wachs and Jonsson; applying integral reduction and elementary group representation arguments then proves the torsion action. The quotient corollary uses barycentric subdivision and the exactness of coinvariants for an order-two group over \(\mathbb F_3\). No independent mathematical audit has been conducted.
