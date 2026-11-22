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
# Reproduction and evidence

Run `python CHECK.py` with Python 3 and its standard library, from the directory containing the extracted file. On this package the checker printed:

`PASS: 196 exact polynomial identities; 91 Chebyshev root/velocity comparisons; 112 numerical exterior roots; 36 first-order velocity comparisons`

The 196 integer identities check the cubic numerator formula, derivative recurrences and reciprocal coefficients for \(2\le N\le50\). The Chebyshev tests numerically bracket the real zeros of \(U_N'\) and check the corresponding unit-circle roots and derivative-ratio formulas; the other checks test small dimensions and fixed interior parameters. These are independent computational consistency checks, not an exhaustive search over all integers or real parameters.

The infinite claims are proved by exact polynomial algebra, simple Chebyshev derivative roots, a no-boundary-crossing homotopy and an implicit-derivative calculation. The local kernel assertion additionally requires the compact-uniform vertex limit proved in Q. Fu, arXiv:2611.15406v1, Lemma 2.3; it is not inferred from finite computations.

Independent mathematical validation: not performed.
