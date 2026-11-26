---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At draw j the mass is 4j. The signed reinforcement factor is -2 or 4, with mean 4a and squared mean v=E[R²], where a=1/2−τ/log N and v=12−8τ/log N. Subtracting a U_{j-1}/j from each increment gives bounded martingale differences with conditional variance v−a² U_{j-1}²/j². The exact moment recurrence is m_j=(1+2a/j)m_{j-1}+v with m_0=0. Its product solution yields m_k≲_τ k(1+log k) for k≤N, since the propagation kernel from j to k is (k/j)^{2a}(1+O_τ(1/j)) and (k/j)^{2a-1} is bounded by exp(2|τ|). Dividing U_k by the product A_k=∏_{j≤k}(1+a/j) gives a martingale; A_j=j^a/Γ(1+a)(1+O_τ(1/j)) uniformly. On k=⌊N^t⌋ with martingale scaled by 1/√log N, the expected total random bracket correction is O_τ(1/log N) by the moment bound and a bounded away from 0. The deterministic bracket converges uniformly by harmonic Riemann sums to 12Γ(3/2)²∫_0^t exp(2τs)ds. The bounded jumps vanish uniformly and the initial one-draw value vanishes in L². The martingale FCLT applies. Away from t=0 the prefactor A_k/√k converges uniformly to exp(-τt)/Γ(3/2); on [0,ε] it is bounded and Doob's inequality gives E sup |X_N|²≲_τ ε+o(1). Consequently replacing the prefactor by its continuous limit is valid in probability in the supremum norm over the entire interval, proving J₁ convergence and the covariance. Applying the same harmonic sum to the exact recurrence gives m_N/(N log N)→12∫_0^1 exp(-2τ(1-s))ds. The factor 1/64 in the proportion variance is from Z_N−1/2=U_N/[8(N+1)]. With τ=0, dividing the recurrence by k+1 and telescoping gives 12(k+1)(H_{k+1}−1).

## originality

FAIL

The window is covered at the statement level by a distinct indexed theorem for general fixed-increment mixed urns, under an exact specialization. That record also supplies the exact second-moment recurrence in the window, leaving the terminal moment profile and critical harmonic identity as direct evaluations rather than a supported independent remainder. Its catalogue path is later than the assigned path; this is demonstrable existing coverage, not a determination that the more general record historically preceded or was independent of this one. The fixed-mixture papers by themselves would not justify this failure.

## value

PASS

For the mixed-urn problem itself, a whole-path logarithmic-scale crossover is a mathematically motivated result. Drift detuning on the inverse-logarithmic scale survives as a finite OU drift, changes the endpoint variance continuously across the spectral threshold, and requires row-uniform control beyond fixed-parameter CLTs. The positive scientific value of that target is separate from the finding's failure to distinguish itself from an existing broader theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
