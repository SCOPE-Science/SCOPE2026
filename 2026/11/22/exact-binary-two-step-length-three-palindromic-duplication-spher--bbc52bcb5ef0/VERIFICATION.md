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

# Reproducibility and limits

The included C++17 program `verify.cpp` performs complete binary source enumeration for all lengths \(3\le n\le22\). It uses the exact bitwise operation corresponding to substring reversal-and-insertion, generates all \((n-2)(n+1)\) histories for every complement representative, sorts outputs to compute the distinct cardinality, records global maxima and labeled maximizing counts, and tests the identified period-four optimizers. Complement reduction is justified algebraically and does not discard inequivalent sources.

Compile with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify.cpp -o verify`; run `./verify 22`. The supplied `verify_output.txt` records the completed replay, including `REFERENCE_OK words=2040 n=3..10` for the independent string-based operation and `EXHAUSTIVE_PASS complement_representatives=4194300 lengths=3..22`. A mismatch aborts with a nonzero exit status.

The exhaustive procedure **proves only the stated finite interval** under the supplied elementary equivalence of the integer encoding and the channel operation. It neither proves the same polynomial or optimizer characterization beyond length \(22\), nor verifies codebook optimality, independent review, or priority against every unavailable source.
