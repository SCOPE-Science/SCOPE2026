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

The full proof is analytic: the six local coordinate transforms have Jacobian \(t^2|\log(ta)|\); their normalized densities converge in \(L^1\) by domination. The exact scalar CDF published in 2018 provides global normalization. The resulting joint marked convergence is in total variation, not merely in distribution.

`python check_marked_side_triangle.py` checks the coordinate identity and mean against 900,000 direct cube draws; checks the known CDF at three points and its small-tail expansion; and importance-samples a single corner chart with 1,100,000 proposal draws at each of three small thresholds. Expected limits are local normalized mass \(1/2\), mean logarithmic split \(1/2\), and both simplex coordinate means \(1/3\). It uses a fixed random seed. NumPy/mpmath are required. Floating-point numerical evidence is diagnostic, not a proof of convergence, nor an independent audit.

All first-public-date statements refer to the publicly dated 2015 problem formulation; the later preprint and journal versions are identified separately. Historical novelty could be affected by additional unpublished or unindexed sources.
