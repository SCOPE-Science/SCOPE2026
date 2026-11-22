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

# Finite verification

Run `g++ -std=c++17 -O2 -Wall -Wextra checks/check_cpp.cpp -o check_cpp && ./check_cpp` and then `python3 checks/check_python.py` with the included `data/` directory alongside `checks/`. The two programs are self-contained apart from standard C++17 and Python 3 libraries.

The C++ program traverses all 65,536 white subsets for both graph encodings and independently verifies the equivalence of residual skew forcing failure and containment of a minimal skew fort; it checks the local strongly regular parameters, all forcing coefficients, all inclusion-minimal fort masks, and induced four-vertex patterns.

The Python program enumerates subsets in increasing size using a different adjacency and propagation implementation. It verifies all 34 coefficient rows in `data/FORCING_COUNTS.csv` and all 632 labeled minimal skew-fort rows in `data/MINIMAL_SKEW_FORTS.csv`, including each row's mask, size and induced degree sequence. Both scripts were executed on the versions supplied here and passed their assertions. The finite certificate is not a proof of historical novelty; no independent scholarly audit was performed.
