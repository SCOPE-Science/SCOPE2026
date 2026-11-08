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

Run `python3 verify.py` with Python 3.9 or later; only the standard library is used. The executable checks exact-rational stochasticity, symmetry, complete trace-decomposition identities for cycles, complete and edgeless graphs, hypercubes and cocktail-party graphs, the precise characteristic polynomial of the strict nonvertex-transitive path-cone witness, and the sharp four-cycle nonedge-bound example. The observed output was `VERIFY_OK exact_rational_checks= 895`.

The proof of the all-graph upper bound and all-vertex-transitive equality is the operator-norm, automorphism-averaging and invariant-subspace argument in `RESULT.md`. Finite exact arithmetic checks support the stated formulas but do not enumerate all graphs or independently certify the infinite result. The converse statement beyond vertex transitivity is explicitly **not** claimed, and the path witness demonstrates strict failure. Self-review is reported in `REVIEW.md`; independent validation has not been performed.
