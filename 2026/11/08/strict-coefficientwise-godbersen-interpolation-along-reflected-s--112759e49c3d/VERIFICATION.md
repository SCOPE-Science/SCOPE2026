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

# Reproducibility checks

The theorem's critical premises are (i) the exact orthant decomposition of the simplex difference-body volume; (ii) the factorization of \(H_n\) from the simple interior zeros of Legendre polynomials; (iii) positivity and strict decrease of the factor parameters \(r_i\); and (iv) the second-moment formula for the binomial-square weights. These premises are established within `RESULT.md` except for the classical Legendre zero-location theorem, whose standard orthogonal-polynomial proof is a known input.

Run `python3 verify.py` with the Python 3 standard library. The program reconstructs the normalized reflected-volume polynomial in two independent algebraic ways: by direct binomial expansion of the simplex sum and by the reduced \(H_n\) polynomial. For dimensions 2 through 16 and six rational aperture parameters it checks these identities and the endpoint mixed-volume normalizations exactly; it also checks strict coefficient decrease along five consecutive parameter intervals at all interior indices and the exact center-derivative identity. The observed result in the present package was `PASS 1605`.

The checker is a finite exact-arithmetic diagnostic and is not an exhaustive or infinite certificate. Its values support the formulas but do not establish them outside the tested range. The preceding analytic argument handles all stated dimensions, indices and parameters. Independent audit has not been performed.
