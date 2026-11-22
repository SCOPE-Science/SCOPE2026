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

Run `python check_landweber.py` with Python 3 and NumPy. The script checks the Householder orthogonality and singular values, exact formula against independently iterated Landweber matrices for small instances, positive covariance normalization, multi-scale approach to independent Gaussian scores, vanishing standardized bias envelopes and a fixed-seed Gaussian simulation. The final printed assertion count and empirical coverage are diagnostic, not substitutes for the proof.

The analytic argument bounds earlier-index modal contamination by \(q^{-(j-i)}/(1-e^{-1})\) and later-index contamination by \(q^{-3(i-j)}/(1-e^{-1})\), then applies continuity of the joint Gaussian law. Since the selected null event is exactly the intersection of the fixed-index null events, it converges to \((1-\alpha)^r\). Each component interval obeys its usual fixed-index source-class bias plus Gaussian quantile coverage. The conclusion is for a specified first-exclusion rule and does not address independent-of-data stopping or general selective inference procedures.

Independent audit has not been performed.
