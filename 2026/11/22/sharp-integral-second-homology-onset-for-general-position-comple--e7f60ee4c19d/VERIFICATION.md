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

A triple fails precisely when a cyclic gap is at least n/2, because the complementary arc then contains the triple and is a shortest path, including ties. Any four vertices have two complementary two-gap arcs, one at most n/2 and hence containing a forbidden triple. Therefore C_3=0. For the positive ranges, balanced gaps g_i satisfy ceil(n/3)+1<n/2 at n=9 and n=12 and the slack is nondecreasing in steps of two; the gaps are also at least two. All eight transversals of three adjacent pairs therefore have positive gaps strictly below n/2. Their alternating chain is a nonzero 2-cycle since dropping any vertex cancels the two binary choices at that position. A coefficient +/-1 yields a map H_2->Z sending that class to a generator, proving primitivity. At each excluded order, listing positive triples of gaps below n/2 gives the frozen table. For n=7 an edge of gap 1 supports (1,3,3) uniquely; then a gap-3 edge supports (2,2,3) uniquely. At n=10 a gap-2 edge supports (2,4,4) uniquely; then a gap-4 edge supports (3,3,4) uniquely. The one-phase rows each have the indicated unique supporting edge. These removals leave no triangles. The final sentence about second-phase edges having 'no cofaces' after phase one is a local wording slip: they have exactly one remaining triangular coface, as the table and uniqueness argument require. This does not change the proved classification.

## originality

PASS

A distinct same-day record gives exact finite homology through n=12, thereby already establishing the first odd and even orders. No chronological order is inferred from the shared date. The supported distinct content is the exact all-order nonvanishing classification together with a uniform, primitive octahedral class. The same-object finite table gives no result for later orders, and the related cyclic Rips theorems impose a different face rule.

## value

PASS

For the natural complex of all geodesic general-position sets, an exact infinite-family top homology dichotomy is a meaningful invariant beyond maximal face size and an initial finite onset. A signed cycle on six vertices is an explicit primitive witness; its construction explains permanent nonvanishing in both parities rather than extrapolating a table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
