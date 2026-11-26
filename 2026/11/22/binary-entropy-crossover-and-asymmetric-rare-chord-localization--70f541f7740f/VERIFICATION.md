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

The norm comparison locates maximal radius at the axes for p<2 and the diagonals for p>2; central symmetry makes the diameter twice that radius. Taylor expansion of |cos α|^p+|sin α|^p at p=2 is uniform including axes because t^p(log t)^j is bounded for j≤2. It gives r=1+(p−2)H/4+O((p−2)^2). Differentiating the exact formula for r uses uniformly bounded t^(p−1)log t, so r′=O(|p−2|) and the angular arclength density tends uniformly to 1/(2π). Comparing each endpoint to its unit-circle counterpart introduces O(ε) chord error, so the deficit event forces |β|=O(√ε). In that window the cosine rule and uniform continuity of H give deficit/ε=z²/4+Gλ(α)+o(1). Changing β to √ε z, using the null-measure limiting boundary, and dividing by the positive limiting event mass gives both the probability and the uniform sublevel-set mark. Its z section has length 4√(x−Gλ)_+, confirming the prefactor and the exact circular normalization. For large positive λ, the diagonal entropy loss is 2u²+O(u⁴); each of four contacts contributes πx/(2√λ) to the angular integral. For λ=−L the axis entropy is u²log(1/u²)+O(u²); at u=√(2x/(L log L))v the penalty tends uniformly on bounded v to xv², and monotonicity away from the axis bounds support in that scale. Four contacts and the semicircle integral give 2√2 x/(π√(L log L)). These are iterated limits only. Read RESULT.md, VERIFICATION.md and verify_entropy_chords.py as text; finite quadrature was not rerun and is not needed for the exact limit.

## originality

PASS

The circle case, the fixed-exponent endpoint geometry, and one-sided entropy localization have direct prior or adjacent overlaps. The distinct claim is the two-sided moving-exponent Euclidean-arclength endpoint law, its normalized joint marks, and the comparison of far-profile amplitudes. The closest same-day records do not give this combined result; their date does not establish priority. This is a bounded originality judgment.

## value

PASS

The result resolves a gap between the circle law and the nonuniform fixed-shape tails in a natural deformation. It determines not just leading probabilities but where each endpoint pair concentrates and its mismatch distribution. The transition from smooth diagonal contacts to an axial entropy loss explains an additional logarithmic factor on just one side, with sharp amplitudes under arclength sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
