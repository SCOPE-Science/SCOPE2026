---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Conditional arclength is uniform in the affine edge parameter. For the two-plus-one configuration a slice through the centroid forces w>=1/2 and requires two independent uniforms to straddle w/(3w-1); integration gives 1/9+4 log(2)/27. For one per side, failure of any specified oriented-edge test has probability 1/2-integral_0^(1/2) (1-u)/(2-3u) du. The three failures are disjoint up to null sets: each requires opposite halves of the parameters at its two consecutive edges, and sharing an edge would require both halves for the same parameter. Cyclic symmetry therefore gives 2 log(2)/3. The multinomial occupancy probabilities yield the cubic, including zero weights. Strict pair balancing increases xy with x+y fixed and hence increases e2 and e3 with positive coefficients. The strict p_i<1/2 bound gives sum p_i^2<1/2, and only the permutations of (1/2,1/2,0) have limiting equality; the equilateral upper equality follows from the sharp e2 and e3 bounds. Same-edge triples cannot contain the centroid. Checked RESULT.md lines 25–88 and the packaged symbolic/Monte Carlo logic; the supplied script was not executed. The analytic check does not depend on sampling.

## originality

FAIL

The earlier November 2 Resultary finding explicitly gives the arbitrary-edge cubic, the arclength specialization, the same strict Schur-concavity and the same sharp endpoints. The October 25 finding already gives the arclength law, range and shape ordering. This is verified mathematical coverage, not a judgment based on paper access or a title match.

## value

FAIL

The natural Euclidean-versus-affine sampling distinction and sharp shape law are mathematically useful, but the frozen record supplies no new exact invariant, extension or genuinely different consequence beyond the already available same-model theorem. Recomputing both occupancy integrals does not create a surviving contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
