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

# Reproduction

From this directory, with Python 3.9 or newer, run the following two independent exact checks:

```sh
python verification/smith_census.py
python verification/modular_census.py
```

The first script requires `sympy` (the integer Smith algorithm); the second requires only the Python standard library. In the completed check, the first printed all fifteen Smith classes, totals \(6435\), and `PASS: 6435 balanced cuts, 15 integral classes; unique three-factor cut`. The second independently constructed the eight-point/eight-triple Levi graph, checked an explicit graph isomorphism with \(\mathrm{GP}(8,3)\), enumerated all complement representatives, and printed the four exact rank histograms for primes two, three, five and seven, ending with `PASS: independent 6435-cut modular census; unique point/line qutrit triple drop`.

Both tests are exact, not floating point. Smith factors determine ranks for *every* prime, so the modular tests are corroborating checks, not the basis for an invalid all-prime extrapolation. No entire-state vector of dimension \(p^{16}\) is constructed. The quantum-spectrum argument in `RESULT.md` is independent of these enumerations and uses character orthogonality.

Limitations: no composite dimension, disorder, noise, nonuniform gate weights, or other graph orders. Independent audit is not performed.
