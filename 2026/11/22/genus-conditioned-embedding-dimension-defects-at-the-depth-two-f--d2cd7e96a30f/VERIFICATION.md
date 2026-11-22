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

# Verification notes

The package's `VERIFY.py` independently calculates semigroup closure, genus, and irreducible positive elements for a finite grid of multiplicities and Frobenius offsets. It enumerates fixed-cardinality subsets to check the hypergeometric coefficient formula and uses exact rational arithmetic for the unconditional mean. Execute with `python3 VERIFY.py` from the extracted package. Executing this embedded checker yielded `VERIFY_OK: 1013 semigroups, 91 finite hypergeometric conditions`. Passing finite tests does not establish the infinite statements; those are proved by hypergeometric convergence, coupling, geometric tails, and Slutsky's lemma in RESULT.md.

The review is same-model only. Independent audit has not been performed.
