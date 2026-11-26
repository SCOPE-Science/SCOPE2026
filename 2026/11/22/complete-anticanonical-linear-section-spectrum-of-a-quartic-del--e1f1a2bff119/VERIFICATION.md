---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Independently polarized the two displayed quadrics and recomputed the pencil determinant and its gcd with its derivative over F5. The determinant has degree five, so there is no singular pencil member at infinity; the five simple roots give the smooth complete intersection by the pencil criterion. The 31 normalized simultaneous zeros agree as a set with the normalized columns transcribed from the published generator matrix. The frozen enumeration of annihilators by RREF is exhaustive. Independently obtained the plane profile without RREF or a no-more-than-four assumption: for each pair of surface points, project the points from its line into the three-dimensional quotient. The zero image contains exactly that pair; each nonzero projective quotient point represents one plane through the pair. Grouping images finds every plane with at least two surface points (divide by the number of pairs); the point and total incidences give the one-point and empty counts. This gives 640 four-point planes and none larger. Independently counted hyperplanes and obtained lines from the absence of collinear triples; points are immediate. Evaluation is injective because no hyperplane contains the whole set. Maxima 10,4,2,1,0 give (21,27,29,30,31), with empty projective common zero set for the full code. Multiplying each hyperplane count by four at weight 31−s gives the stated ordinary enumerator, plus the zero word.

## originality

PASS

The published example already gives the model, point count, generator matrix and minimum distance. The supported distinct contribution is the exact complete section-frequency data (particularly the 640 four-point planes and full hyperplane weight distribution). The higher-weight tuple is partly a consequence of elementary geometry and code dimension and is not credited as five separate new facts. No inspected source gives or mechanically implies the full frequency data without actually evaluating the incidence census.

## value

PASS

The object is an independently motivated published example of a high-performing nonsplit del Pezzo code, not a selected numerical subcase. Its finite section frequencies are canonical and distinguish the geometry of its higher-dimensional subcodes in a way the minimum-distance datum does not. In particular, 640 distinct planes give the multiplicity of minimum-support two-dimensional subcodes, and the ordinary distribution resolves all nonzero codeword weight frequencies. The low-codimension exact data, not the individually routine final generalized weights, justify the contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
