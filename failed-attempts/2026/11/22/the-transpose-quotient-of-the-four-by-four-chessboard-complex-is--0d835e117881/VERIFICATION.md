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

Rank preservation in the face-poset subdivision makes each simplex closure inject into the quotient: orbit-equivalent points in a closure have identical supporting ranks, hence the same support, and the action fixes that support pointwise. Thus signed deletion of flag members gives the regular cell boundaries and unique active top cofaces really are free. Independently enumerated matching faces and strict flag orbits in replays/3_5_topology.py (run with argument 3), obtaining (125,586,768,300), and replayed all 300 stored collapse pairs, leaving (125,586,468). Independently contracted a spanning tree of the residual complex and used triangle relations with just one unknown edge to kill all 462 non-tree generators. This proves simple connectivity without relying on the packaged Tietze implementation or published connectivity bounds. The two-dimensional residual complex has Euler characteristic 7 and free H₂ of rank 6; Hurewicz and homological Whitehead give the integral wedge equivalence.

## originality

FAIL

A distinct indexed record, 830d1ace075a, gives exactly the same integral homotopy classification for the same geometric transpose quotient. The differing finite or group-theoretic checks do not distinguish the frozen mathematical claim. It is not the self-match 0d835e117881. The same catalogue date does not establish which version came first, or whether they were independent.

## value

PASS

The row–column exchange is a canonical symmetry at the first simply connected balanced rank. An integral orbit homotopy classification, including simple connectivity and torsion, is stronger than numerical homology and is useful for distinguishing the orbit space from the original complex and its fixed space. There is no separate mathematical conclusion beyond the exact companion; the claim fails originality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
