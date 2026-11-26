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

The independent-domination definition is equivalent to inclusion-maximal independence. For given chosen duads D, independence forbids each syntheme meeting D, and domination forces every syntheme avoiding D to be chosen. Remaining duads must then be covered by those matchings, exactly the frozen mask criterion. The two recorded programs implement complete finite searches in two explicitly identified graph presentations; inspected them and their outputs without executing them. Independently generated the 15 duads and 15 perfect matchings from six labels and enumerated all maximal cliques in the complement by pivoted Bron–Kerbosch (python3 /workspace/independent_checks/5.py). Its P/X recursion exhausts maximal cliques without duplicates, and the output matches the full feasible/minimum/optimum table by duad count. In particular the exact size histogram is {9:90,10:2352,11:690,12:100,13:30,15:2}. Matched the optimum sets exactly to the 45 cycle pairs and checked all 4005 pairs of optima, obtaining exactly those 45 jumps and the same 45 slides. One may also see the exchange condition directly: a move keeping one bipartition part fixed cannot change the other, by forced completion in either direction. Any other jump from the four-duad to the five-duad class must nest their duad sets. A four-cycle plus its complementary disjoint edge contains just one four-cycle, forcing matching cycle classes. The removed matching contains the added complementary duad, confirming incidence for each slide. The two natural S₆ orbits follow from transitivity on four-cycles and the invariant duad count.

## originality

FAIL

The known minimum ordinary dominating-set classification for equal-order generalized quadrangles covers the independent optimum layer here. Héger–Hernandez Lucas's 2020 abstract explicitly announces sharpness and complete classification; the indexed mathematical account 4561b0658340 identifies Theorems 2.1, 4.5 and 5.1 and gives the specialized flag templates in full. The template crosswalk is exact, not inferred from matching counts. Given a duad–syntheme flag (c,L), take C to be the four-cycle on the four labels outside c whose two diagonals are the other two duads in L. This gives a bijection from flags to cycles. Of the vertices at distance exactly two from the flag endpoints as a set, the duads are precisely D=E(C): they are disjoint from c and exclude the two other duads of L, which are at distance one. The synthemes there share a duad with L but avoid c, hence are precisely F(D) minus L: a matching avoiding D either uses c and both diagonals (then is L), or uses the two remaining labels on cross edges and uses exactly one diagonal. Thus adding L or c to the distance-two set gives exactly I₀(C) or I₁(C), both independent. The new object names do not yield a new classification. Moreover all exits in the putatively distinct exchange layer follow immediately from the classified family: forced completion forbids jumps within either bipartition-count class; across classes the smaller duad set must be the unique four-cycle inside the larger. The flag swap is then necessarily the slide c↔L. The conclusion is based on the primary abstract, explicit indexed theorem account and verified mathematical implication together, not on the inability to retrieve the primary theorem pages.

## value

FAIL

The graph and the minimum-layer exchange invariant are natural. Here, however, the finite optimization reproduces the known flag classification in label coordinates, and the apparent reconfiguration remainder is determined by forced completion and the uniqueness of the cycle in a disjoint cycle-plus-edge. Equality of jumps and slides is in fact general for maximal independent sets: after a jump the deleted vertex would be undominated unless the added vertex were its neighbor. The exact exchange answer is therefore mechanically implied in this setting rather than an independently needed computation or a new rigidity argument. No distinct valuable repaired claim is supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
