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

For k>=2 each induced type is either independent or K_{i,j}; matching ordered domain and range sets of the same type multiplies the square of the type count by the correct automorphism order, with a factor two for equal nonempty side sizes. Rank two fixes the product m=ab up to m↔binom(n,2)-m. Independently reduced the induced type polynomials modulo a²-na+m after b=n-a; checks/4.py (Python 3 and SymPy) verifies the rank-three identity and the rank-four reflection difference 2(n-2)t(8t²-n(n-1))/3 exactly, and independently enumerates the 4+4 vs 2+6 example. For two feasible reflected products, each is at most n²/4, giving |t|<=n/4; then 8t²<=n²/2<n(n-1) for every n>=4. Thus there is no nontrivial reflected collision through rank four. The pair with sides (h²,h²) vs (h²-h,h²+h) realizes distinct complementary products for every h>=2, proving sharpness, not just a finite search result. The scope is uncoloured bicliques with both sides at least two.

## originality

PASS

The supported distinct claim is sharp inverse reconstruction from numerical ranks 1, 2 and 4, including redundancy of rank 3 and the infinite lower-rank collision family. The full-spectrum census merits no separate originality credit here: the matching asymmetric record gives it for unequal sides, while an earlier homogeneous-graph record covers equal sides by complement. Same-day dating does not resolve precedence. The inverse threshold is not the extraction of an already given coefficient: it needs the reflection obstruction, uniform separation over feasible products, and an infinite collision construction, none of which is supplied by the matching formula statements. The existing reconstruction theorem for actual partial maps is a different input invariant. The frozen related-work paragraph should acknowledge the asymmetric census; that bibliographic omission does not change the distinct theorem.

## value

PASS

The inverse problem asks how much of a natural numerical monoid invariant must be retained to recover the biclique. The parity of the first informative rank is structural: rank three can never resolve the rank-two ambiguity, whereas rank four always does. An infinite family realizes the obstruction; the result gives a usable uniform cutoff independent of graph size, not just another forward census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
