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

# Reproducibility and verification

The accompanying `verify.py` uses exact Python integers and the standard library only. Run `python3 verify.py` from this directory. It prints `VERIFY_OK` only after every asserted comparison succeeds.

The code constructs the friendship graph adjacency lists independently of the closed formula and recursively enumerates all legal pebbling moves. Every move lowers the total pebble count by one, so the recursion is finite. It exhaustively checks all labelled nonnegative configurations with totals two through eleven on one triangle, totals two through twelve on two triangles, and totals two through twelve on three triangles. No graph automorphism quotient is used in this main test. It also checks the defect move inequalities and eventual affine parity in a large integer window and directly checks critical configurations for two through nine blades.

Successful replay output:

```
LOCAL_DEFECT_AND_PERIODICITY_OK
LABELLED_GRAPH_EXHAUSTIVE_OK 1 through_size 11 configurations 360 cache 362
LABELLED_GRAPH_EXHAUSTIVE_OK 2 through_size 12 configurations 6182 cache 6184
LABELLED_GRAPH_EXHAUSTIVE_OK 3 through_size 12 configurations 50380 cache 50382
CRITICAL_UNIQUE_OBSTRUCTION_PATTERN_OK 2
CRITICAL_UNIQUE_OBSTRUCTION_PATTERN_OK 3
CRITICAL_UNIQUE_OBSTRUCTION_PATTERN_OK 4
CRITICAL_UNIQUE_OBSTRUCTION_PATTERN_OK 5
CRITICAL_UNIQUE_OBSTRUCTION_PATTERN_OK 6
CRITICAL_UNIQUE_OBSTRUCTION_PATTERN_OK 7
CRITICAL_UNIQUE_OBSTRUCTION_PATTERN_OK 8
CRITICAL_UNIQUE_OBSTRUCTION_PATTERN_OK 9
VERIFY_OK
```

These are finite checks, not an infinite proof or an independent audit. The unrestricted correctness rests on the five-case move inequalities, the constructive blade reduction, the central-stack perturbation, and the exact defect-sum argument provided in `RESULT.md`. The historical originality comparison is provisional.
