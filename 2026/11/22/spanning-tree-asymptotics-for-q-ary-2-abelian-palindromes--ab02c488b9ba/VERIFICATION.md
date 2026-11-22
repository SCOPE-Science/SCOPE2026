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

# Reproduction and limitations

Run `python verify_exhaustive.py` to compare direct opposite-bigram multiplicities against the independent cotree condition for all words up to the listed test lengths, with an exact ternary binomial cross-check. Run `python verify_transfer.py` to count longer cases by dynamic programming on signed cotree currents, and compare the normalized counts to the derived constants. Both checks passed in the reviewed package.

A separate exact symbolic check of the fundamental-cycle Gram determinant for alphabet sizes three through seven gave \(q^{q-2}\); a Hermitian numerical eigenvalue check for sizes three through six agreed with the predicted quadratic expansion. These checks are reproducibility aids, not universal computational certificates. The proof's all-length scope is provided analytically in `RESULT.md`. Historical priority is qualified by the inaccessible 2014 full paper and incomplete access to the 2018 article.
