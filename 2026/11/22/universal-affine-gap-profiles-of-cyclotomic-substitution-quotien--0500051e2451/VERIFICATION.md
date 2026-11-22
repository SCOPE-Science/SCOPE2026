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

# Verification

Run `python3 verify.py` in a clean directory containing this file and `verify.py`. Only the Python standard library is required.

The checker constructs every relevant cyclotomic polynomial by exact integer monic division of \(X^n-1\), without using the periodic-block formulas. It then constructs each substitution quotient by a second integer polynomial division, independently constructs all cyclic coefficient words, and checks full coefficient equality, whole gap histograms, the affine increment, the upper bound \(\varphi(m)\), and total gap-length mass. The tested instances include composite \(t\), small and nonsquarefree \(m\), and all eight residues for \(m=15\). The explicit 64-number slope and 64-number intercept certificate for \(m=15\) is checked against two sets of data. Expected output begins `PASS: 631 independent exact-division quotient instances`.

The infinite quantifiers are proved by the algebraic periodicity, nonvanishing, boundary and truncation arguments in RESULT.md. Finite checks are arithmetic regression tests, not exhaustive verification of infinite families. No external or independent audit has been performed.
