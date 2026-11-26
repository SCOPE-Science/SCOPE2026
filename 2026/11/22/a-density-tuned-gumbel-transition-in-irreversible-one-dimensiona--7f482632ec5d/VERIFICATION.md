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

Independently reconstructed the run law, the random-prefix maximum argument, all normalizations, and the transfer to sweeps. On a ring of L >= 3 with a nonempty initial plus set, different minus runs use disjoint site clocks and cannot merge. Given length k, a run has k-1 independent rate-2 waits followed by one independent rate-1 wait, including the k=1 case. Mixing over geometric(p) lengths gives H = E + BW in law with independent E ~ Exp(1), B ~ Bernoulli(1-p), W ~ Exp(2p), so its Laplace transform is p(s+2)/[(s+1)(s+2p)]. The survival function is [p exp(-t)-(1-p) exp(-2pt)]/(2p-1) for p != 1/2 and exp(-t)(1+t/2) at equality. To avoid conditioning marks on the renewal count, embed successive complete runs in an infinite iid marked prefix. Their count divided by L tends in probability to p(1-p), or to 1/4 in the triangular case by bounded second moments of the geometric cycles. Sandwich the maximum pathwise between fixed-prefix maxima of (p(1-p) +/- epsilon)L marks on the count event, then send epsilon to zero. Runs meeting the cut and omitted from the prefix are bounded by the two geometric-tailed boundary fragments; they contribute o(1) at any threshold tending to infinity. The all-plus configuration has time zero, and conditioning away the all-minus event, of probability (1-p)^L, does not affect the limits. For p<1/2 the center is [log L+log(p(1-p)^2/(1-2p))]/(2p), with multiplier 2p; for p>1/2 it is log L+log(p^2(1-p)/(2p-1)), with multiplier 1. At p=1/2 the center is log L+log log L-log 8. In the window p_L=1/2+a/log L, exp[-(2p_L-1)t] tends to exp(-2a) at the stated thresholds, and the leading survival factor is exp(-t)(log L)w(a)/2, where w(a)=(1-exp(-2a))/(2a), w(0)=1. Adding log w(a) to the critical center gives Lp_L(1-p_L)R_{p_L}(t) -> exp(-x); the fixed-density centers give the same intensity at their scaled thresholds. The iid maximum formula then gives exp(-exp(-x)). For de-Poissonization, the first L prefix marks and the boundary lifetime have a uniform positive exponential-moment bound for each fixed p or near p=1/2 (choose the moment parameter also below the geometric-fragment bound). Their union bound gives conditional E[T_L]=O(log L). Independent rate-L interattempt gaps have conditional time-error variance J_L/L^2, with E[J_L]=L E[T_L] under the same conditioning, so the sweep error is o_P(1). The argument is analytic; the uploaded checker was not executed.

## originality

PASS

Best-of-knowledge PASS for the exact Bernoulli-initial ring absorption law: the density-dependent rate and center, the critical log log L term with its constant, and the fixed-detuning 1/log L crossover. The exact kinetic rule and deterministic run staging are prior work. Neither exponential resonance as a general mechanism nor the Gumbel maximum argument is original.

## value

PASS

The natural quantity is the time for the last minus domain to disappear, not the time for a typical site to flip. Its effective decay rate changes from 2p to 1 as the seed density crosses one half. Equal rates change the polynomial multiplier in the tail, leading to a log log L delay, and the order-one crossover constant describes which finite-size normalization applies near that density. This supplies an exact collective passage-time benchmark for a standard kinetic constraint and distinguishes iid preparation from the known deterministic patterns. The scientific contribution is this model-specific classification and window, not the general Gumbel method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
