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

Exact finite verification for two named fifteen-vertex line graphs. The two C++ programs reconstruct the entire state space independently using different classification methods, rather than sampling states. In the `verification` directory, compile and run:

```
g++ -std=c++17 -O3 classify.cpp -o classify
g++ -std=c++17 -O3 check_independent.cpp -o check_independent
./classify 1
./classify 2
./check_independent 1
./check_independent 2
./classify 1 --reps > generated_1.txt
./classify 2 --reps > generated_2.txt
cmp generated_1.txt reps_1.txt
cmp generated_2.txt reps_2.txt
python3 check_symmetry.py
```

`counts_1.txt` and `counts_2.txt` record the complete period/entry histograms from the first classifier, including the maximum times and period-specific state counts. `reps_1.txt` and `reps_2.txt` each contain every primitive temporal cycle of length four or more, one phase representative per line. The Python checker recomputes all base-graph automorphisms and induced edge permutations, checks exact temporal least periods, and partitions these lists under their full automorphism groups. The independent classifier prints the same nonzero period/entry cells with slightly different labels. The complete exhaustive methods, their deterministic graph encodings and the logic connecting these checks to the claims are in `RESULT.md`.

No claim is made for other graphs or excitation thresholds. Neither simulation nor finite verification would establish a universal line-graph preservation principle. No external independent validation has been conducted.
