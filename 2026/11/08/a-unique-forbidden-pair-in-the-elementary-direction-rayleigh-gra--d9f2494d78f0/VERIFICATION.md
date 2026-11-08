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
# Verification and scope

The result has a finite universe of 45 unordered pairs selected from 10 explicitly defined integer vectors. To reproduce the coefficient certificate, place `verify.py` and `PAIR_CERTIFICATE.tsv` in the same directory as extracted from the research record and run `python3 verify.py`. Python 3 standard library suffices. The program reconstructs the four-dimensional zonotope volumes from all 4-by-4 minors at the two required anchor values of the parameter; it uses integer determinant arithmetic, not optimization or floating point. It compares each computed polynomial coefficient triple to the TSV and checks the exceptional factor, positive-coefficient conditions for all other pairs, and all boundary equality counts.

An additional symbolic-matrix determinant implementation checked all 360 volume expressions (four volumes, two anchor values, and 45 direction pairs) independently against the integer-permutation implementation. It returned `SYMPY_INDEPENDENT_CROSSCHECK_OK 360`. The certificate's actual execution returned `EXACT_PAIR_CLASSIFICATION_OK 45 pairs; 44 nonnegative; one violation for 0<t<2; eight t=0 equalities`.

Completeness is justified because the 10 chosen directions generate exactly 45 unordered distinct pairs. Affineness in the nonnegative scale parameter is an analytic consequence of the one-special-generator determinant expansion, and the continuum sign statement follows from the displayed quadratic polynomials; it is not based on sampling. General directions outside the specified ten and arbitrary-dimensional zonoids are not checked or claimed. Independent mathematical audit has not been performed.
