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

# Reproducibility and scientific verification

The analytic proof starts with the explicitly normalized weighted Bergman monomial basis and computes the two opposite one-step Toeplitz actions. The resulting self-commutator is an exact two-step band matrix, not a finite-dimensional truncation. Its diagonal quantities satisfy the exact positive rational identity for \(3A_n+B_n\); the off-diagonal estimate \(C_n+C_{n-2}<2A_n\) yields nonnegativity of the quadratic form for every finitely supported vector at \(|a|\ge3|b|\), then boundedness extends it to all vectors. For \(|a|<3|b|\), asymptotic coefficients \((1,-3,1)\), phase-alternating support and an arbitrary sufficiently large block yield an explicit negative quadratic form.

From a directory containing `CHECK.py`, run `python3 CHECK.py` with Python 3 and the standard library. A successful invocation reports `PASS: 22332 supplementary checks; analytical proof required for universal quantifiers`. Its rational identities, band forms, and finite negative witnesses support computation integrity but cannot by themselves decide all Bergman parameters, coefficient phases or unbounded support lengths. No external proof assistant or expert audit was used.

The full theorem is restricted to the specified two-term polynomial, analytic power-weighted Bergman disks with \(\alpha>-1\), and bounded Toeplitz operators. It does not imply subnormality, arbitrary Toeplitz hyponormality, or established historical priority beyond the named comparisons. Independent audit remains unperformed.
