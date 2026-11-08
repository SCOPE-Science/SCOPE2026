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

# Reproducible checks

The sources `verification/enumerate.cpp` and `verification/inverse_verify.py` were extracted from the package, compiled or run without modification, and their asserted outputs ended with `VERIFY_OK`.

- The C++ enumeration covers every permutation exactly once for each length \(2\le n\le10\), includes every possible realized ordered record, and checks the full cardinality identity.
- The Python reconstruction starts from each initial position, tries both signed increments, rejects repeated labels and out-of-bound steps, and thereby enumerates the complete inverse fibers for the maximizing records at lengths \(8,9,10\).
- The Python symmetry verification partitions all \(30\) length-eight extremal permutations into seven four-element and one two-element orbit under reversal and complementation.

No check was made for length greater than ten, no computational evidence is substituted for an all-length theorem, and no independent audit has been performed.
