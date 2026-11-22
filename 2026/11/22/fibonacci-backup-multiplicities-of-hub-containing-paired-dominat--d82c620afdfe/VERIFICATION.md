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
# Verification of wheel paired-domination backup multiplicities

The source programs `verify_redundancy.py` and `verify_redundancy.cpp` were freshly run, using the current accompanying source files rather than stale or unrelated package paths. The Python verifier constructs all wheel edges and independently enumerates all nonempty vertex masks for rim sizes 3–15, tests domination, counts *every* induced perfect matching recursively, and compares the exact bivariate cardinality–multiplicity census with positive-run composition counts. The C++ verifier independently uses adjacency bitsets and a matching-subset dynamic program for orders 3–16, checking the formulas for the number of hub-containing paired-dominating vertex subsets, the number admitting a unique matching, and the total number of perfect matching witnesses.

Recorded successful output is in `verification_output.txt`; both source files are included and can be run independently (Python 3; C++17). Mathematical steps requiring proof beyond finite checks—the unique odd component, multiplicities, exceptional full wheel, formal generating-function formula, and all-order Fibonacci bijection—are in `RESULT.md`. No Lean run or independent mathematical audit is claimed.
