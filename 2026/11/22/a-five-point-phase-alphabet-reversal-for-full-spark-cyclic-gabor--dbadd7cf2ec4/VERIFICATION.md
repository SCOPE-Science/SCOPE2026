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

# Verification scope and reproducibility

The five-by-twenty-five Gabor matrix uses columns \(5x+y\) and coefficients \(\omega^{yt}g(t-x)\); no floating-point singularity decisions are made. The exact finite-field checker verifies both primes, their primitive sixty-th roots, and the strict norm-product inequality \(p_1p_2>5^{20}\). It enumerates every normalized word and every increasing five-column combination until the first exact singular witness; counts are checked for all phase alphabets of orders one through five.

Compile `g++ -O2 -std=c++17 artifacts/gabor_phase_census.cpp -o census` and run `./census reproduced.tsv`. The expected console output is embedded verbatim in `artifacts/census.out`; `cmp reproduced.tsv artifacts/witnesses.tsv` checks all 709 singular-window witnesses. In a separate implementation, compile `g++ -O3 -std=c++17 artifacts/symbolic_cyclotomic_check.cpp -o symbolic` and run `./symbolic`; compare against `artifacts/symbolic.out`. This second program uses exact signed 120-term determinant expansions and \(\Phi_5\), not the finite-field arithmetic of the main checker.

Verified outcomes: \(q=1,2,3,4,5\) respectively have \(0,5,60,205,0\) full-spark normalized windows; the independent integer implementation confirms \(5\) for binary phases and \(0\) for fifth-root phases. These are finite exhaustive computational proofs with stated exact bounds, not experimental evidence of an infinite-dimensional or all-prime phenomenon. No independent external audit has been performed.
