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

# Computational verification

Run `python3 verify.py` in the same directory. Only Python 3 standard-library modules are required. The checker independently constructs the binary de Bruijn graph and checks every theorem missing-pattern triple with exact fraction-free integer Laplacian cofactors for window orders \(3\) through \(8\). It separately counts edge-labeled Euler tours for orders \(3\) through \(5\), enumerates all three-edge sets and verifies that only the four predicted missing triples are balanced at those orders, and verifies the explicit period-three three-by-three overlap determinant for periods \(2\) through \(15\). The replay of the embedded script completed with the `VERIFY_OK` marker and exact finite totals listed in the result.

These finite checks cannot certify an infinite statement. The infinite theorem relies on the stated graph-theoretic bijection, the BEST theorem, the shift-chain identity \(P^m=J\), and the three-by-three symbolic residue calculation. In particular, a zero determinant at window order \(3\) is interpreted as no Euler tour, not as a computational timeout. No independent audit was performed.
