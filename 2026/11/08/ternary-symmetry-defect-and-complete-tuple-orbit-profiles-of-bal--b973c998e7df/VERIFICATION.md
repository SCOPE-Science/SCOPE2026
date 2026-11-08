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

Run `python checker.py` with Python 3 and its standard library. The executable directly enumerates Venn cell signatures of ordered distinct tuples for small balanced Johnson graphs and compares ground-permutation orbit counts, full graph-automorphism orbit counts, and complement-fixed counts with independently computed signed-Stirling formulas. It verifies the ternary interval method, an independent two-subset-stabilizer method, the parity formulas for all \(2\le k\le25\), and the complete automorphism group of \(J(4,2)\). The last check enumerates all permutations of the six vertices and tests graph adjacency. The expected final line is `ALL_CHECKS_OK`.

This finite executable does not prove claims for arbitrary \(k\) and \(r\). The infinite proof is the Venn-cell classification, Burnside averaging, equality-pattern inversion, three-way-cell inequalities, and rational-polytope lattice-point asymptotics in `RESULT.md`. Historical priority is not independently certified, and some earlier association-scheme literature remains to be checked independently.
