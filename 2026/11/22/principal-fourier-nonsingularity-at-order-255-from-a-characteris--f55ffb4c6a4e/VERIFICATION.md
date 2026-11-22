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

# Reproducibility and limits

The complete finite-characteristic calculation consists of exactly \(32767\) nonempty principal determinants for each of the two primitive-root Frobenius orbits. No random sampling, floating-point operation, outside database, or unresolved computational subtask is used by the included checkers.

Compile `verify_255.cpp` with `g++ -std=c++17 -O3 -Wall -Wextra -pedantic verify_255.cpp -o verify_255` and run `./verify_255`. Expected: two `PASS` lines, corresponding to root exponents 1 and 7, each reporting all 32767 nonzero determinants and the fifteen cardinality counts. Compile `verify_255_gauss.cpp` with the analogous command and run; expected: `bad=0` for both exponents and `GAUSSIAN_OK`.

The first checker uses division-free Laplace subset recursion; the second uses exact finite-field Gaussian elimination and inverses. Both were compiled and executed from the included source code, with the reported results. All primitive roots are covered because characteristic-17 Frobenius has two orbits on the eight units modulo fifteen.

The order-255 nonvanishing is established by applying Theorem 1.4 of Caragea–Lee–Malikiosis–Pfander, arXiv:2505.24326, to the certified characteristic-17 premise. Neither checker attempts direct determinant enumeration at order 255. Independent mathematical audit has not yet been performed.
