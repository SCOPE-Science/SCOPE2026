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

The eligible Poisson count thins to mean λp_ω. The state-independent structural zero adds η only to the k=0 mass; every mass is positive for η<1. For k≥1, B_k=r^k exp(−θ). The mixed B_0 is below one, so B_1≥1 cannot reverse it, including at θ=log r. At θ>log r, multiplying B_0−B_1 by the positive low-state zero mass gives η(1−r exp(−θ))−(1−η)(r−1)exp(−λp_H). This has one zero, at the stated η_c, with a tie there and a strict reversal only above it. At η=0 the entire Poisson likelihood-ratio sequence is strictly increasing. For fixed positive η the same inequality is F(λ)>(r−1)(1−η)/η, with F=e^(λp_H)−r e^(λp_L), derivative p_H(e^(λp_H)−e^(λp_L))>0 for λ>0, lower zero at log r/(p_H−p_L), and F unbounded. This proves a unique decreasing crossing depth; factoring e^(λ_cp_H) and taking logs as η→0 proves the additive o(1) formula. Strict tails follow even under reversal: the common flag multiplies each positive-count tail by 1−η, and coupling by an independent extra Poisson at the higher rate gives strict inequality at every positive integer threshold. The recorded flag restores Poisson MLR on the eligible stratum, with the absent stratum uninformative when present. Positive prior odds preserve the exact-count comparison. Independently checked exact fractions including the equality case η=1/2 and the reported witness (25/28,3/4,9/4); eight 60-digit sign/root comparisons independently recovered the depth equation. Replay: python3 -B /workspace/reproductions/check.py 2; /workspace/reproductions/2.log. The universal claim uses the analytic proof, not these finite comparisons.

## originality

PASS

Bounded comparison supports the exact cutoff and depth crossover as a distinct, narrow ordering result for common-flag ZIP laws. The ZIP mass formula, Poisson MLR conditional on exposure, and the basic coupling are not independently original. The exact zero-versus-one count comparison, including its equality case and exposure-depth dependence, is the surviving claim.

## value

PASS

The result identifies exactly when a specific observable comparison (one affirmative action versus none) becomes misleading if one uses ordinary count monotonicity, even though every positive-count tail moves up. Changing guaranteed eligibility from unobserved to observed is a concrete interpretation of the comparison, and the depth boundary and its dependence on structural zeros are usable for choosing or checking such a model. The model is stylized, but the well-motivated inferential boundary is more than an isolated ZIP calculation; the generic thinning and flag-stratum observations alone would not suffice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
