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

# Reproducibility

Execute `python verify.py` under Python 3, standard library only. It enumerates priority permutations on 2 through 7 ordered keys; recursively constructs Cartesian search-tree fringe-interval sets; and independently checks all single- and double-interval probabilities against rational boundary and beta-integral expressions. It also checks the squared two-independent-tree pair probabilities and expected-size identities. The delivered run returned `PASS 1622 exact rational checks`.

# Limits

The file is a bounded exact finite-case verifier, not an enumerative proof for all input sizes and not an empirical justification of an infinite limit. The proof of the asymptotic claim appears in RESULT.md. Independent audit or external reproducibility confirmation has not been performed.
