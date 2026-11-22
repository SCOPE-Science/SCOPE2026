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

# Reproducible finite checks

From a directory containing the six document files, the two verifier source files and the two expected-output files, run:

```
python3 verify_crossfree.py > python_actual.txt
diff -u python_expected.txt python_actual.txt
g++ -O3 -std=c++17 verify_crossfree.cpp -o verify_crossfree
./verify_crossfree > cpp_actual.txt
diff -u cpp_expected.txt cpp_actual.txt
```

These commands were executed with both comparisons returning success. The Python implementation represents unordered disjoint colour classes by canonical 13-bit masks. The C++ implementation uses a 13-position base-four digit assignment and canonicalizes colour names; it tests every allowed swap with a zero-position. Both independently build the cyclic Steiner system from two 13-translate generators, apply the four-block Pasch switch, and validate exactly one triple per point pair. The Python implementation additionally checks class overlap (3868 states in both versions), degree divisibility, small component shapes and the six-leaf triangle decomposition in every seven-state motif. The C++ implementation verifies every reverse graph edge and degree profile in each component. Reproducing a finite count does not establish any general theorem about higher Steiner orders.

For analytical checks, the 26 blocks per system and six blocks incident with any point imply at most three points per cross-free class by a 20-versus-18 pair-count contradiction. The all-or-none insertion lemma implies every valid insertion in one three-point class gives three possible one-point removals, proving degree divisibility by three. The programs enumerate all 200200 unordered candidate placements in each design and do not rely on randomized trials.

No external or independent scholarly audit has been performed. The public-literature priority check is subject to unindexed records.
