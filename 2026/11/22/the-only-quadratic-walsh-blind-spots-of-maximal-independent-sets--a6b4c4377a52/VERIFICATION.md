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

In a nonempty maximal independent set, clockwise gaps are 2 or 3; fixing one vertex roots an ordered composition, and fixing a second independently roots both arcs. Thus the one- and two-site incidence counts are b_n and b_d b_(n−d), including d=1 where the latter is zero. Perrin recurrence and lengths 3,4,5 give P_n=2b_n+b_(n−3). Expanding the two Walsh signs yields H(n,d)=4b_d b_(n−d)−2b_(n−2)−b_(n−3). The constant mode is positive, the singleton multiplier b_(n−3) vanishes only at n=4, and adjacency gives a strictly negative pair multiplier. The exact seeds at distances 2 through 9 suffice: each later H is the sum of its two- and three-step predecessors, and all earlier feasible lengths in those rows are accounted for. For larger distances use d≤n/2 and the proven bounds 0.408<b_k/λ^k<0.421 for all k≥10; they propagate from 10,11,12 because λ^(−2)+λ^(−3)=1. The strict rational comparison 4·0.408²>0.421(2/L²+1/L³) at L=1.324717957 enforces H>0 when both arcs are at least 10. Thus the finite check is not used to infer infinite nonvanishing. At n=9 each of distances 3 and 4 has nine unordered pairs; ordinary unnormalized convolution multiplies each Walsh character by its own coefficient.

## originality

PASS

The counting formula is already substantially covered, as are examples of low-degree zeros and full nonvanishing on nine residue classes. The surviving distinct claim is the exhaustive classification in degrees at most two at all lengths, including exclusion within residue classes where the full operator can be singular. None of the inspected strongest statements supplies that exclusion or implies it without further mathematics.

## value

PASS

The restricted low-degree band has a natural role: it comprises all linear and pair statistics of the vertex bits. Exact identification of which such signals are erased by this unweighted averaging is a useful discrimination even when the full operator is singular. The result is a complete invariant for this band at every cycle length, not a repetition of the known count formula or a cutoff picked after an enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
