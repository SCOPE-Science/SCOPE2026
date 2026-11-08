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

# Reproducibility and checks

Run `python3 verify.py` with a standard Python 3 interpreter; the program needs no external packages, remote data, or other files. It constructs the substitution independently of the digit-parity formula, compares all \(3^{11}\) first letters, computes signed block-prefix extrema for \(0\le k\le8\), and checks the exact Abelian-complexity values \(2k+2\) at \(3^k\) for \(0\le k\le7\) using a prefix of length \(3^{11}\). It also tests the upper signed-weight bound for all lengths through \(300\), and prints `VERIFY_OK` when every assertion passes.

These finite checks are consistency evidence, not exhaustive verification of infinitely many factor lengths. The infinite theorem depends instead on the exact prefix recurrence, the two-supertiles lemma, complement closure and sliding-window interpolation proved in `RESULT.md`. No independent audit has been performed.
