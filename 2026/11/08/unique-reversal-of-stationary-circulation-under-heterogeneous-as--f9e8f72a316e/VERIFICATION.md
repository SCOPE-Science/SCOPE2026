---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

Actual RESULT.md, SLOGAN.txt, VERIFICATION.md and verify_aspiration_cycle.py were inspected from the frozen Git snapshot. The orientation 00->10->11->01->00 gives the exact R(t)=F/G from direct payoff flip rates; F-G=t(P+Qt). For u=β(B-1), v=βB with v-u=β>0, f(z)=(u/v)(∫_0^z exp(uw)dw)/(∫_0^z exp(vw)dw) and g(z)=(u/v)(∫_0^z exp(-uw)dw)/(∫_0^z exp(-vw)dw). The first weighted ratio strictly decreases in z and the second increases, and multiplication by u/v changes signs as specified for B<1. Hence P,Q are nonzero opposite signs for all a>b>0, giving a unique t_*>0; monotonic t=e^{-βA}, Kolmogorov reversibility, and constant stationary edge current prove the sign formula. At A_*, detailed balance and Σ=0; elsewhere Σ=J log R>0. B=1 and a=b yield R=1. A separate independently written SymPy exact Markov classifier verified the three social-dilemma currents and product ratios (1/2904,33/26), (0,1), (-8/2055,26/33), three B=2 witnesses and their stationary vectors, and the B=2 polynomial factorization. Eighteen additional parameter sign/root tests corroborated, not substituted for, the unrestricted proof. All seven fetched Git blob SHAs reconstructed exactly the assigned tree 2ebe4629b4fae7031457c0c4f2adb99f17028b02. Limits: excludes β=0, infinite A, mutation and N>2; no inference of deterministic cycles.

## originality

PASS

Qualified best-of-knowledge. The closest primary Foster–Knight–Krapohl 2026 full text supplies this aspiration update and tracks mean cooperation, not the exact Kolmogorov affinity threshold or strict current sign. Du et al. 2014 and the 2015 structured counterpart establish detailed balance on aggregated scalar birth–death chains, not heterogeneous four-state flux. Zhou et al. 2018 addresses heterogeneity of update functions and population additivity; Foster et al. May 2026 exact product stationary law applies to counterfactual introspection, not aspiration. Materially reviewed two related published Resultary results (incidence-kernel Fermi imitation and metric-graph circulation) without statement implication; matching Resultary entry is the assigned finding’s mirror. One plausibly related 2026 step-level threshold-public-goods source remains uninspected because full text is not openly available and authorized institutional retrieval reported VPN disconnected; abstract-only information is not used to assert noncoverage.

## value

PASS

This is a motivated exact dynamical classification for the smallest population permitting a nontrivial labelled heterogeneous action square. A microscopic non-equilibrium current is invisible to mean stationary cooperator abundance. The theorem proves the existence, uniqueness and strict signs of a reversible/irreversible transition for all unequal positive contributions and all positive finite intensities; it also supplies an exact nonzero positive-aspiration witness inside the genuine 1<r<2 social-dilemma regime, and sensitivity-independent B=1/2 and B=2 thresholds. The universal monotonic coefficient-sign argument is more than computing one finite 4x4 inverse. It does not claim applicability to larger populations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
