---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Each good has ONE Bernoulli(p) common realized utility for every agent, independently across goods. Precommitted disjoint bundles produce independent Bin(k_i,p) success counts; realized EF1 is exactly range<=1. Transfer one Bernoulli from size b to a (b>=a+2), couple U~Bin(a,p), V~Bin(b-1,p) and apply antisymmetry plus monotone-likelihood-ratio order. The (U,V)=(0,1) all-other-zero event yields strict gain >=(b-a-1)p²(1-p)^(m-2). Iterated smoothing gives unique balanced bundle multiset, finite adjacent-interval inclusion-exclusion yields exact P*, and the binomial local CLT/Gaussian Riemann sum gives (2^n-1)/sqrt(n)*(2π q p(1-p))^(-(n-1)/2) for fixed n,p. The m<=n and n=2 boundaries are covered. Independent exact exhaustive small-allocation enumeration agrees.

## originality

PASS

PASS, qualified. Igarashi–Oh Fair Division of Lotteries centers exact ex-post envy-freeness with range=0, while this claim optimizes the larger range<=1 EF1 event under common item draws with a strict finite transfer inequality and fixed-population asymptotic. Later Resultary counterexamples with agent-specific Bernoulli realizations use a different stochastic model. General binomial likelihood-ratio arguments are prior tools, not claimed original. Full primary Igarashi–Oh source could not be retrieved through allowed routes (authorized institutional access blocked); compare known theorem descriptions only and retain risk that a hidden general likelihood-ratio lemma implies the EF1 result.

## value

PASS

PASS. The gap between ex-ante fairness and ex-post EF1 is a natural risk-of-fairness question; this theorem classifies every optimal pre-realization assignment, gives a sharp positive one-transfer improvement for all population and goods counts, and proves that even optimal eventual realized fairness decays polynomially with exact coefficient. It is an independently useful stochastic fair-division result beyond an elementary binary event probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
