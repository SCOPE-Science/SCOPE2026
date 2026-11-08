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

# Reproducible checks

The package includes `verify_fgc_mv.py`, a self-contained Python standard-library verifier. Run `python3 verify_fgc_mv.py` in the directory holding the program. It creates no files, imports no third-party packages, and prints a PASS message on complete success.

For each finite Łukasiewicz chain of size \(2\le n\le10\), it exhausts all weakly increasing maps \(f\) satisfying \(f(j)\le j\). For each possible \(f\), the unique possible left adjoint \(g\) is computed as the least \(y\) satisfying \(j\le f(y)\), and all primitive Frobenius identities are checked directly on all input pairs. The surviving pairs are compared as exact sets with the divisor floor/ceiling formulas. There are \(16{,}796\) candidate maps at \(n=10\).

The observed number of pairs for \(n=2,\ldots,10\) is \(1,2,2,3,2,4,2,4,3\); all tests pass. Exhaustive small-case verification is not an independent proof for arbitrary chain size. The exact all-size proof appears in `RESULT.md`. No external review, independent audit, or formal proof certification is claimed.
