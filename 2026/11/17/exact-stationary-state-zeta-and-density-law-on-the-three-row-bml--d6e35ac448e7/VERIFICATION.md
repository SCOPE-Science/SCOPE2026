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

# Reproduction and scope

Run `python verify_transfer.py` with SymPy 1.14 to reconstruct the full 18-by-18 transfer matrix directly from the two local blocking rules, compute the complete symbolic bivariate determinant, check the integer characteristic polynomial, and reproduce the exact trace values for physical circumferences 3 through 9. The program additionally checks the two weighted determinant derivatives that produce the limiting stationary occupation densities.

Build and execute `g++ -O3 -std=c++17 verify_bruteforce.cpp -o verify_bruteforce && ./verify_bruteforce`. This independently simulates both original traffic substeps on **every** three-state input at widths 3, 4 and 5; its totals agree with the transfer traces. The stored `transfer_output.txt` and `bruteforce_output.txt` are outputs of those exact scripts.

The transfer reduction proves correctness for every width; finite exhaustive simulation by itself proves nothing about larger widths. Numerical root approximations supplement, but do not establish, the strict Rouché/Cauchy spectral-gap argument in `RESULT.md`. The expectation limit follows from an isolated simple leading spectral root and the exact displayed derivatives. No proof is claimed about recurrent-but-nonstationary configurations, transient attraction basins or phase transitions. The publication-priority review is not independently certified.
