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

The conditional geometric lag law has normalization 1-r^t. At a cut with right endpoint t=j+1 the first lag is 1 and a birth h steps after t requires lag at most h. Independence and telescoping give b_j=[(1-r)∏_{h=1}^j(1-r^h)]^m. For the stationary K-window indicators the later cut imposes stricter bounds on every overlap, including for neighboring cuts, giving the stated pair law. A separate factorial-moment check can bypass the Poisson approximation citation: for ordered finite-start cut endpoints 0<t_1<...<t_k, set t_0=0. The strictest bound at any birth is the bound of the most recent cut. Multiplying the factors on successive blocks and the final infinite tail, the common denominators from t_1 onward telescope and give the exact joint probability ∏_{i=1}^k b_{t_i-t_{i-1}-1}. Set a_d=b_{d-1} and N=floor(H/ρ). The sum of a_d for d≤K=ceil(β^-2) is O_m(β^m), by bounding factors for h≤floor(β^-1/2) by sqrt(β) and the remaining terms by monotonicity. For d>K, a_d/ρ=1+o(1) uniformly by the geometric tail of log of the product. Therefore ∑_{d≤N}(a_d−ρ)=o(1). The total difference between any fixed-order joint factorial-moment sum on disjoint subintervals of [0,H] and the independent-site sum with probability ρ is at most k![(∑_{d≤N}a_d)^k−(Nρ)^k]=o(1), using nonnegative differences and enlarging the domain to all k-tuples of gaps in [1,N]. This yields the independent Poisson counts and vague convergence on compact sets. The void probability on [0,H] gives the first-index limit. For each fixed β the stationary i.i.d. lag process is ergodic and cuts have positive frequency; the conditional resampling coupling differs from the stationary draws at only finitely many births almost surely since ∑_t mr^t<∞. Finally the eta modular identity gives the product factor sqrt(2π/β)exp(−π²/(6β)+β/24)(1+O(exp(−4π²/β))); the extra (1−r)^m gives the printed prefactor (2πβ)^{m/2} and relative O_m(β) error.

## originality

PASS

The credible distinction is the vanishing-bias limit of the full terminal-cut process, at the specified normalization, not the model, cut criterion, or almost-sure existence. The strongest exact match in primary literature proves fixed-bias renewal, and the closely related later indexed result treats fixed-bias Gaussian fluctuations rather than the vanishing-bias Poisson law. No inspected distinct result gives or directly implies the stated scaling limit without additional rare-gap control.

## value

PASS

The result distinguishes eventual occurrence at fixed bias from the scale at which barriers first become visible as bias vanishes. The exact scale is exponentially large in reciprocal bias, and convergence of the point process controls separation and joint counts, not just a single marginal. Ruling out rare-event clustering for cuts defined by the entire future is substantive and useful for questions involving random bottleneck spacings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
