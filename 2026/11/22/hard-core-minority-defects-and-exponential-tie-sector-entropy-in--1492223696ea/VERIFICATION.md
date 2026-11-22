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

The executable `check_equilibria.cpp` uses direct neighbour counts, independently of the proof's reduced formula, to compare the purported structural characterization with the actual fixed-point predicate at every three-opinion word in the target histogram sector on rings of lengths 5 through 16. It also checks every admissible minority count and the exact labelled formula. The captured output is `check_equilibria.out`.

The independently written exact-arithmetic `check_transfer.py` compares the three-by-three transfer trace against a cyclic-spacing binomial enumerator for two sign parameters and lengths 5 through 90, and verifies the closed parity-filtered formula over the same lengths. The captured output is `check_transfer.out`.

Compilation and replay instructions:

```
g++ -O3 -std=c++17 check_equilibria.cpp -o check_equilibria
./check_equilibria
python3 check_transfer.py
```

These are finite numerical checks only. The all-length correctness justification appears in the proof, which handles low-population boundary cases and the tie rule explicitly. Asymptotic error estimates are from the roots of the displayed characteristic polynomials, not numerical extrapolation.
