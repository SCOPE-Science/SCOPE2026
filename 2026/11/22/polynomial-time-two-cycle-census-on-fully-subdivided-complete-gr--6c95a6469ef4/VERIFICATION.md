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

The claim is established by the four-step all-size combinatorial proof in `RESULT.md`. The following independent finite checks corroborate its base cases and arithmetic.

```sh
python3 verify_formula.py
c++ -O2 -std=c++17 verify_dynamics.cpp -o verify_dynamics
./verify_dynamics
```

`verify_formula.py` compares the closed sum to direct enumeration over all firing-bit patterns on full subdivisions of \(K_3,K_4,K_5\), and checks the reciprocal-pair sieve against direct selection maps at shore sizes through three. It also evaluates the formula through \(n=8\).

`verify_dynamics.cpp` explicitly calculates the chip-firing update and its square on all chip configurations in the degree-confined finite box for \(n=3,4\). It recognizes nonfixed two-step returns and divides their state count by two. These finite checks are logically independent from the all-size combinatorial proof and do not claim to enumerate configurations of larger graphs. The exact program outputs end with `FORMULA_AND_CUT_CHECKS_PASSED` and `DYNAMICAL_CHECKS_PASSED`.

No independent external audit has been performed. The package contains standard-library-only source code, not a compiled executable.
