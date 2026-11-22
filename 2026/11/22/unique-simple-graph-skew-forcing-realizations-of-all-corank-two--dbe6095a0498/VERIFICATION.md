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

The supplied standard-library checker `verify.py` was executed on 232 labelled multipartite-with-isolates instances, covering 101,132 starting subsets. In every instance it compared the iterative skew forcing closure with the rank formula of the dual rank-two matroid on all starting sets, checked that minimum forcing sets were exactly complements of edges, and verified the Tutte polynomial at four integer evaluation pairs where the total vertex count was at most eight. Its actual output was:

```
GRAPH_INSTANCES 232
INITIAL_SUBSETS_CHECKED 101132
DUAL_CLOSURE_MINIMUM_SET_AND_TUTTE_CHECKS_OK
VERIFY_OK
```

The symbolic derivations and the use of DeAlba's connected-graph characterization are given in RESULT.md. The finite test is supporting evidence, not an exhaustive check of arbitrary orders or a substitute for proof. Independent mathematical audit has not been performed.
