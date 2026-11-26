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

Independently exhaustively reproduced the three-state synchronous two-contact dynamics from the exact edge lists, without executing the supplied programs. In the audit, disjoint bit sets E and R encode excited and refractory vertices; the next state is (A(E) minus (E union R), E) where A(E) consists of vertices with at least two neighbors in E. Enumerating all E and every submask of its complement for R visits each labeled state exactly once. Iteration to the absorbing empty pair gives first-rest histograms (1,2047,51361,87116,36202,420) of 177147 states and (1,4095,117272,237555,151450,20160,908) of 531441 states. The largest nonempty bins 5 and 6 give the sharp times, and a nonzero periodic orbit is impossible. The independently recovered least base-three sharp witnesses 1089 and 120 give trajectories (1089,67792,153098,43767,54,0) and (120,9232,254180,492804,40825,2,0). At threshold one, the respective cycles are (448,88769,176502,448) and (448,265916,530796,448); the K4,4 cycle has the four displayed distinct states and the verified closing transition at threshold two. Checked the Grötzsch construction directly from C5 and its twins; checked the exact labeled Chvátal edges against the independently published graph generator. Both are triangle-free and four-chromatic by checking edge-neighborhood intersections and possible three/four covers by maximal independent sets. The finding concerns precisely these two labeled graphs; the Chvátal graph's extremal description should be read with four-regularity, not as another unqualified minimum-order example.

## originality

PASS

The strongest same-graph records concern threshold one (including a three-state Grötzsch record indexed on the same day) or a four-state rule. The strongest threshold-two overlap is a theorem only on initially primitive-three states at half degree, which excludes that period on Chvátal but not other periods or long transients. None of these actual statements gives the paired threshold-two zero-map identities, sharp transients, or first-rest distributions.

## value

PASS

The two graphs are standard extremal chromatic benchmarks, including the regular case. Exact finite extinction on both is not forced by triangle-freeness, four-regularity, or initial-three-cycle exclusion. The sharp unequal cutoffs and full first-rest distributions provide useful finite-network benchmarks for the effect of contact threshold, and the oscillating biclique shows a concrete boundary of the phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
