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

The exact finite certificate is reproducible with `python3 check.py` and `python3 check_independent.py` (standard Python library only). The first program generates the coefficient vectors iteratively by integer convolution, compares against direct assignment enumeration at \(k=1,2,3\), then checks log-concavity and unimodality for each \(1\le k\le103\). The second independently computes coefficients by \(\sum_j\binom{k}{j}\binom{2(k-j)}{r-3j}\), checking all same indices and central values.

`check_output.txt` contains the full central coefficients, their exact positive difference, the finite profile-hash summary and `VERIFY_OK`; `binomial_output.txt` records independent agreement and `BINOMIAL_VERIFY_OK`. The finite cutoff is a complete range computation, not Monte Carlo. The generating function and eventual nonunimodality use mathematical proofs in `RESULT.md`; numerical checks do not certify an infinite statement. No external independent audit is claimed.
