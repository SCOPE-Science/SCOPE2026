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

## Reproducibility
Run `python3 checker.py` using Python 3 and the standard library. The code enumerates all pairs of finite allocations in eight small parameter cases, calculates exact rational probability weights, and tests the mixed moment identity up to total order three plus the covariance identity. It prints `PASS 168 exact identities` when all assertions hold.

## Analytic checks and limits
The key asymptotic step is the expansion of \(m_n\log Q_{i,j}\), with remainder \(O(m_n/n^2)=o(1)\), and the separate treatment of \(\tau=\infty\). The factorial moments identify a unique proper multivariate Poisson law. Their finite-size computational checks are corroborative, not substitutes for the proof. The work does not establish quantitative total-variation rates, heterogeneous-coupon extensions, or any independent validation.
