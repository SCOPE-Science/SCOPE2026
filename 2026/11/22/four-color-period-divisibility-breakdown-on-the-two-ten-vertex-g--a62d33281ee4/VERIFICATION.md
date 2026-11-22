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

The finite state space has \(4^{10}=1{,}048{,}576\) configurations per graph. Both supplied C++17 programs compute every transition for each graph and map, with different graph embeddings and cycle algorithms.

```
g++ -O3 -std=c++17 compare.cpp -o compare
./compare > current_compare.out
diff -u compare.out current_compare.out
g++ -O3 -std=c++17 verify_indegree.cpp -o verify_indegree
./verify_indegree > current_verify_indegree.out
diff -u verify_indegree.out current_verify_indegree.out
python3 verify_witness.py
```

`compare.out` contains every nonempty first-entry/period class as well as the joint tables; `verify_indegree.out` independently repeats the joint census. The programs are complete exhaustive integer calculations rather than randomized samples. A third small checker directly traces both featured configurations, confirming that CCA becomes fixed and GHM has a primitive five-cycle. The remaining limitations are historical novelty uncertainty, confinement to two finite graphs, and lack of external independent mathematical validation.
