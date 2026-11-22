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

At each convex polyhedral vertex, orient faces outward and label the three distinct side lengths modulo 3. The common cyclic label sequence forces each consecutive radial edge color to advance 2 mod 3, hence the vertex valence d is divisible by 3. Every three consecutive incident corners are the three angles of T once, so incident angle sum equals d*pi/3; strict convexity (<2pi) and d>=3 force d=3. Euler and triangulation counting yield V=F=4, E=6. Each side length appears on exactly two opposite tetrahedron edges, so P is disphenoid. The standard orthogonal coordinate realization gives x²=(b²+c²-a²)/8 etc, positive iff T acute, and uniform outward handedness by half-turn symmetries. The conclusion is an unrestricted combinatorial/convex proof; finite tetra/octa oriented-color verifier only corroborates.

## originality

PASS

Georgiou (2026) classifies reflection-allowed congruent triangular facets, cites direct orientation as remaining open for right/obtuse scalene triangles; his acute tetrahedron converse is credited. Hungerbühler et al construct monohedral shapes with reflected facet arrangements, and the exact scalene octahedron classification is only an 8-face reflection-allowed finite case. Neither entails the all-face-count one-handed exclusion. The local modulo-three valence/curvature obstruction is not located as a previously published theorem.

## value

PASS

Solves the mathematically motivated signed/direct-congruence variant for all convex face counts, distinguishing reflection-allowed universal realizability from a strong one-handed obstruction. A simple exact curvature quantization forces global tetrahedral rigidity and gives an iff acute existence theorem; this is an unbounded classification, not a cosmetic reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
