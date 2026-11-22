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

The predictive Pólya law is a Dirichlet mixture for all real a_i>0. Conditioning on P shows P(no S in t draws)=(A-a_S)_{overline t}/(A)_{overline t}; inclusion-exclusion gives survival for t>=1. For a chosen pair with total h, Dirichlet aggregation makes Q=P_i+P_j and all outside probabilities independent of its split while U=P_i/Q~Beta(a_i,a_j). Conditional on the number M of pair draws and outside coverage, the chance both pair colours appear is 1-[(a_i)_{overline M}+(a_j)_{overline M}]/(h)_{overline M}; for M>=2 the summand is strictly convex and symmetric in the split, while it is zero for M<=1. Therefore any nontrivial balancing strictly raises P(T<=t) at each t>=k, since M>=2 and full outside coverage have positive joint probability for positive initial masses; for t<k coverage is impossible. A finite chain of T-transfers proves the full strict majorization order and uniqueness up to permutation. Each singleton absent probability equals Gamma(A)/Gamma(A-a_i) t^{-a_i}(1+o(1)); every pair absence is O(t^{-(a_i+a_j)}), so Bonferroni yields m Gamma(A)/Gamma(A-alpha) t^{-alpha}. Conditioning gives asymptotic probability 1/m for each of m minimal-mass still-unseen colours and vanishing probability for multiple unseen colours. The positive-power moment criterion follows from the discrete tail-sum comparison sum t^{s-1-alpha}. Boundaries k=2,t=0 and noninteger positive masses were checked. Independent fresh code compared 48 finite-time Dirichlet-mixture inclusion-exclusion probabilities to a distinct reinforced-path dynamic program, 36 strict-balance tests for three nontrivial transfers, and 8 large-t gamma-ratio tests; INDEPENDENT_CHECK_OK 92. Finite checks are not proof of the universal result.

## originality

PASS

Qualified acceptance only for the genuinely cross-parameter strict all-time stochastic majorization in a unit-reinforcement Pólya urn. Jacobs (2022) already contains the exact negative-Pólya all-colour completion distribution and must be credited; Henze–Holmes (2019) covers the one-colour tail; Zoroa et al. (2016) provides exact deterministic-iid coupon majorization. The decisive comparison is that neither latter theorem compares Dirichlet mixtures with different shape vectors at fixed sum. Calabrese (2012) varies replacement amount, Dean (2022) studies growing-composition limits. No stronger result in the bounded Resultary searches or primary inspected sources was shown to imply the strict alpha-majorization result; priority is best-of-knowledge with specific listed risk.

## value

PASS

This is a natural stochastic-order extremal problem for the time until every species/colour has appeared under preferential reinforcement. Uniform starting mass uniquely minimizes all attainable survival probabilities at a fixed total (not merely expectations that may be infinite), and the exact rarest-colour exponent demonstrates why tails and moments respond nontrivially to initial imbalances. The old exact distribution and scalar first-hit tail are background; the surviving strict all-horizon comparison makes an independently usable structural classification of the entire cover-time law. No broad downstream theorem is required and none is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
