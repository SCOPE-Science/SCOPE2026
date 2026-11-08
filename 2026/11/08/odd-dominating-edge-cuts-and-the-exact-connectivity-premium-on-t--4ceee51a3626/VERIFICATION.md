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

Compile `verify_triangular_direct.cpp` with a C++17 compiler (for example `g++ -O2 -std=c++17 verify_triangular_direct.cpp -o direct`) and run `./direct`. The program builds the line graph directly, enumerates all \(2^{\binom n2}\) selections for each \(3\le n\le7\), checks every parity constraint, performs induced-connectivity graph traversals and compares every weight coefficient to the stated formula. It prints `DIRECT_EXHAUSTIVE_PASS` only after every comparison succeeds.

Run `python3 verify_triangular_linear.py`. This separately constructs the binary closed-neighborhood matrix, performs row elimination, reconstructs all affine solutions, checks every linear equation and connectedness, and compares ranks and full weight profiles for \(3\le n\le9\). It prints `GAUSSIAN_SOLVER_PASS` on complete success.

The included `triangular_direct_output.txt` and `triangular_linear_output.txt` are actual recorded outputs of those source files. They verify only these finite instances; the mathematical proof for every \(n\) is in `RESULT.md`. No external or independent scholarly audit was performed.
