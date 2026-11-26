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

For a pair at distance one the common neighbors differ only in the unique changed coordinate, so existence of a common neighbor defines the binary/nonbinary edge split in FO³. Each two-anchor coordinate allows (0,0)/(1,1) when the anchors agree, (0,1)/(1,0) for distinct binary anchors, and these latter two plus (1,1) for distinct nonbinary anchors. Independent coordinate choices give equality of extension supports for equal (b,s); a pebble move leaves at most two anchors. The resulting invariant preserves both equality and adjacency indefinitely. Conversely, bounded walks in either definable edge relation use three names by local rebinding; existence of a pair at exact finite distance k recovers the component diameters b and s, also distinguishing diameter zero. The representative and d+1 tally follow immediately. The four-clique corollary is read as in the proof, comparing the all-ternary nonbinary representative to a one-factor enlargement; existence of a four-clique need not separate an arbitrary product already having a K4 layer. The accompanying finite support and set-refinement outputs were inspected as corroboration, not executed or used as the infinite proof.

## originality

FAIL

A distinct indexed record states and proves the same classification as the k=3 specialization of its full spectrum theorem, with identical hypotheses and logical resources. This establishes coverage, not chronological priority: the displayed calendar dates do not order these results. The narrower correct finding supplies no distinct classification outside that coverage.

## value

PASS

The mathematical content is a complete structural classification for a natural anisotropic graph family, with exact minimal representatives and sharp variable-width examples; binary versus larger factors is intrinsic to unlabeled adjacency. Its scientific usefulness is separable from originality, which fails because this content is covered.

The dated certificate retains the supplied scientific assessment, sources and limitations.
