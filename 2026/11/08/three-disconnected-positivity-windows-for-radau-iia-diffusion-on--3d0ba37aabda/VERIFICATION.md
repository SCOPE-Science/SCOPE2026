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

# Verification evidence

Run `python3 verify.py` with Python 3 and the standard library. The result in this package is `VERIFY_OK 2228`.

The checker builds the star Laplacian and its orthogonal projectors over exact rational numbers for integers \(2\le m\le32\) and eleven positive rational step sizes. It checks the original completed Radau IIA matrix equation, stochastic row sums, symmetry, diagonal rational identities, strict positivity of each off-diagonal entry, and equivalence between matrix nonnegativity and the two polynomial signs. It also checks four exact formal bivariate polynomial identities and an exact univariate coefficient identity for the strictly positive \(m=10\) certificate. Exact-rational evaluations cover the threshold witness for \(2\le m\le60\).

The finite checks are **not** an exhaustive test over all integer graph sizes or real step sizes. Infinite-family correctness is established by the polynomial proof in `RESULT.md`, including the degree-two concavity argument, the discriminant, and Descartes' rule. The source comparison does not establish priority over unidentified literature.
