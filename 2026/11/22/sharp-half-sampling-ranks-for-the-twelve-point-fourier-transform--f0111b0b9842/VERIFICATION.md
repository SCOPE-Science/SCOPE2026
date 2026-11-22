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

# Reproduction and evidence

Compile `verify_rank12.cpp` with `c++ -O2 -std=c++17 verify_rank12.cpp -o verify_rank12`; run `./verify_rank12 rank_orbits.csv` and `python3 verify_period12.py` in the directory containing the three files. The first program enumerates the 80 translation classes of six-element subsets of the twelve-cycle, checks modular primitivity, and produces an exact 6,400-pair rank table. The second independently enumerates the classes and checks every representative pair using different modular Gaussian elimination, verifies all weights and derives the period-equality condition without matrices.

The recorded executions returned `VERIFY_OK` and `PERIOD_AND_ORBIT_VERIFY_OK`; exact integer histogram `3:76, 4:5376, 5:150564, 6:697760` sums to `853776`. The supplied `rank_orbits.csv`, `check_cpp.txt` and `check_python.txt` preserve the data and observed output. This is a finite exhaustive calculation with a rigorously justified lift from two finite fields to complex rank via the cyclotomic integer norm bound; it is not a floating-point rank experiment. The general rank inequality and saturation iff statement have an explicit noncomputational proof in `RESULT.md`.

Only the mathematical statements and recorded computations were reviewed in this package. No separate independent mathematical audit is represented, and the result makes no claim about arbitrary order-twelve minors of other sizes, condition numbers, or full spectra in other groups.
