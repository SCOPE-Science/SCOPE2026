# Independent mathematical audit

## correctness

PASS

For any continuous common CDF, the transformed endpoints are independent uniforms and have no ties almost surely. Monotonicity then preserves all sampled strict endpoint orders even if the CDF has flat pieces. In the uniform endpoint triangle (u,v), the conditional probabilities of containing a peer and being contained in a peer are respectively (v−u)² and 2u(1−v); others are conditionally independent. Integrating these absence probabilities with density 2 and weight n proves both expectation integrals. For the first, use d=v−u, integrating (1−d²)^(n−1) with weight 2n(1−d); the two terms are n B(1/2,n) and 1. The gamma ratio then gives the stated O(n^(−1/2)) remainder. For the second, integrate in v first, symmetrize u with 1−u, and put s=1−2u on the first half. This gives ∫[1−Q(s)^n]/[1−Q(s)] ds on [0,1] with Q=(1+s²)/2. Expanding the finite series and its binomials gives the claimed sum for all n≥1. To compare with H_n split 2/(1−s²) into 1/(1−s) and 1/(1+s). Since 0≤Q−s=(1−s)²/2 and Q≤exp(−(1−s)/2), the divided power difference integrates to O(1/n); subtracting the Q^n term from the 1/(1+s) integral has O(1/n) cost as well. This proves log n+γ+log 2+O(1/n) and the ratio of expectations only. Independent enumeration of all matchings through seven arcs confirmed both exact means; at n=7 the 135135 matchings give 1619/429 and 140744/45045 respectively. Replay: /workspace/branches/1da99c1c-3c5b-494d-b3bb-bb9d14dce460/independent_matching_check.py and independent_matching_check.txt. The frozen script was inspected, not executed; finite matching tests do not verify asymptotics.

## originality

PASS

The supported distinct finding is the quantitative comparison of the two strict-containment frontiers, including the exact outer-frontier mean and its sharp constant. The inner gamma-ratio value also occurs as the mean of a different boundary statistic in a distinct same-day record. Neither a priority claim from dates nor a claim that the gamma-ratio sequence itself is new is warranted. The studied precedence law, matching depth results, and independent-coordinate Pareto results do not give the outer containment mean or the two-frontier comparison.

## value

PASS

Inner and outer irredundant containment collections are canonical summaries of the same interval sample, not arbitrarily chosen subsets. Exact distribution-free calibration of the logarithmic side, including its constant, and its comparison to the square-root side quantify very different expected summary sizes. This is useful without a claim about concentration or realized ratios; it is not just reusing the known numerical mean of a precedence frontier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
