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

The standalone programs in `verification/` require Python 3 standard library and a C++17 compiler. Run:

```sh
python3 verification/transfer_check.py
g++ -O3 -std=c++17 verification/direct_check.cpp -o /tmp/rule126_direct_check
/tmp/rule126_direct_check
```

The transfer checker reconstructs the full space–time graph at heights one, two, three and four, enumerates all cyclic strongly connected components, elementary cycles and common-vertex conditions, checks exact independent adjacency traces through size twelve, and derives the coefficient sequences and sharp forty-nine-site gap. The direct enumerator applies the local rule independently to each binary initial state at lengths three through twenty, compares every fixed-by-two and fixed-by-four count and prints a complete census. Its 4-step checks are applied directly to states, not to a table of prior computed periods.

Recorded outputs are supplied as `verification/transfer_output.txt` and `verification/direct_output.txt`. These computation logs should not be treated alone as a proof. The mathematical proof reduces the all-length claim to the verified finite graph and its exact elementary-cycle expansion. No result outside the stated temporal-period classes is asserted.
