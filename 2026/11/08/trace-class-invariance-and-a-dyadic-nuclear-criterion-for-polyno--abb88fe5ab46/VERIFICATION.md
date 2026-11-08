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

The operator is represented in a normalized monomial basis by a factorable lower triangular matrix. Exact nuclear-norm necessity uses the contractive Fourier projections extracting the block diagonal and nearest-subdiagonal. Nuclear-norm sufficiency sums the entire earlier-column rectangle for each dyadic output block. Polynomial column weights are geometrically summable precisely in the stated parameter range, and finite block similarities compare the exponents.

Run `python3 verify.py` with Python 3 standard library; the program reports `POLYNOMIAL_RHALY_BLOCK_CHECK_OK 41248 finite assertions`. Checks cover finite block factorization, adjacent and accumulated rank-one energies, weight comparisons and the divergent endpoint witness scaling. No numerical test certifies the infinite trace-class claim; the analytic argument is essential. The endpoint example establishes only failure of cross-weight invariance at exponent one, not a full endpoint classification.

The public primary source's main theorem statements were compared, but its later proof sections and some older full texts could not be completely inspected. Independent mathematical and priority audits were not performed.
