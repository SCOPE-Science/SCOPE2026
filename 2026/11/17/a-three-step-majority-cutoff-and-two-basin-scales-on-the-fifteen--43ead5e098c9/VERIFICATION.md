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

# Reproducibility and verification limits

The exact finite-state computation uses a fixed lexicographic order of the fifteen unordered pairs of six labels. The public update rule is the strict open-neighborhood majority among six disjoint pairs with old-bit tie retention. The C++ checker constructs neighbor bitmasks and tests all \(32768\) states. The Python checker independently evaluates occupied named-edge sets, rebuilds their dynamics and symmetry orbits, and asserts the same complete entry-time and basin tables.

Run `g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_majority.cpp -o verify_majority && ./verify_majority` and `python3 verify_majority.py`. Outputs supplied as `verify_cpp.txt` and `verify_python.txt` were obtained by these invocations from the provided code and reviewed with the 26-orbit `classes.tsv` listing. Both enforce \(F^5=F^3\), the sharp failure of \(F^4=F^2\), the five basin classes, 502 fixed points, 2,670 two-cycles and eight plus eighteen spatial classes.

The scope is limited to this finite graph, the stated rule, and labelled configurations. A full historical-priority certification or independent external audit has not been performed.
