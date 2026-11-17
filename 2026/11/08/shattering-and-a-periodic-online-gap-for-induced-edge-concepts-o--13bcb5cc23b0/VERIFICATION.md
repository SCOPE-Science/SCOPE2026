---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For n>=3 and edge labels b_i=a_i*a_(i+1), image consists exactly of cyclic 101-free words: two neighboring positive edges force their middle edge. Shattered supports are cyclic 111-free because every connected component of queried edges is a vertex-disjoint path with 1 or 2 edges, permitting arbitrary endpoint selection. Marked-zero run vectors give s_k=n/(n-k)[t^k](1+t+t^2)^(n-k); VC=floor(2n/3). Partition indices into length-three blocks (at most seven possible patterns, Ldim<=2 each) gives upper 2q for n=3q and 2q+1 for n=3q+1. For n=3q+1 the root e0=0/1 both admit 2q independently selectable edge labels, yielding online depth 2q+1. No all-order Ldim for n≡2 mod3 is asserted. Independent exhaustive cycle C7 traces and online dynamic recursion gave VC4 and Ldim5; source checker inspected.

## originality

PASS

Classical cyclic 111-avoiding enumeration is not novel in isolation. The edge-AND image, exact shattering-complex identification and especially infinite n≡1 mod3 Littlestone separation were not obtained from inspected broad closure/zero-set results.

## value

PASS

A natural graph-induced Boolean concept class has a complete static support criterion, exact labeled support spectrum and a sharp unbounded-order periodic adaptive/static gap. The residue is forced by local 3-edge obstruction rather than arbitrarily selected instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
