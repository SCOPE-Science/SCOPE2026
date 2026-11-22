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

# Finite certificate and reproducibility

This package enumerates two representative singleton endpoint classes of three-state binary epsilon-free NFAs: coincident initial/final state and distinct initial/final states. Their exhaustive \(512^2\) transition-pair domains cover every possibility, including empty transition images. Relabeling contributes multiplicities three and six for the all-labeled result.

The exact census data are contained in `data/joint_spectrum.csv`. To recompute every row (not simply inspect a stored report), from the directory containing `RESULT.md` run:

```sh
g++ -std=c++17 -O2 verify/partition_enumeration.cpp -o /tmp/nfa_partition
/tmp/nfa_partition data/joint_spectrum.csv
python3 verify/distinguishability_enumeration.py data/joint_spectrum.csv
```

The C++ program computes BFS of reachable powerset states, successive partition refinement and forward/backward trimness. The independent Python program computes reachable subsets, backward fixed-point propagation of distinguishable state pairs and trimness. Both assert exact equality with every one of the 62 nonzero CSV rows, absence of extra nonzero rows, and the \(262{,}144\) domain size for each case. The pair propagation is complete because new distinguishable pairs arise from a strictly bounded set of at most \(28\) unordered subset pairs; no timeout or sampling substitutes for exhaustion.

Successful executions returned the following messages:

```text
PASS partition census: 62 cells, two 262144-machine families, trim 190080 and 209664
PASS distinguishability census: 62 cells, 524288 transition/final cases
```

The proof relies on finite exhaustive computational enumeration; the supplied programs can be independently run, but no outside verification has been performed. Larger NFAs, multi-initial or multi-final automata, epsilon transitions and general alphabet-size distributions are not certified by this result.
