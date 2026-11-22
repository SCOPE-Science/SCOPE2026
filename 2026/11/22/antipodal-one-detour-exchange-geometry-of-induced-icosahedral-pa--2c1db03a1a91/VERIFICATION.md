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

The two independent standard-library implementations may be replayed with:

```
python3 verify_partition.py
g++ -std=c++17 -O2 verify_partition.cpp -o verify_partition
./verify_partition
```

Both executions print `CERTIFICATE_PASS`. Their recorded outputs are included as `verify_python.out` and `verify_cpp.out`.

`verify_partition.py` provides a fixed complete edge list and a disjoint-set acyclicity test. `verify_partition.cpp` separately constructs the same graph using two pentagonal rims and tests the exact edge-versus-component forest identity. The explicit relabeling of the two graph models appears in `RESULT.md` and was checked on all thirty edges. Both enumerate the whole twelve-vertex configuration space, all feasible one-out/one-in exchanges and every shortest-path distance, rather than samples.

The common results include sixty feasible named bipartitions, 120 exchanges, degree four throughout, connectedness, bipartite shores of thirty each, diameter six, unique complementary antipodes and 420 pairs at one-exchange excess over Johnson distance. The Python program additionally computes the exact girth six by shortest alternative paths after edge deletion. The independent C++ code provides a distinct finite predicate and graph construction; agreement is a cross-check, not independent institutional certification.

The already published count of sixty six-vertex forest faces is explicitly credited and not treated as a newly discovered number. The exchange metric and adjacency claims do not extend to arbitrary regular polyhedral graphs without additional work.
