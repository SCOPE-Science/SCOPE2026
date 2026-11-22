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

# Verification and limitations

The all-length proof consists of a three-vertex Euler trail/circuit criterion, an exhaustive characterization of five-bin histogram feasibility, a disjoint generating-function case partition, and exact coefficient extraction. This does not depend on an external computer algebra system.

Run `python3 verify.py` in the directory containing this file. The included program uses only the Python 3 standard library and returns:

```
SPECTRUM_VERIFY_OK word_instances=118092 histogram_vectors=3478760 Euler_witnesses=12286 lengths=1..50
```

The first test constructs the actual output set from every ternary linear and cyclic word at read counts one through nine and verifies equality of sets with the mathematical feasibility classification, plus both cardinality formulas. It counts 118,092 tested source words in total. The second enumerates the complete integer-composition space of 3,478,760 five-bin histograms at read counts one through fifty, independently checking the formula counts against the finite feasibility predicates. The third constructs actual Euler walks for feasible histograms and checks that their observed outputs agree, with exhaustive histograms through length thirteen and 1,000 additional parameter cases up to length five hundred. An exact symbolic simplification of the derived series independently confirms the rational generating function and initial coefficients.

Finite tests alone do not establish the infinite theorem. The mathematical proof in RESULT.md establishes completeness of the three explicit disconnected linear types and four cyclic parity/connectivity cases for every integer read length. The theorem concerns a fixed three-symbol alphabet, noiseless and unindexed read sums. Scientific independence and external validation have not been established.
