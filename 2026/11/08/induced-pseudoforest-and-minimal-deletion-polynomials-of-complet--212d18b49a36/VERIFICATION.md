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

# Verification details

The theorem is proved in `RESULT.md`. The finite checker `pseudoforest_verifier.py` is a separate standard-library-only implementation of the object definitions and a graph-level inclusion-maximality test.

Run `python3 pseudoforest_verifier.py` in the extracted artifact directory. During the self-review the script emitted:

```
VERIFY_OK graph_instances=52 candidate_subsets=41384 balanced_arithmetic_orders=47
```

The 52 graphs are nonisomorphic-by-sorted-profile checks with three to five positive part sizes and order at most twelve. Each candidate subset was tested using adjacency and connected-component edge counts; all one-vertex extensions were checked for maximality. The same program tests the specialized balanced-tripartite coefficient identities for 47 further positive parameters. The finite checks do not establish the infinite theorem or independent validation; both follow the exact mathematical proof only in the former case. The search for prior equivalent complete enumerators was inconclusive as a guarantee of publication priority.
