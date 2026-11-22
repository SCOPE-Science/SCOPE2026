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

Every ideal hyperbolic quadrilateral has one real cross-ratio modulus; sending its diagonal intersection to Klein origin puts vertices (±c,±s), c²+s²=1. Minkowski side-distance formulas yield sinh(inradius at (x,y))=min((c-|x|)/s,(s-|y|)/c)/sqrt(1-x²-y²). For u=|x|<=u*=(c²-s²)/c the horizontal-side bound decreases with v and is maximized at (u*,0). For u>u*, equality of the two monotone competing bounds occurs at v*=(cu-(c²-s²))/s; there the squared maximum is (c-u)/(u+3c-4c³), strictly decreasing. Thus unique |x|=u*,y=0 and F²=1/(4c²-1): exactly two centers if c>s, merged to one at c=s, with appropriate 3-side versus 4-side tangencies. Independent numerical global searches at c=.75,.85,.99 found the predicted centers and radii, but calculus is the proof; ideal limit c→1 is excluded, square boundary included.

## originality

PASS

The classical projective Klein/cross-ratio normalization is prior geometry, as are inball radius problems for simplices. A planar simplex is triangular and therefore does not imply four-sided ideal-quadrilateral two-center symmetry breaking. Primary Izmestiev porism analyzes projective/cyclic quadrilateral relations rather than maximal inscribed hyperbolic disks. The exact two-versus-one locus and radius survive these mathematical comparisons, with unindexed historical geometry retained as a risk.

## value

PASS

The regular ideal square admits one maximally tangent disk, while every nonsquare ideal quadrilateral has two largest disks each touching only three sides. This sharp symmetry-breaking and location formula is a complete classification for a one-parameter natural geometric moduli space, with a nontrivial global maximin proof. The exact boundary between one and two solutions is potentially useful to hyperbolic inball and polygon-center questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
