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

# Verification

The self-contained `verify.py` enumerates all local-switch cycle covers at lengths 3 through 5, reconstructs closed incoming signatures for every graph vertex, and compares with independently enumerated prefix-class selections at lengths 2 through 4. It prints `KAUTZ_CLASSIFICATION_FINITE_OK` with counts 4, 27 and 1728 at lengths 3, 4, 5 and separately verifies the base count 2 at length 2.

The independently implemented `independent.cpp` uses integer-indexed graph vertices and 64-bit signature masks rather than the Python set-signature method. It checks the counts 4, 27, 1728 and prints `INDEPENDENT_CPP_OK`.

The construction `sampler.py` chooses exact equiprobable allowed local switches and checks minimum-cardinality identification on sampled outputs for orders 2 through 8, printing `UNIFORM_SAMPLER_CONSTRUCTION_OK`. The uniformity claim itself follows from the proof's bijection and equiprobable independent choices, rather than statistical tests.

To reproduce with installed standard Python and a C++17 compiler, run `python3 verify.py`, then `python3 sampler.py`, then `g++ -std=c++17 -O2 independent.cpp -o checker && ./checker`. These checks do not independently certify the all-order argument or historical priority.
