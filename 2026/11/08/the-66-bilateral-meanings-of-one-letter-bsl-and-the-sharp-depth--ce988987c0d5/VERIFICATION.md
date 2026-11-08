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

Run the two independently implemented source files in this directory with Python 3:

```sh
python3 checker.py
python3 checker_direct.py
```

Expected success markers are `BSL_BILATERAL_ONE_ATOM_OK` and `INDEPENDENT_SET_SEMANTICS_OK`. Both report the finite depth-count sequence `[39, 64, 66, 66]`. The first checks all 66 table entries, all unary closures, all ordered pairs for both binary closures, the two new depth-two elements, the precise internal-\(\Diamond\) witness, and the number 11 of support projections. The second uses actual finite sets of valuations and teams to reconstruct the operators from their semantic definitions, rather than reusing bit-operation code.

There are exactly four teams and a finite table of \(66\) candidate pairs, so these are full deterministic checks over the claimed domain, not numerical samples. An induction on formula construction identifies arbitrary formulas with the least algebra of paired meaning profiles, and the finite table is closed under every primitive connective. Consequently the evidence establishes the unbounded-syntax statement. The programs do not prove any theorem outside the one-variable setting and do not establish historical priority. No independent audit has been performed.
