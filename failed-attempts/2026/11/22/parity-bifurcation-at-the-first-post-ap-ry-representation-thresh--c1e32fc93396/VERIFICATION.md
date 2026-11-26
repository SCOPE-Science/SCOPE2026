---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The gap predicate is d_a(n)≤p, not nonrepresentability. At fixed total coin count k, writing u=y+2z gives the exact allowed range max(0,u-k)≤z≤floor(u/2), on 0≤u≤2k. For n=aq+r with 0≤r<a and q≤a+1, only k=q and k=q-1 can contribute. For q≤a a lone first term is at most ceil(a/2); when both terms contribute their sum is q-h for odd a=2h+1 and q-h+1-(r mod 2) for even a=2h. This includes the whole initial interval. At q=a+1 both terms contribute, and the counts are h+2 for odd a, or h+2 at even residues and h+1 at odd residues for even a. In the even q=a+2 block the only extra term is at r=0, and the counts are all above threshold. Appending an a-coin preserves each residue's above-threshold property, so no gaps follow. This also proves the cardinality and connected-component assertions including a=3,4.

## originality

FAIL

The complete-set result is a direct specialization of previously published layer counts, residue monotonicity, and the known maximum, and is explicitly covered for every a≥5 by two distinct broader parity-specific records. The relative ordering of the same-day records is not established and is not needed for the mechanical implication from the earlier result. Neither small endpoint a=3,4 escapes that implication.

## value

FAIL

Complete topology of a gap set can be useful, but here the only distinction from the earlier maximum collapses to two immediate evaluations of the published layer count, with the entire range already governed by published monotonicity and the cutoff. The companion band results also give that topology for all non-minimal sizes. The two smallest instances and the parity census supply no independent surviving invariant beyond those implications.

The dated certificate retains the supplied scientific assessment, sources and limitations.
