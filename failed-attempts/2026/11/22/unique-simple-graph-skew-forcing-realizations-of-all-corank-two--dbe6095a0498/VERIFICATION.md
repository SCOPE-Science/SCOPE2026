---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

In a rank-two dual the hyperplanes are exactly the loops together with one nonloop parallel class. Their complements are the circuits of M and exactly the nonempty neighborhoods of the proposed graph. A forcing step is therefore precisely a circuit completion; every matroid closure element outside the initial set has such a witnessing circuit, so the two closures agree on every subset. In any competing simple graph each nontrivial component saves at least two initially filled vertices by starting with just the endpoints of an edge unfilled. Additivity and minimum size n−2 imply one nontrivial component, to which DeAlba’s complete multipartite characterization applies. The multipartite graph's class and isolate data are then recovered from the dual; this includes K₂ with no isolates when n=2. The successful sets contain complements of bases of the dual, giving the three enumerator coefficients, and base exchange is edge incidence. The Tutte sum separates the empty subset, subsets of one class and subsets meeting multiple classes on the nonloop restriction of P; the displayed intermediate T_P refers to that restriction, as the paragraph specifies. The final dual formula correctly restores the x^ℓ factor for coloops. Independent enumeration of all labelled simple graphs for each n from 2 through 5, not only preconstructed multipartite graphs, gave 1, 7, 36 and 171 with forcing number n−2; for each it verified the multipartite description and full closure by the dual rank test.

## originality

FAIL

The full corank-two classification is a direct corollary of established results, not just the uniform special case. Standard rank-two duality gives the circuit neighborhoods of the proposed multipartite graph, so Hall–Pfeil–Taylor Proposition 2.10 gives all-subset closure equality immediately. For uniqueness, DeAlba Theorem 3.3 and component additivity force the graph to be multipartite apart from isolates; Hall–Pfeil–Taylor Proposition 2.8 already identifies identical nonempty neighborhoods with series pairs, exactly the nonloop parallel classes in the rank-two dual, and omitted singletons detect isolates. Thus the labelled inverse follows without a new classification lemma. The enumerator, line graph and Tutte expression are direct translations of the same rank-two partition. No earlier verbatim statement of the combined theorem was established; the basis for failure is demonstrable implication, not wording or search incompleteness.

## value

FAIL

The realizability question is natural, and the explicit synthesis is useful exposition. As a standalone research finding, however, it does not resolve a mathematical gap beyond the existing realization criterion, extremal graph characterization and series-neighborhood theorem. The remaining formulas use standard rank-two counting and Tutte duality; none of them supplies an independently unresolved exact invariant or a new mechanism on the stated domain. No substantive surviving repair is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
