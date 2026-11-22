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

# Verification and reproducibility

This package contains two complete standalone finite regressions:

- `verify_linear.py`: execute `python3 verify_linear.py`. It performs exact row-reduced binary Gaussian elimination over the actual Cartesian-torus four-neighbor adjacency matrix for all 196 pairs with \(3\le m,n\le16\); checks forced translation-complement for particular solutions and invariance for all homogeneous basis vectors, and verifies constructive witnesses. Expected final line: `PASS: sizes 3..16 x 3..16: 196 solvable mixed: 80 both fourfold: 16 none: 100`.
- `verify_bruteforce.cpp`: compile `g++ -O3 -std=c++17 verify_bruteforce.cpp -o verify_bruteforce` then run `./verify_bruteforce`. It independently exhausts all vertex subsets using Gray-code syndrome updates for eight explicitly listed small torus sizes. Expected minima: infeasible at \((3,3),(3,5)\); 6 at \((3,4)\); 4 at \((4,4)\); 10 at \((4,5),(5,4)\); and 12 at \((4,6),(6,4)\).

The finite regressions verify small cases and the algebraic witness constructions; they do not establish the theorem for infinitely many parameter pairs. The independent-of-computation proof is in `RESULT.md`. The public scholarly audit remains unperformed.
