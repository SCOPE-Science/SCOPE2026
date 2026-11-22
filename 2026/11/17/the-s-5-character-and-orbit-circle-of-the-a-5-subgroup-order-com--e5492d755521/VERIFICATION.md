---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Independently enumerated all 60 even permutations, closure-generated all 59 A5 subgroups including endpoints, verified the proper orders 2:15,3:10,4:5,5:6,6:10,10:6,12:5, and all 57 vertices,131 inclusion edges,15 triangles. Every C2<V4 edge is a free face of exactly one C2<V4<A4 triangle, leaving a connected 57-vertex,116-edge graph; b1=60. Across all 120 S5 conjugations the exact fixed-face Lefschetz traces are 60 on identity, 6 on transpositions, 0 otherwise. These yield the listed 60-dimensional Specht multiplicities and a one-dimensional invariant. Orbit counts under both inner A5 and full S5 are (7,8,1); the one triangular orbit has a free (2,4)-edge orbit, and the connected residual graph has b1=1, giving ordinary S1 quotient. Exhaustive finite verification pertains exactly to A5, no extrapolation to other groups.

## originality

PASS

PARTIAL PRIOR COVERAGE explicitly credited: a separate 2026-11-17 published paper already establishes the INNER-conjugation A5 subgroup quotient ≃ S1; its cell orbit counts (7,8,1) coincide with S5 counts, so the outer S5 orbit-circle assertion follows. The surviving independent contribution is the full class-by-class 60-dimensional S5 homology character and explicit Specht decomposition, not stated in the prior orbit result or known nonequivariant Möbius value. Best-of-knowledge PASS solely on this substantial equivariant representation remainder; no new credit assigned to the covered quotient-circle component.

## value

PASS

The complete rational outer-automorphism character of the A5 proper-subgroup complex is a natural finite-group topological representation, distinguishing full S5 and inner A5 symmetries. Its six nonzero Specht multiplicities and transposition trace provide nontrivial equivariant information beyond a known wedge count, Möbius scalar or quotient-circle topology. The already-covered orbit-circle is not credited toward value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
