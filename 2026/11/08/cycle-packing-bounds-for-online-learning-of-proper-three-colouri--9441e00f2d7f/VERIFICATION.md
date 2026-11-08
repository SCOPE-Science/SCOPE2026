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

Run `python3 check_cycle_packing.py` using Python 3 and no third-party dependencies. The checker constructs the proper three-colouring concepts directly and recursively computes the exact maximum depth of a complete binary mistake tree by partitioning on each vertex-colour equality query. Independently it enumerates vertex-disjoint cycle packings. It asserts the cycle-packing bound for tested graphs, the exact pseudoforest equality, and the forest equality condition. It also tests the finite bicyclic boundary instance by an exhaustive dimension recursion.

The recorded output was:

```
EXHAUSTIVE_ALL_GRAPHS_PASS 924 pseudoforests 501
EXTENDED_PASS 21 BOWTIE_4_4_LDIM_6_PASS
```

The first line covers every graph with up to four vertices, plus five-vertex graphs having at least four edges. Additional explicit cycles and pendant-cycle graphs and paths and stars are checked. These are finite checks only. The unrestricted formula follows from the constructive proof in `RESULT.md`; the two-square boundary case is an exact finite computation with the full executable recurrence. The independent audit has not been performed.
