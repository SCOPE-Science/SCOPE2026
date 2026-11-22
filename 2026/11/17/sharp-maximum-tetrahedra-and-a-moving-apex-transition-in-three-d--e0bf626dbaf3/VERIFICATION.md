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

Given Bayer et al. Theorem 2.3 vertex characterization, translated polytope has 16 symbolic vertices, reduced to 10 when C=0. Determinant is multi-affine in four corners; vertex quadruple suffices for maximum. Independent sympy generated all C(16,4)=1820 symbolic determinants: exactly two ±(A^3+B^3), six ±B²(C+A) and 1812 others with for both signs coefficientwise nonnegative nonzero margin below A^3+B^3; C=0 coincidences collapse. Convex combinations of signed determinants show nonvertex equality is possible only via the six top apex vertices sharing three axial vertices; gives full 2D permutahedral apex face. Δ=(d-e)C²+(2d²+e²)C+d³+d²e+2de²+e³ switches once if e>d, never if e<=d; tested including C=0. This exact polynomial certificate plus multiaffinity proves full real C≥0,d,e>0, not merely finite samples.

## originality

PASS

Best-of-knowledge original contribution remains after subtracting credited prior special or broader results; each of four implication comparisons and source inspections below document the boundaries. 

## value

PASS

Maximum-volume contained simplex is a natural affine/metric invariant at the first nontrivial dimensional case, and identifying a sharp two-polynomial envelope with an optimizer-locus dimension jump 0→2 is substantive. This is not the known polytope volume, vertex count or enumeration alone; arbitrary-point equality uses a separate geometric argument.

The dated certificate retains the supplied scientific assessment, sources and limitations.
