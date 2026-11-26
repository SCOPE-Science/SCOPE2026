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

The Stieltjes representation on (0,1] includes the possible pointwise endpoint jump and has total variation equal to the input seminorm. Bernstein reproduces constants, so the L² triangle inequality bounds the norm by the supremum of single-jump errors; the unit-variation steps prove the converse. Within each cell the sampled threshold is fixed and d(E²)/dt=2F−1, an increasing function, yielding the two traces per grid point. The artificial endpoint traces (0,0) and (n,n+1) are zero, the right trace (0,1) is a limit, and (n,n) is attained. Reconstructed 270 traces exactly in the Bernstein basis (product coefficients followed by an antiderivative of degree 2n+1), replay `python /workspace/review_checks/4.py`. For n≤14 the only largest trace labels are (0,1) and (n,n), of value 1/(2n+1); for n=15 only (6,7) and (9,9) give 7885956840965217/239784545898437500, strictly above 1/31. The latter trace is the admissible step at 3/5. A separate reviewer-written replay via beta integration agreed. The frozen checker was inspected, not executed. For interior t_n→t, the binomial CLT with bounded third moments and variance comparable to n gives pointwise Φ(z) at x=t_n+sqrt(t_n(1−t_n)/n)z; Hoeffding outside the bounded scaled neighborhood gives an integrable Gaussian majorant uniformly for t_n in compact interior ranges, including shifted thresholds. Writing Q=1−Φ, integration by parts gives ∫₀∞Q²=φ(0)−2∫₀∞φ²=(sqrt(2)−1)/(2sqrt(π)). For the frozen Chebyshev justification of (7), the threshold n|x−t|−1 has to be positive, not merely its squared denominator; the splitting uses Chebyshev only there and the bound 1 in the near part. An independent check is to write F as the CDF of the jth order statistic U of n uniform variables. Jensen gives ∫(F−1_{x≥t})²≤E|U−t|. Its beta mean is m=j/(n+1), variance m(1−m)/(n+2); |m−t|≤2/n implies (7), also for the limiting traces j∈[1,n], and both omitted constant-threshold endpoints are zero. Compactness now excludes both endpoints at scale √n and maximizes sqrt(t(1−t)) uniquely at t=1/2. This proves the displayed sharp asymptotic and the location conclusion, not a finite-n optimizer classification beyond 15.

## originality

PASS

Best-of-knowledge pass for the exact pointwise-BV to integrated L² norm, finite crossover, and global sharp asymptotic with location. The binomial pointwise description, normal approximation and BV machinery are not claimed as new. The substantive prior comparison is with published pointwise estimates and continuous-input results, not with search nonappearance.

## value

PASS

The jump model and endpoint convention are intrinsic to point sampling on Jordan BV. The exact transition distinguishes the endpoint artifact from a genuine interior extremizer, and the large-degree sharp constant plus localization resolve which jump configurations govern worst squared error. The cutoff is a structural fact for a classical operator, not an arbitrary isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
