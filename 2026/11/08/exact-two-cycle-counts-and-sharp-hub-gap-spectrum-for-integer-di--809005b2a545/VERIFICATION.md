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

The mathematical proof is in `RESULT.md`. The following standalone source files use only standard C++17 and Python standard-library functionality. The source and captured outputs are both part of this package.

To evaluate the exact multinomial sums use `python count_formula.py`. Its output is captured in `formula_check.out`, including all values for \(n=1,\ldots,10\), positive-hub-gap counts, support, and sharp endpoint assertions for \(n\ge3\).

To check the update dynamics independently, compile with `g++ -O3 -std=c++17 direct_check.cpp -o direct_check` and run `./direct_check`. The captured result is `direct_check.out`. The program first normalizes the first hub to zero and then enumerates the *entire* theorem-proved finite domain for \(n=1,\ldots,5\): every other hub label in \([-2n-2,2n+2]\), every leaf in \([-n-1,n+1]\). It applies two full synchronous diffusion steps to each configuration and records exact gap-resolved counts. A total of 9,602,861 states is tested. Counts for signed gaps are asserted symmetric.

The first five total counts agree between the two implementations: \(9,47,299,2915,36455\). The sharp-gap support and extremal multiplicity are checked by integer formulas through \(n=10\). These are finite checks only; the proof establishes the all-size conclusion. No independent external audit, formal proof assistant check, or exhaustive test at unbounded size has been performed.
