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

The self-contained all-length proof is in `RESULT.md`. To reproduce the finite checks, run `python3 verify.py` with a Python 3 standard-library interpreter. The verifier enumerates every binary word of each relevant length from four through 23 without `11`, computes the minimizer locations directly, compares them with an independently coded structural charge classification, checks the four endpoint-refined Fibonacci identities, then compares Parry-weighted densities with the closed formula at 50-digit precision. It also checks monotonicity and pair plateaus through \(k=99\).

The test covers 196,405 admissible contexts with \(1\le k\le20\); it does not constitute an exhaustive test for infinitely many lengths, nor a separate expert review. All-length validity rests on the prefix decomposition and stationary-cylinder calculation in `RESULT.md`. The exact density is source-specific and should not be confused with uniform finite-context frequencies.
