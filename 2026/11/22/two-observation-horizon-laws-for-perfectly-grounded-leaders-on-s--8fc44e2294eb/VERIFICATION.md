---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Every exact-budget leader set is leaf-only or hub-containing, and permutations of leaves are transitive on each type. The original-degree follower block is I_(m−k+1) when the hub is pinned. When k<m leaves only are pinned, the leaf zero-sum space has dimension m−k−1 and eigenvalue 1. On the hub and normalized constant-leaf vector the block is [[m,−√(m−k)],[−√(m−k),1]], of trace m+1 and determinant k; its polynomial is negative at 1 and roots satisfy 0<λ_-<1<λ_+. If k=m the spectra instead are {m} versus {1}, giving strict leaf-only wins. Symmetry makes the squared propagator norm exactly tr exp(−2TL_FF), and integrating gives the covariance trace for unit Brownian forcing and zero initial state. Subtracting the common unit modes and multiplying by exp(2T) yields exp(2αT)+exp(−2βT)−2, with derivative at zero 2(1−m), strict convexity, and divergence to +infinity; thus one positive root with the asserted type switch. The integrated difference starts at zero, decreases to T_Q, then increases to (m+1−2k)/(2k) via the sum and product of λ_±. It crosses once after T_Q exactly when that limit is positive; in the equality case it stays strictly below zero at every finite horizon. At fixed k the two nonunit eigenvalues tend to 0 and +infinity. Uniform convergence of the sign comparisons on compact intervals away from zero lets one bracket the unique positive roots on both sides of log(2)/2 and of the positive root of T−1+exp(−2T)=0, giving τ_0/2. The final persistent discrepancy applies to the overlap 2k≥m+1 and k<m, with k=m handled separately as in the Finding. Section 4 of python /workspace/review_reproduction.py checks exact small grounded blocks, the equality boundary and the stated finite examples; this does not establish the full all-budget result on its own. The proof assumes unit spokes and isotropic forcing and does not transfer to general weighted stars.

## originality

PASS

The steady-state star threshold is a specialization of the weighted-star result and is not original here. The supported distinct claim is the exact pair of finite-horizon placement laws for all unit-star budgets, their strict discrepancy including finite horizons at a stationary tie, and the two fixed-budget limiting times. Closely matching objective families elsewhere use different graph spectra or a different error functional.

## value

PASS

The two exact criteria are the response to initial isotropic errors and to accumulating isotropic noise. Their optimization is different even on a canonical symmetric network. The law specifies both thresholds when both exist, and explains exactly when the leaf-only covariance choice persists despite eventual hub preference for the instantaneous criterion, including at a stationary tie. The fixed-budget limits make the distinction quantitative and robust. This is an exact unit-star classification, not a general prescription for stochastic networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
