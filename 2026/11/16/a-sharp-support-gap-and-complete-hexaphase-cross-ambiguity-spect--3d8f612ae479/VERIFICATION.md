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

Two independent C++17 checkers (`verify_structural.cpp`, `verify_spectrum.cpp`) use exact integer arithmetic and deterministic exhaustive loops, with no external data, randomness, external packages, or floating-point equality tests.

```sh
g++ -O2 -std=c++17 -Wall -Wextra verify_structural.cpp -o verify_structural
./verify_structural
g++ -O2 -std=c++17 -Wall -Wextra verify_spectrum.cpp -o verify_spectrum
./verify_spectrum
```

The first tests all 1,679,616 normalized coefficient pairs via Eisenstein-coordinate zero sums and cyclotomic row rigidity. The second constructs all 7,776 sixth-root length-five coefficient words, directly reduces their five Fourier modes modulo the degree-eight cyclotomic polynomial \(\Phi_{30}\), and tests every shift for every pair. Each program compares its complete eight-level support and eight-profile histograms against declared integer targets; a mismatch causes a nonzero exit status. These checks were executed successfully on the delivered source files before inclusion.

The cyclotomic irreducibility, five-term zero-sum classification, derivative parity lemma and nonoverlap with the motivating equality theorem are given as human-readable mathematical steps in `RESULT.md`. This finite certificate is exhaustive for the stated phase alphabet and cyclic length only. It does not establish independent validation, other group sizes or near-zero noise robustness.
