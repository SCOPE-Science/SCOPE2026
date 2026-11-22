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
# Reproducible checks

The analytic proof covers every integer \(n\ge5\) and is not inferred from finite enumeration. To reproduce the finite checks:

```sh
c++ -O3 -std=c++17 verification/functional_graph.cpp -o functional_graph
c++ -O3 -std=c++17 verification/direct_forward.cpp -o direct_forward
./functional_graph 3
./functional_graph 4
./functional_graph 5
./functional_graph 6
./direct_forward 5
./direct_forward 6
```

The functional-graph program constructs a complete labelled state transition array, traverses every transient, and reports the complete recurrent-component period spectrum and maximal entry depth. The independent forward program applies the update repeatedly from every base-three state and counts the earliest all-rest time. The two methods agree on extinction and sharp maximum four for the orders five and six. The forward histograms are provided in the finding and sum to the exact state-space cardinalities. Independent external checking has not been performed.
