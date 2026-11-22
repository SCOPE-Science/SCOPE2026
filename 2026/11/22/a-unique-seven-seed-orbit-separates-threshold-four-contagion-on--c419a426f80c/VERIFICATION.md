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

# Reproduction and limits

The two standalone files `check_direct.cpp` and `check_core.py` are included in the package. A C++17 compiler and Python 3 are sufficient. Run:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_direct.cpp -o direct
./direct
python3 check_core.py
```

The C++ checker explicitly visits all \(2^{16}=65,536\) initial sets on each six-regular graph and applies synchronous four-neighbor infection. The Python checker instead deletes all residual vertices with degree at most two in each parallel round. Both calculate the full successful-cardinality histogram, test inclusion-minimality via every one-vertex deletion, and check the exact minimal-set completion-time table. Both also enumerate all seven-vertex induced degree signatures; Python verifies the \(64\)-set affine orbit using all twelve difference-preserving linear matrices and sixteen translations.

Expected key data: Shrikhande minimal sets by \((\text{size},\text{rounds})\): \((6,3):96\), \((6,4):336\), \((6,5):1152\), \((6,6):576\), \((7,3):64\); rook \((6,3):288\), \((6,5):576\). These are *complete* finite-domain enumerations, not extrapolations. The proof of the infection-to-core-peeling equivalence and of the minimality test is in `RESULT.md`. Results are not generalized to other graphs or thresholds. No independent audit has been undertaken.
