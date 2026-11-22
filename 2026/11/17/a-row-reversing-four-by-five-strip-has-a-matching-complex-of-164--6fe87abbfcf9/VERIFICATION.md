---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The assigned graph has 20 vertices and 35 edges including the four row-reversing seam edges. Independent recursion from that graph produced precisely 255300 matchings including the empty simplex, nonempty face vector (35,505,3910,17725,48197,77455,69770,31630,5820,252), reduced Euler 164; the ordinary seam gives reduced Euler 136. The inspected deterministic toggle discrete Morse construction pairs 127550 faces and checks no gradient cycles, leaving one 0-cell, 181 6-cells and 17 7-cells; signed 181x17 integer differential has 17 unit pivots. Its unit Smith form realizes homotopic cancellations because the Morse CW model is 5-connected and 7-cell attaching maps into the wedge of 6-spheres are integer degrees. The separate reverse matching has a degree5 critical cell and verifies d^2=0, consistent with wedge 164 S6. Computational exhaustion applies to this one finite graph only.

## originality

PASS

Best-of-knowledge search and actual statement comparisons across Resultary, primary accessible literature and the assigned proof found no earlier statement implying this specific final claim. Named comparisons below identify exact overlap and inapplicability; failure to find a source is not itself novelty proof, and material uninspected is retained as risk.

## value

PASS

The first twisted-seam width-5 four-row graph is a natural finite topological boundary case comparing Möbius-type closure with open and untwisted grids. Its integral homotopy wedge classification (including no higher attaching torsion), not merely an Euler number, is a substantial exact finite invariant useful when studying matching-complex periodic boundary conditions; the 164 versus 136 reduced-Euler contrast motivates the distinct object.

The dated certificate retains the supplied scientific assessment, sources and limitations.
