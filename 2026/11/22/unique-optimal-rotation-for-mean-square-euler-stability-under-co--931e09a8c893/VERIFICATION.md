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

# Reproducibility and verification

The file `verify.py` is a standalone Python 3 program requiring SymPy, NumPy and mpmath (mpmath is a standard SymPy dependency). Run `python verify.py` from the directory containing it. Its observed output is stored verbatim in `verification_output.txt`.

The program verifies exactly: (i) the return-gain rational identity against the geometric series, (ii) the rank-one feedback determinant identity for the symmetric covariance operator, (iii) the transformed timestep derivative, and (iv) the polynomial numerator of the frequency derivative. The polynomial coefficient positivity and the optimal-frequency uniqueness follow from the displayed hand proof, not from an unbounded code search. There are 104 separate finite rational-parameter cases comparing the exact inequality with the eigenvalues of the independently formed covariance matrix; these use floating-point eigensolvers only as supplementary tests. A high-precision numerical root validates the illustrative normalized-noise-3 example. No numerical sampling proves universal spectral claims, and no independent external audit has been performed.
