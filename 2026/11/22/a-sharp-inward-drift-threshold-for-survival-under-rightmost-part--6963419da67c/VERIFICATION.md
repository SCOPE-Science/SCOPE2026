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

# Verification and limitations

The full mathematical claim, hypotheses, proof, priority comparisons, and finite tests are in `RESULT.md`, `REVIEW.md`, and `check.py`. The checker was executed as `python check.py`, with NumPy and SciPy available, and printed `PASS: normal-maximum integrals, monotone critical drifts, 4 independent endpoint-skeleton Monte Carlo checks.` It directly computed \(m_2=0.564189583548\), \(m_3=0.846284375322\), and the two-particle critical drift at \(D=r=1\) as \(0.707106781187\). The seed and sample size are fixed in `check.py`.

Numerical experiments test finite cycle laws only. They neither prove the half-line absorption classification nor certify priority. The infinite-time classification relies on iid random-walk oscillation and a finite exponential moment for the within-cycle Brownian drawdown. Source-inspection coverage and the remaining possibility of unindexed equivalent results are reported in `REVIEW.md` and `AUDIT.json`.
