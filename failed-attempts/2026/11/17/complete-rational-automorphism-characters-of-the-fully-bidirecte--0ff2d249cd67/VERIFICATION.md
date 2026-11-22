---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For 18 ordered oriented arcs, the exact allowed-simplex predicate (distinct in/out endpoints, no directed cycles) gives 714 nonempty faces with f-vector (18,108,264,252,72); the original verifier enumerates every 18-bit subset. Its exact acyclic greedy Morse matching has 336 pairs and residual cells 1 vertex, 5 degree-two, 24 degree-three, 12 degree-four; top Morse differential vanishes and 5x24 next differential has a unit 5x5 minor, yielding Z ranks 19,12 in degrees3,4. Original top boundary rank60 in dimension72 leaves 12 top rational cycles. Signed action of all 72 automorphisms produces H3 traces (19,1,1,3,1,1,-1,1,-1) and H4 (12,0,0,0,0,6,-2,0,-2) on nine classes. Standard S3 wreath S2 character inner products give the listed seven and five unique irreducibles; H3^G dimension1, H4^G zero. This is a complete fixed finite calculation, not a family extrapolation. C PASS.

## originality

FAIL

Already-published 2026-10-18 result on the identical fully bidirected K3,3 multipath complex and the identical 72-element automorphism group supplies, in its Finding, the very same complete nine-class rational character tables for BOTH homological degrees, and the full-group invariant dimensions. Group-character orthogonality uniquely determines every irreducible multiplicity in the new claimed decomposition; the quotient rational Betti numbers follow via finite-group transfer. Thus the allegedly novel equivariant characters, decomposition and quotient rational homology are all already implied by that earlier text. FAIL.

## value

FAIL

Determining exact representations of a natural finite complex is intrinsically interesting, but this package reprints previously published same-object full characters, and its irreducible list is the routine unique character expansion with no new independent structure or limitation identified. No standalone new valuable claim remains. FAIL.

The dated certificate retains the supplied scientific assessment, sources and limitations.
