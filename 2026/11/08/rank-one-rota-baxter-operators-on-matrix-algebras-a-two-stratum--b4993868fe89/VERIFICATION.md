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

# Verification

Run `python3 verify.py` from the extracted package directory. The expected final message is `VERIFY_OK_RB_RANK_ONE`.

The program enumerates all pairs of nonzero matrices \(B,C\) in \(M_2(\mathbb F_2)\) and \(M_2(\mathbb F_3)\), checks the Rota–Baxter identity directly on matrix-unit pairs, and confirms equivalence to the necessary-and-sufficient classification. It computes each rank-one operator's multiplicity correction of \(q-1\) for the factorization \((B,C)\). For \(M_3(\mathbb F_2)\), it exhaustively checks the classification for all nonzero pairs, directly checks every classified pair and a deterministic sample of nonclassified pairs. It then compares to the independently implemented Gaussian-binomial count.

The observed counts, including the zero operator, are \(16,57,652\) in the cases \((n,q)=(2,2),(2,3),(3,2)\). Additional arithmetic tests cover small \(n\) and several prime-power parameters, checking integrality and boundary values.

These checks do not exhaust all characteristics and sizes; the general theorem depends on the displayed algebraic proof. Nothing in the package constitutes an independent external mathematical audit.
