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

# Verification record

The closed-neighborhood and symmetric-difference reduction is proved in `RESULT.md`; it is sufficient and necessary for identification, not an approximation. The exact primary checker computes every detector subset for dimensions two through six and both a complete lower-bound search and the entire equality layer in dimension seven. In the latter, branching on every element of an unmet requirement is exhaustive. Pruning by a family of pairwise disjoint unmet requirements only discards branches that need more additional detectors than the allowed budget. The complete twelve-detector equality layer consists of thirteen distinct sets.

Reproduction:

```sh
g++ -std=c++17 -O3 fib_identifying_verify.cpp -o verify
./verify
g++ -std=c++17 -O3 fib_identifying_alternate.cpp -o alternate
./alternate OPTIMA_N7.tsv
```

The expected stdout markers are `VERIFY_OK` and `ALTERNATE_OK`. The main verifier reports 1,345,072 recursive calls for the impossible eleven-detector threshold and 14,117,207 for the twelve-detector equality search; the second checker independently examines every reflection-orbit selection at dimension seven and the complete subset space in dimensions two through six. All thirteen listed twelve-word sets are directly checked for unique nonempty signatures. These exact finite computations were replayed directly from the embedded package sources, without floating-point solvers.

Limitations: exact computations only certify the explicitly stated finite dimensions, and they do not establish historical priority. The included checkers constitute mathematical reproducibility evidence, not independent external expert verification.
