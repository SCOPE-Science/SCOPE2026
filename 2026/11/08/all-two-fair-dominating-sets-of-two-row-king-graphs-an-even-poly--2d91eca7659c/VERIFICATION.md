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

The proof is a combinatorial bijection with a disjoint word decomposition. The standalone checker `artifacts/verify.py` enumerates *actual labelled vertex subsets* of the two-row king graph for \(1\le n\le9\), testing every omitted vertex's exact two-neighbour condition; it does not assume the claimed word classification. A second test enumerates all ternary column words for \(1\le n\le12\), and a third checks predicted minimum degree, multiplicity and parity through \(n=200\).

The verifier finishes with `VERIFY_OK`. Finite computations are auxiliary cross-checks only. The arbitrary-length theorem rests on the proved local equivalence and run-length decomposition. No external or independent validation has been performed.
