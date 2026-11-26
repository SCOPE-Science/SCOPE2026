---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The rational return for (1,q,q) simplifies to ((1+qu+v)/(uv),(1+qu)/v), and the cited invariant specializes to the stated positive Laurent function. The max/log-sum error is bounded uniformly on compact sets by a constant times 1/t; this justifies passing the conservation identity to the limit at both the original and moving image points. The bounds y≥2−h, x≤h−1, y−x≤h−1 force h≥4/3 and equality only at the stated fixed point. For h≤2 these three lines enclose the entire sublevel triangle, the remaining bounds being redundant. For h>2, the vertical bounds and the upper/lower affine envelopes meet at the six stated vertices; their primitive lengths are h−2,2,h−2,h,h−2,h. The local branch matrices are integral unimodular and preserve primitive directions and their length coefficients; continuity, invertibility and orientation give a translation in the boundary arclength coordinate. The stated A→B and A→D images give exactly the two displacements and agree at h=2. At h=p/q>2, put d=p−q; gcd(2d,p+4d)=gcd(2,p), since gcd(d,p)=1. At integer energies, integral vertices make the boundary lattice points exactly the unit-spaced sites in that coordinate; the shell periods and counts follow, and the minimum rules out any energy below 2 for a lattice point. I inspected the packaged finite-check code and output without running them. The claims are verified by the all-level argument rather than by finite orbit samples.

## originality

FAIL

There is a zero-cost dynamical equivalence not tested in the frozen comparisons: De Angelis's published autonomous max-map rotation, squared and orientation-reversed, has exactly this rotation profile, with an elementary change of energy. For A=e^(−1) and j=log c, Theorem 4 gives the unit-step fraction g=1/6 for j≤1 and j/(5j+1) for j≥1. For h≥2 take j=h−1; for 4/3<h≤2 take j=(3h−4)/2. It follows that 2g is exactly the claimed ρ at every level. De Angelis's log-coordinate side data also give primitive perimeters 6j and 5j+1, exactly the submitted lengths under this reindexing. Indeed, matching the counterclockwise arclength of the forced polygons to the clockwise arclength of the autonomous log polygons conjugates the forced map to the square; both arclength systems on integer outer shells enumerate lattice sites in unit steps. Thus the period-three island, twist profile and parity split are covered dynamically, and not just similar to autonomous results. The six-sided versus seven-sided outer geometry is genuinely different as an embedded polygon, but does not distinguish the claimed dynamics or arithmetic and is not a surviving original research claim by itself.

## value

FAIL

The choice of a minimal nonconstant forcing and the exact shell law are well motivated, but the ostensibly new orbit invariants are mechanically recoverable from a known autonomous rotation by squaring and matching primitive perimeters. The residual embedded triangle/hexagon calculation is useful for implementing this coordinate description, but is a routine half-plane intersection with no substantive new phenomenon isolated in the record. There is no genuine remaining research claim to repair merely by relabeling the old result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
