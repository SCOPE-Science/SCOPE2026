---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Edge normals alone realize every unoriented chord-normal direction modulo pi, and the 18 directed supports have heights 1 at even indices and cos(pi/9) at odd indices. A genuinely slack side of a minimizing polygon can be pushed inward to remove positive area, and a triangle can be strictly cut by an additional nonagon edge support. Boundedness is equivalent to all successive gaps being less than pi. To confirm feasibility, write any other normal as Au_i+Bu_j in the basis of an adjacent pair; at least one coefficient is nonpositive. If just one is negative, maximize the other normal on the nonagon to show its contact point gives at least the tested value in the third direction. If both are nonpositive the tested value is nonpositive. Hence adjacent intersections satisfy the other constraints; coincident intersections may be counted as repeated vertices. I independently intersected the lines by Cramer's rule and used planar shoelace with rational enclosures, rather than the frozen support-area summation. The replay finds 1548 bounded normal sets, strictly separates all 1539 outsiders from the nine even shifts of (0,5,9,13), and verifies exact representative 2 sin(pi/9) times area = 5/4-c/2+2c² in the cubic field, with four distinct adjacent points. The opposing bases and reflection exchanging normals 5 and 13 give the isosceles trapezoid; parity gives one vertex and three edge contacts. Normalization is by 9sc. Under nonsingular affine maps the minimizing sets and area ratios, not the Euclidean isosceles property, are transported.

## originality

FAIL

The strongest distinct Resultary entry 54cf1fb013d5 states the same restricted optimization, the same nine normal quadruples and the same edge-only penalty and affine transport. Its area expression is precisely the area of (0,5,9,13): the two mixed 1,c gaps of 5 contribute the first term, and the two equal c,c gaps of 4 give 2c² tan(2pi/9). The independently verified shoelace of that very polygon is the frozen cubic expression divided by 2 sin(pi/9), so this is exact algebraic coverage, not a resemblance between decimals. Exact coverage by a distinct entry is not a judgment of who established the result first.

## value

FAIL

The regular nonagon and edge-only comparison have a genuine motivation in finite chord-enclosure conjectures. But the submitted exact invariant, contacts and diagonal necessity have all been catalogued together. Reproducing them in a different algebraic form does not supply a separate useful unknown benchmark or a new general result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
