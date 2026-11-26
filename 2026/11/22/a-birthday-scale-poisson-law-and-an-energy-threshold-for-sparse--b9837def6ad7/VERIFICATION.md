---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Taking logs of the factorial likelihood ratio gives the stated deterministic correction; its difference from lambda_n is O(n^3/K^2). Uniform approximation by continuous-density cell averages gives K s_2 -> integral f^2, and boundedness gives s_h=O(K^(1-h)). For occupancy b at most 2 the log numerator is exactly log(2) times the pair count; for b>=3 the discrepancy is bounded by a constant times binom(b,3) and the expected triple count is O(lambda_n n/K). At the critical scale the disjoint ordered pairs have count (n)_{2r}/2^r; every overlapping factorial-moment graph has v>=2c+1 and contributes O(n^(2c-v)), so the factorial moments converge to those of the moment-determinate Poisson law. When lambda_n grows, independence of disjoint pairs and the joint probability s_3 for two pairs sharing one index give the displayed variance (three unordered pair-pairs on each index triple); this is o(lambda_n^2). When lambda_n tends to zero use Markov on the pair count. Integrating the cosine cell-wise gives the sinc-squared attenuation of the cosine amplitude; the grid mean of the cosine is zero and of its square is 1/2 for d>=3 (not d=2), yielding the exact stated energy and cutoff. A separately written bounded test passed 1808 checks of the finite likelihood-ratio identity, unit null mean, pair moments and grid energy; these do not establish any limiting assertions. The null transfer is via Henzi–Law's Proposition 1(iii), while the alternative, unscaled cutoff equality, and any grid-changing sequential interpretation are explicitly delimited in the frozen theorem.

## originality

PASS

Best of knowledge for the combined terminal sparse-grid statement, particularly the sign change in actual log evidence across a nonuniform energy boundary in the many-collision regime. The finite statistic, the underlying birthday scale, and Poisson collision approximation per se are not novel. The null birthday-scale transformation is especially close to a standard deduction and is not the only basis of this assessment.

## value

PASS

Identifies a non-Gaussian terminal calibration exactly where collision noise first survives. More importantly, it quantifies a real grid-resolution failure mode for this particular evidence functional: even positive analytic dependent oracle copulas can yield vanishing terminal evidence, with the precise energy at which that reverses. This is useful for comparing evidence procedures and interpreting a fine grid, without making power claims about empirical sequential ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
