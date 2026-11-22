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

# Reproducibility and mathematical checks

The standalone sources `verify_prism_tpr.cpp` and `independent_bruteforce.cpp` require a C++17 compiler and standard library only.

Compile and run:

```sh
c++ -O2 -std=c++17 verify_prism_tpr.cpp -o verify_prism_tpr
./verify_prism_tpr
c++ -O2 -std=c++17 independent_bruteforce.cpp -o independent_bruteforce
./independent_bruteforce
```

The first executable prints `PRISM_TPR_VERIFIED_345` if all assertions pass: exactly 468 transitions, nonnegative reduced costs from shortest-path potentials, exactly two zero-cost directed cycles of lengths 3 and 6, precisely six one-cost closing transitions all of length 5 modulo 6, and the four low-cost formulas for every formal length from 1 through 345. Using the determinant-trace rationality argument given in `RESULT.md`, degree at most 333 after multiplication by the known denominator turns those 345 checks into identities for all cycle lengths.

The second executable separately enumerates ternary graph labelings for sizes 3 through 7 and returns:

```text
3 4 3
4 6 48
5 7 30
6 8 9
7 10 35
```

Each line means circumference, minimum weight, number of minimum functions. The first test is a finite exact algebraic certificate and the second is a genuine independent exhaustive check on small graphs; neither is claimed as an independent human audit.

No result is asserted for graph cycles of lengths one or two. Formal transfer coefficients at those lengths are used only in the rational-function identity. No arbitrary higher-width grids or all-weight closed polynomial are asserted.
