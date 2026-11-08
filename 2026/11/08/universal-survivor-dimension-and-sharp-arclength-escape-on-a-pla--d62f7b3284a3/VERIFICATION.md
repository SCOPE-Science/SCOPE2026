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

# Computational and analytical verification

The proof is analytical and uses an eight-state inverse-branch matrix. For the specified map, exact substitution gives the core arrow list and expansion factors in RESULT.md. The determinant and the similarity-pressure polynomial are explicit identities. A graph-directed open-set condition follows from the disjoint relative interiors of inverse image segments. Perron–Frobenius convergence applies because the graph is strongly connected with coprime return loops.

The standalone script `check_survivor.py` tests exact endpoint images and ordered image decompositions at nine rational parameters, including both endpoints and the graph change, and uses SymPy for the exact determinant. Its expected status line is:

`POLYGONAL_CORE_EXACT_BRANCH_AND_CHARPOLY_OK parameter_samples=9 states=8`

Its numeric dimension and positive real decay root agree with the analytical expressions. This finite test cannot establish arbitrary-real-parameter correctness or general novelty; those depend on the proof and inspected literature.

No full-plane area distribution, independence certificate, or priority guarantee is claimed.
