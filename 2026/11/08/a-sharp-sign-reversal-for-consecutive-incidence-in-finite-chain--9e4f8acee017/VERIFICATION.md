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

Directly reconstructed independent binomial C1~Bin(n,p), R1~Bern(mu), and E[C2|C1]=(n-C1)(1-a q^C1). Four binomial generating-moment identities give formula, including n=2 endpoint. Logarithm L(p) of bracket multiplier has L(0)=0,L'(0)=n-2+mu, strictly negative L'' and L(1-)=-infinity, proving unique positive crossing (or uniformly negative at n=2,mu=0). Root expansion uses n p^3=o(1), log(1+np)-np^2+o(1)=0 and uniform recovery bound; at fixed beta=Np, covariance tends to beta^2. Independently enumerated full two-round transition probabilities with exact fractions at many n,p,mu (not a proof of asymptotics).

## originality

PASS

Best-knowledge PASS. The exact two-round observable, recovery-dependent sign threshold, and log-log finite-size location do not follow from the primary general chain-binomial PGF formalism inspected. This is not a new stochastic transition model, binomial identity or fixed-beta branching approximation. Unindexed classical two-generation covariance formulas are an explicit priority risk.

## value

PASS

PASS. Exact positive-to-negative dependence transition of consecutive incidence in a natural finite epidemic, including the sharp log-log depletion crossover and its disappearance in fixed-contact branching asymptotics; meaningful diagnostic boundary rather than only parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
