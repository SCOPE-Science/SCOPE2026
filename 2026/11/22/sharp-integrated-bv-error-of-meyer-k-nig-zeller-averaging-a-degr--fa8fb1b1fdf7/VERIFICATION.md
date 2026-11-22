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

The finite verification is reproducible with `python checker.py`, requiring only the Python standard library. The script evaluates 326 exact rational endpoint candidates for degrees one through seven, compares against their respective boundary values, and checks the degree-eight strict interior candidate. A second exact calculation integrates the negative-binomial response polynomials directly for 25 small examples and compares with the Beta-absolute-moment formula; these are mathematically distinct evaluation paths.

For all higher degrees, the proof relies on the algebraic monotonicity comparison of \(q(x)=(x/(x+3))^{x+2}\) and a decreasing rational function, not on finite checking. The asymptotic coefficient and jump localization rely on the gamma-ratio central limit theorem, the delta method, the exact Beta variance bound, and uniqueness of a scalar maximizer. The program does not independently certify these infinite arguments. All arithmetic for the finite boundary test uses Python `Fraction` and integer binomial coefficients.

The operator samples point values; the theorem is stated for canonical right-continuous \(BV\) functions with no endpoint jumps. Extending the theorem to arbitrary \(L^1\) equivalence-class representatives or modified/integrated versions of the operator has not been proved.
