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

# Exact reproducibility

Execute `python3 verify.py` from the same directory. Standard Python is sufficient. The program calculates every four-by-four maximal minor of each generator matrix using the 24-permutation determinant formula and takes its absolute value. It builds multivariate coefficient dictionaries rather than fitting polynomials to sampled values. Its checks cover all four underlying volume formulas, 22 nonzero monomials of the full defect, the sharp two-block specialization, 81 exact rational two-block trials, and seven additional anisotropic trials. Result from the packaged script: `PASS 103 assertion groups 22 nonzero four-variable defect monomials`.

# Mathematical completeness and limits

Exhaustive maximal-minor enumeration supplies an exact, finite coefficient certificate for a polynomial identity valid on the entire nonnegative real parameter domain; the validity of the zonotope volume formula is a standard geometric identity. The sign classification then follows symbolically by a single strictly increasing quadratic in the nonnegative second block parameter and a monotone rational threshold. Numerical or finite-grid trials do not establish the continuum result on their own. The source's unthickened volume quadruple is independently reproduced. The arXiv source and the closest accessible findings were compared by definitions and implications, but independent mathematical and historical-priority audits have not been performed.
