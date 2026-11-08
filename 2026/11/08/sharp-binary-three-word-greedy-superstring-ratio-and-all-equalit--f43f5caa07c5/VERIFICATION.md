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

`verify.py` and `verify_independent.cpp` are standalone source files. Their algorithms use no external datasets, packages, network connections, or random inputs. The full finite observation is supplied in `census.csv`.

The Python executable independently computes the worst legal greedy outcome by recursive merges of actual strings and by a path-endpoint recursion. It computes optimal superstring length by a maximum-overlap Hamilton-path dynamic program and checks every answer independently against all permutations of the original words. The C++17 executable independently reconstructs the direct greedy recursion and permutation optimum from scratch.

In actual checks, the Python program reported `BINARY_3MER_GREEDY_VERIFY_OK masks=255 ratio=10/7 maximizers=4`; the C++ program reported `BINARY_3MER_INDEPENDENT_CPP_OK masks=255 maximizers=4`. The \(255\) complete rows from both implementations were compared and were identical. The four equality masks are \(31,87,234,248\); explicit witnesses for mask \(31\) were validated step by step.

The computer-assisted upper bound is limited to three-letter binary input sets, not all alphabets or lengths. This is a self-review only; no independent mathematical audit was performed.
