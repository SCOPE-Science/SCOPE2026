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

# Exact finite verification and limits

The proof is algebraic for all cycle lengths. Its only nontrivial fixed-size computation is the characteristic polynomial of the explicitly defined integer matrix of order 81. `VERIFY.py` reconstructs that matrix from the four closed-neighborhood entries for each potential new column, derives the characteristic coefficients using Newton identities and exact integer traces, and compares to the stated factored polynomial. No floating-point computation or external packages are used.

Run `python3 VERIFY.py`. This also checks all color assignments of three colors for cycle lengths 3–5 and all two-color assignments for cycle lengths 3–10. Compile `BRUTE.cpp` with `g++ -std=c++17 -O2 BRUTE.cpp -o brute` and run `./brute` for an independent graph-level brute force check using a different implementation through length 7 for three named colors and length 10 for two named colors.

The transfer-matrix trace identity and log-determinant formula extend exact finite characteristic arithmetic to every length. Exhaustive tests at small lengths alone are not asserted to prove the infinite result. The scripts prove neither publication priority nor independent mathematical certification. Literature risk and scientific limitations are in the result and review.
