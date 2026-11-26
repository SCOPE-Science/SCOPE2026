---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The merged non-reset row has a mass u/m at the reset vertex and m−1 masses p/m; the reset row has mass γ at itself and m masses p/m. Detailed balance gives stationary masses u/d and p/d respectively, and averaging the two row entropies yields the stated expression (RESULT.md lines 26–40). At fixed m the −γ log γ term beats the O_m(γ) terms at γ↓0; continuity, the endpoint values, and the positive stationary mass of rows with only m successors give the strict interior and upper-bound claims. For the large-size claim, the split into bonus B and nonnegative divergence K gives γ<e/m whenever the gain is positive. K''=(m−1)/(pu) supplies a quadratic penalty of order mγ² there, whereas the weighted bonus is at most O(γ log m/m) when m²γ≥1; hence every maximizer has x=m²γ=O(log m). In that window K has quadratic term (m−1)γ²/2 and cubic error O(m²γ³). Expanding B separately retains the singular γ log(mγ). After scaling the error is uniformly o(1), including x=0 by boundedness of x²|log x| near zero. The comparison function x(1+log m−log x)−x²/2 has curvature ≤−1, derivative zero at W(m), and value W(m)+W(m)²/2 there. The uniform error controls the value additively and the squared distance of every maximizer to W(m); uniqueness of the finite-m maximizer is not required. The frozen 126 finite checks concern row entropy and normalization, not the limiting claim; no uploaded code was run.

## originality

PASS

The exact finite clique entropy is covered by specialization of the earlier indexed regular-graph formula and does not receive a separate originality pass. The surviving claim is the optimized all-maximizer scale and optimized gain with additive o(1) in the scaled quantities. This requires a uniform localization and variational analysis not supplied by the inspected general expression or by the branch-wise regular-graph optimizer.

## value

PASS

Merging indistinguishable arrivals changes the scale, not just a finite-size correction: the observed optimal probability is smaller than the split-outcome prescription by a diverging factor, and the useful entropy increment vanishes with a quantified leading expression. Controlling every optimizer and the additive error for a canonical network family gives a substantive benchmark beyond evaluating finite row entropies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
