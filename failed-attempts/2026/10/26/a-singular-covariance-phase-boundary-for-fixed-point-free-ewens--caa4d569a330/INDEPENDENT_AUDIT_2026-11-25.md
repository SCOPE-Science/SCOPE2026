# Independent mathematical audit

## correctness

PASS

The RESULT.md theorem is correct. Marking one a-cycle and one b-cycle in the fixed-point-free exponential generating function shifts n by a+b and multiplies by θ²/(ab); subtracting the separately marked means yields the stated determinant. For α=θ−1, coefficient transfer at z=1 gives log H_n = const + α log n + A/n + B'/n² + O(n⁻³). The fixed-shift mixed difference log H_(n−a−b)+log H_n−log H_(n−a)−log H_(n−b) is −αab/n²+O(n⁻³): the analytic-factor terms do not contribute at order n⁻². Exponentiating and using H_(n−a)H_(n−b)/H_n²=1+O(n⁻¹) proves the coefficient. At θ=1, write q_m=e⁻¹+(−1)^m r_m with the positive Taylor integral remainder. With N=n−a−b≥2, r_(N+k)≤3^(−k)r_N; the sign-correct linear determinant term has magnitude at least e⁻¹(62/81)r_N, exceeding the quadratic bound (2/81)r_N². At N=0 use 1/3≤q_m≤1/2 for m≥2; at N=1 use q_1=0. For fixed lengths the shifted remainders are o(r_N), and r_N∼1/(N+1)!, giving the signed prefactor. The separate frozen REVIEW.md under Value incorrectly calls the unconditioned uniform counts independent. They are only uncorrelated under the stated length bound: at n=5 the positive-probability events C₂=2 and C₃=1 cannot coincide. This error in the commentary is not part of RESULT.md's theorem.

## originality

FAIL

The earlier, distinct 2026/10/18 Resultary record explicitly gives the same conditioned law, strict parity for exactly the stated domain, and the same signed factorial limit. These cover both purported additions at θ=1, not just the underlying covariance identity. Da Silva–Jamshidpey–Tavaré already give the conditional factorial moments. The off-critical coefficient is the standard fixed-shift second difference of their coefficient ratio and matches the unconditioned leading term; it was not found stated in the passages of that paper. No separate substantive original advance survives in the claim as written. The later catalog match is not used as evidence of earlier priority.

## value

FAIL

The strict parity and factorial scale have structural interest but are already available together in the earlier exact result. With those removed, the extra computation is a routine curvature calculation from known factorial moments and ordinary coefficient asymptotics. It gives the same leading coefficient before and after conditioning. The record does not determine the first noncritical correction attributable to conditioning or any parameter-uniform transition; no genuinely valuable distinct remainder is established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
