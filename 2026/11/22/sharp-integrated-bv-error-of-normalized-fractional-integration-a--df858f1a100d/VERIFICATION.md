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

The canonical representative is exactly a constant plus the integral of right-continuous unit jumps against a finite signed measure. Constants cancel; the step residual is 1_{x>s}[1−(1−s/x)^α] a.e. Tonelli against the total variation gives the upper bound by the maximum step-response integral h, and atoms attain their response. Integrating by parts gives h'=−1+α∫_0^{1−s}u^{α−1}/(1−u)du and h''=−α(1−s)^{α−1}/s; the signs at the two ends show a unique interior maximum. Equality requires all total variation at that point, and stationarity gives the claimed norm. At α=1 the step response is s log(1/s). For small α, splitting the integral gives 1+α log((1−s)/s)+o(α) at fixed s, bracketing the root at 1/2 and giving C/α→log 2. For large α let q=αs. For y≤α/2, the logarithm of the ratio of (1−y/α)^(α−1) to e^(−y) is at most y/α and has absolute size O((y+y²)/α); thus the ratio differs from one by O((y+y²)/α). Exponential tails beyond α/2 and exponential moments give relative O((q+1)²/α) for q comparable to log α. Bracketing at (1±ε)log α locates the root there. Two integrations by parts for E1 yield q+log q=log α+O(1/q) and αe^(−q)=q+1+O(1/q), proving both stated W estimates. Replay: RESULT.md §§Proof, lines 31–85. The frozen checker was inspected only; no finite tests are relied on for all-order or equality claims.

## originality

PASS

The supported distinct result is the all-real-order sharp identity defect and the order-dependent extremizers/asymptotics for the normalized fractional power kernel. The α=1 Hardy subcase and the generic step-kernel norm reduction are not separate novelty claims.

## value

PASS

Normalized fractional integration is a natural positive approximation to identity on jump data; the sharp error and unique worst jump are useful for comparing orders without a smoothness assumption. The migration from midpoint to a Lambert-scaled initial boundary layer and the +1 deficit term are nontrivial quantitative information, not merely a relabeling of the Hardy case or general column-norm principle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
