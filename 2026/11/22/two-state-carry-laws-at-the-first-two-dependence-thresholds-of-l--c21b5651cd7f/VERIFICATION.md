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

# Verification and reproducibility

`verify_riesz_moments.py` runs with Python 3's standard library. Run `python3 verify_riesz_moments.py`. It independently expands each factor's Fourier series with exact fractions, convolves across geometric frequencies, and compares the zero coefficient against the proposed two-state matrix product. It additionally checks the strict adjacent-base inequalities for orders four through ten and specific exact fourth-moment coefficients. The observed output was `PASS: 220 independent exact assertions`.

The finite replay does not establish statements for arbitrary product length or arbitrary integer exponent. The proof in `RESULT.md` supplies the digit-carry bijection, finite state bound, transfer reduction, matrix positivity, Perron convergence, and perturbative onset constants. There are no numerical approximations in the asserted exact equalities. All variables and normalizations appear in `RESULT.md`. No independent validation is claimed.
