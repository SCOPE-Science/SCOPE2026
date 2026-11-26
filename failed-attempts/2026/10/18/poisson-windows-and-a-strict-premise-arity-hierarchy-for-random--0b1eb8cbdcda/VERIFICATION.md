---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

A rule forbids precisely one row pattern on r=k+1 independent columns. The first moment is the number of labelled rules times q_k^n. If two supports share s<r columns, the two bad patterns either conflict or together specify 2r-s bits, so joint rule satisfaction is at most (1-2a+a²2^s)^n, with a=2^(-r). Distinct heads on one support have disjoint bad patterns and joint probability (1-2a)^n. The log of the proper-overlap bound is strictly convex, with endpoint values 2 log q_k and log q_k, proving the stated strict chord inequality. The disjoint-column dependency graph is valid for the whole neighborhood. Pair counts of order m^(2r-s) and m^r then give vanishing Stein–Chen sums at m on the critical scale and, by the same estimates, vanishing relative variance above it. Below it Markov applies. The limit t^r/k! counts unordered premise positions and the labelled head. For lower arities including zero, -log(1-2^(-u))/u is strictly decreasing in u, so the expected counts vanish in the k-window. The first moment for empty premise support has the same exponential base as the (k-1)-premise implication count and also vanishes there. Hence the claimed simultaneous minimality and support property holds only in the stated critical regime. Inspected the supplied checker as bounded corroboration, not as a proof of the limit.

## originality

FAIL

Bognár (1962) directly treats the same independent uniform random subsets, general fixed-arity Boolean relations, and their critical-window and overlap estimates. The k=2 implication is the complement dual of a printed strictly regular example; every higher fixed k is the same one-forbidden-atom specialization of the criterion. The earlier paper is not credited with an explicit TV count theorem. Instead, its already established negligible overlapping-pair sum, together with first moments and independent disjoint column sets, yields that theorem by the standard local-dependence inequality without a further probabilistic estimate. The hierarchy and support statements add first-moment comparisons of the same one-atom relations, not a distinct surviving result.

## value

FAIL

The random-implication question is natural, but as a new contribution the submitted hierarchy combines already controlled one-atom probabilities with immediate monotone comparisons of their bases. The TV refinement is a routine application of local Poisson approximation to the previously quantified overlap family. There is no remaining nonmechanical minimal-premise or support theorem beyond those direct applications in the stated critical regime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
