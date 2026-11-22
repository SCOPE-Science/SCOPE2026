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

# Verification record

The mathematical proof is given in `RESULT.md`. Its four critical inputs are: \(n\lambda_n\to\infty\); relative concentration of all cells below \(r\); the binomial rare-cell limit \(N_{n,r}\Rightarrow\operatorname{Pois}(c/r!)\); and a union bound removing **all** cells above \(r\) with probability tending to one. The ratio for the fitted mean is separately controlled. The resulting limit uses the exact infinite unseen-cell tail, not a numerical truncation.

Run `python verify.py` with a standard Python 3 installation. The packaged script was executed and passed 367 checks, including exact finite-histogram expressions and binomial-to-Poisson approximations. These checks supplement the written analytic proof; they are not an infinite-problem certificate. The research comparison covers the original arXiv work, the linked earlier thesis, the later journal record, a related Poisson-testing review, and relevant different-statistic Stein–Chen work. No external independent audit has been performed.
