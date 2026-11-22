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

The finite script `verify.py` directly checks induced-four-path exclusion and adjacency traces using integer bitsets. On execution it produced:

```text
VERIFY_OK exhaustive_cographs=6039 exhaustive_parameter_cases=362227 extremal_witnesses=12 randomized_cotree_cases=5000
```

The checks enumerate all labeled simple graphs through six vertices that are \(P_4\)-free and all nonempty parameter sets therein. A separate family of exact constructions for \(m\in\{1,\ldots,12\}\) tests external trace equality and the full-graph \(P_4\)-free property. Randomized cotree tests use a fixed reproducibility seed. The critical general proof is the union/join induction and the distinct full-binary-tree leaf-set construction given in `RESULT.md`. Empirical checks do not establish the theorem for unbounded sizes; they are supportive. No independent mathematical audit has been carried out.
