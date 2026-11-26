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

Writing L=N−1, weighting the cosine mode by the square root of the degree gives the symmetric normalized-path eigenvector, including the alternating terminal mode; each mode normalization cancels in its vertex/endpoint ratio. The observation matrix is a Vandermonde times a diagonal eigenvector-evaluation matrix; the nonzero common factor cancels, leaving amplitude ratio 2^(m/2) times the absolute cosine product at interior sites. For m=2, reflection and strict monotonicity reduce to comparison at π/L. For m=3, the side lobe of |u(2u²−1)| is at most 2/(3√6); at L≥6 the first-interior product is at least √3/4 and beats endpoints. For L=2,3,4,5 the maximum unscaled interior products are 0, 1/4, 0, 1/4. For m=4, z=cos²x gives z(2z−1)(4z−3). On 0≤z≤3/4 the larger absolute extremum is (10+7√7)/108, less than 21/64; on the remaining interval the cubic increases. For L≥9, z at j=1 exceeds 7/8, making the amplitude ratio exceed 4(21/64)>1 and all other half-path values strictly smaller. The small-L cases reduce to exact products: at L=5, |cos x cos 2x|=1/4 for every interior site; at L=7, cos(4x) and cos(3x) agree in magnitude and |sin(8x)/sin x|=1, giving unscaled product 1/8; at L=8, odd j give 1/4 by the sine double-angle identity and even j give zero. For L=3,4,6 direct substitution gives the remaining all-tie, endpoint-only, and j=2,4 tie cases. Finally the three cosines tend to one at j=1 and the squared amplitude ratio tends to 16. The bounded checker is corroboration only.

## originality

FAIL

A distinct indexed Resultary finding covers the entire classification under precisely the same observation and multiplier hypotheses. Normalized adjacency S and normalized Laplacian I−S have the same ordered low-frequency modes after reversing the eigenvalue order, and the multiplier function is changed by composition with λ↦1−λ. The extra displayed limit follows immediately from that finding's exact ratio. The distinct record is dated later; the equivalent coverage is demonstrable, but no earlier priority or dependence is inferred from the dates.

## value

FAIL

A complete low-band optimal-placement diagram with real equality cases is a meaningful design result, not an arbitrary set of small paths. But as submitted it adds no new design case to the exactly covered diagram; the only extra numerical limit is a direct evaluation of the indexed formula, not a substantive surviving increment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
