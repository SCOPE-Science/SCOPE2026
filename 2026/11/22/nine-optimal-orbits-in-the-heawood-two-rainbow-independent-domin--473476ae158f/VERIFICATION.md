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
# Reproducibility and verification

`component_enumerator.py` enumerates all \(2^{14}=16384\) zero-vertex sets and all component-flip colorings, checks the exact polynomial, and enumerates all point-line automorphisms and nine weight-eight orbits. It prints `CERTIFICATE_OK` after assertions.

`direct_label_enumerator.cpp` visits all \(3^{14}=4782969\) assignments, checks every zero-neighborhood and monochromatic edge, and prints `TERNARY_CERTIFICATE_OK`. The implementations do not share enumeration logic.

Reproduce with Python 3 and a C++17 compiler from the directory containing these two source files:

```sh
python3 component_enumerator.py
c++ -std=c++17 -O2 -Wall -Wextra -pedantic direct_label_enumerator.cpp -o verify_direct
./verify_direct
```

The representative table contains one lexicographically minimal word per orbit, in the exact point-first vertex ordering defined in `RESULT.md`. Claims of completeness are limited to these finite exhaustive loops, not to any infinite collection of incidence graphs. No third-party scientific audit has been conducted.
