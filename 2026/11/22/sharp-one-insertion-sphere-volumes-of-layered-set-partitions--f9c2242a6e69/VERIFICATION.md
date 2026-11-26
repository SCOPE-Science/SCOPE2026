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

The frozen proof at RESULT.md lines 33–35 is invalid as written: inserting 0 between the two 1s of the layered word 0011 gives 00101, with two noncontiguous blocks, and deleting a member of another block can close a gap. In that example the layered deletion results 0001 and 0011 have different compositions. The replacement at /workspace/repairs/4/RESULT.md proves the required distinction in general and retains the formula, extrema and attainment counts. For two valid old-block deletions from distinct blocks, any noncontiguous block must be one of the two. If either is noncontiguous the other must be as well: its deleted member is an isolated gap between runs of the first, but is in a block of size at least two. The deleted members then must be adjacent and are the interior positions of a segment X^u Y X Y^v; deleting either one gives different ordered compositions (u+1,v) and (u,v+1). Thus distinct-block deletions cannot collide for a fixed source. Same-block collisions require a block of precisely two separated occurrences and contiguous intervening singleton blocks, because the intervening length sequence must agree after moving a part of size one from front to back. Each singleton-run pair yields exactly one such double history and there are no triple histories. The other losses are n for layered old-block insertions and L per run of length L for new-singleton insertions; interior singleton insertions in nonsingleton blocks have unique histories. The repaired optimization uses a strict decrease when borrowing one unit from a part of size at least three to split or shorten a singleton run, balanced lengths for the minimum penalty and strict superadditivity for the maximum including k=1. This reconstructs all boundary cases and optimizer counts. The frozen checker was inspected, not run; its recorded finite evidence covers through n=10 and does not establish the repaired proof.

## originality

PASS

After repair the exact claim is unchanged: a source-conditional one-insertion volume and its complete fixed-(n,k) optimization. The strongest available matching statement is a general equal-deletion-read classification. It is relevant to the mechanism of overcounting but does not give the conditioned volume or characterize and count extremizers in its available description. The full prior text was unavailable and stronger overlap is not excluded.

## value

PASS

The exact size of the set of distinguishable one-insertion outcomes measures one-edit ambiguity in a standard structured family, including the nonlayered outputs that are easy to overlook. The theorem shows a real dependence on the arrangement of same-sized blocks and provides maximizers, minimizers and counts at each n and k. The structural collision analysis, not merely convex optimization of a known penalty, supplies the exact invariant. No capacity claim is required or made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
