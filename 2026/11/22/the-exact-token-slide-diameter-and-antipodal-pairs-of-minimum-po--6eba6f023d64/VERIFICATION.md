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

After domination the unobserved rectangle is the product of empty rows and columns. With both sides at least two no force starts; if one side is a singleton the appropriate row or column neighbors each have a unique unobserved neighbor. Thus the minimum states are exactly the two coordinate near-transversal families. Their internal degrees are n(n−1) each, their overlap has degree 2(n−1), and an exclusive-to-exclusive edge is impossible because a slide retains the set of coordinates of one type. This yields the stated edge and vertex counts. Within a family, move the hole once if necessary, then align at most n−1 entries, giving strictly less than 2(n−1) even at n=3. Across families an arbitrary matching of source rows to target columns gives a two-phase path of length at most 2(n−1); any shared row or column can be matched to save a slide. If neither coordinate is shared, the only possible endpoints are the complementary column and row stars. Tracking individual tokens proves that each must change both coordinates there, irrespective of temporary moves, and gives the lower bound and exactly n² unordered pairs. An independent calculation enumerated minimum sets by actual propagation, built edges via common deletion subsets, and tested all source orbits under row/column permutations and transposition at n=3,4,5. Sorted occupied-column multiplicities classify distinct-row states up to this action, so these 2, 3, and 5 representatives test every pair up to symmetry. Counts were (36,126), (416,2784), and (5650,60100), with precisely the stated extremal type.

## originality

PASS

The state structure and vertex count are established prior coverage. The distinct supported claim is the number of legal minimum-set slides and the sharp adjacent-slide distance with all extremizers. Checked reconfiguration results concern either a different move rule, a different graph, or a different domination/forcing parameter.

## value

PASS

The slide metric measures relocation effort when the monitoring budget stays optimal and a sensor can move only along an edge. General connectivity or the number of optimal placements does not give that worst-case effort. The sharp linear bound and complete description of its witnesses isolate a genuine obstruction (both coordinates must change for all tokens); the edge census further quantifies the legal choices on this basic graph family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
