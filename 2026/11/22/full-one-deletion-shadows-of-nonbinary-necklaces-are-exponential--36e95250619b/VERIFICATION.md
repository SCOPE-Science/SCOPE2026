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

## Reproducible checks
Compile `verification/verify.cpp` using `c++ -std=c++17 -O2 verification/verify.cpp -o verify` and execute `./verify` from the package root. Compare the resulting exact output with `verification/output.txt`.

The checker enumerates every source word for ternary lengths 3–12 and quaternary lengths 3–7 and compares canonical circular one-deletion outputs. It also checks the explicit maximal construction at lengths 3–256 and enumerates the abstract deletion-alignment permutations at lengths 3–30, verifying that any alignment with too many permutation cycles forces equal cyclic neighbors.

These computations do not test infinitely many words, establish mathematical originality, determine the optimal exponential rate, or constitute an independent audit. The all-length argument is given in `RESULT.md`.
