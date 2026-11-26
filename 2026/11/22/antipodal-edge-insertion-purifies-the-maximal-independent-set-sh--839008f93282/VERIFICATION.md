---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Use the explicit folded 5-cube F=Q4 plus antipodal edges, not the 10-regular complement. A shattered support must be independent to admit the full trace. An independent triple can be translated to 0 and two sums of direction pairs with a shared member; translations and direction permutations give one orbit. At {0,3,5} the three independent extensions are 6,9,14: the latter two lie with the triple in N(1), and the first is the affine-sum extension, adjacent to both others. This gives 160 triples, 80 neighborhood quadruples and 40 affine planes. The planes are maximal independent and the sole extensions beyond four are the 16 neighborhoods. Each neighborhood quadruple extends to exactly one maximal independent set, ruling out shattering a five-set. The two orbit representatives are shattered by the listed witnesses. Independent reproduction enumerated all 65,536 supports per graph and all maximal-independent-set traces; replay python3 /workspace/branches/13e11a5a-0a54-4226-a73e-81ef5bbc595f/recheck.py. It confirmed both polynomials, the orbit types for F and the eight antipodal pair facets of Q4. The difference is setwise, not just a net count: a Q4 shattered four-set contains no antipodal pair by the pair-facet result, so is independent in F and remains shattered; exactly 16 new four-sets result. A separate local obstruction identifies these new four-sets as the 16 ordinary Q4 neighborhoods: each neighbor of a queried vertex in N_Q4(v) is v or is at distance two from v, and so fails to be private to that vertex. No trace with exactly that one vertex absent can be achieved in Q4. All 16 neighborhoods become shattered independent quadruples in F, accounting for the whole difference. The supplied scripts were inspected, not executed.

## originality

PASS

The standalone Q4 polynomial and facet structure are directly covered by a distinct same-day Resultary record and are credited rather than accepted as a distinct result. In the frozen comparison Q4 is the baseline. The supported distinct contribution is the structural folded-cube shattering classification and exact change of the complex under inserting the antipodal edges. The earlier or same-day general/comparison statements examined do not cover that contribution.

## value

PASS

A natural symmetric edge insertion raises the number of shattered four-sets while removing pair facets and making the shattering complex pure, without changing its dimension. The folded four-facet geometry and obstruction at five give a concrete structural distinction from independence. The exact perturbation is useful as a benchmark for how shattering by maximal independent sets responds to changes in adjacency; the already covered cube numbers serve as its comparison, not its value on their own.

The dated certificate retains the supplied scientific assessment, sources and limitations.
