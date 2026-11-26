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

The repaired RESULT.md under /workspace/repairs/2 proves the same claim. In the frozen proof, moving both endpoints in the same cyclic direction gives order a,a',b,b', so the query chord crosses the marked chord itself, which is wrong for an open neighborhood. The opposite-side move used in the repair gives a,a',b',b; it preserves all crossings with other marked chords. All traces can then be realized simultaneously by using distinct new endpoints in the specified gaps. For the lower bound, gap-prefix parities are the empty mask, two endpoint singletons, and all consecutive two- and three-blocks. The repaired case split includes shifted three-blocks with a one-point overlap, an omitted case in the frozen exhaustiveness explanation; this gives two length-two runs, already counted. For the two-run types of lengths a,b in {2,3}, at least one middle zero gives binomial(m-a-b+1,2) placements. Equal-block offsets one give singleton displacement two or three; unequal-block overlap gives (1,2) and its reflection, with exactly one duplicate apiece when adding the endpoint-singleton cases. Two endpoint singletons give an extra (1,1) for m>=7. Nesting and adjacency contribute only lengths 1 through 6, each appearing at every possible start. Summing the table gives 2m^2-4m+1. I independently enumerated the pairs of endpoint gaps by testing exactly one marked endpoint in [i,j), confirming 31 and 49 distinct traces for the boundary cases m=5 and m=6. The formula for arbitrary m rests on the repaired case split, not the finite check. The frozen verify.py was inspected, not run, and its finite census assertions are unaffected.

## originality

PASS

The corrected proof makes no change to the claim. The inspected statements support the all-size trace census and sharp coefficient as distinct from the prior finite shattering calculation, insertion-type count and general VC framework. The m=5 case and the basic encoding are not credited as independently new. This is a best-of-knowledge judgment, not a claim of historical priority.

## value

PASS

The invariant is a natural extremal measure of the size of the set system of open neighborhoods. The upper bound by endpoint gaps is elementary; the content is that collisions cost only O(m) of the gap pairs, shown by one uniform explicit construction with an exact census. VC dimension alone does not answer this, and the result does not claim a sharp finite global maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
