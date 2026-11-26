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

For a central plane missing the vertices, an edge is crossed exactly when the endpoint signs differ. The intersection point is exposed in the section by a functional exposing that edge in the prism; no point in the relative interior of a face of dimension at least two is a section vertex. This is the justification for the edge count, rather than the source's imprecise appeal to strict convexity. The three base projections in a symmetry sector are c,-a,-b with 0<a<b<c. As h cot(theta) runs through the four intervals cut by a,b,c, the nine-edge count is 4,5,4,3. The independent uniform height coordinate z=|cos(theta)| makes the threshold CDF x/sqrt(h^2+x^2). Integrating on 0<phi<pi/6 gives the stated inverse-sine law. The derivative of the pentagon probability has the sign of 1-q(h) for the stated q, with q'(h)>0 and q going from 0 to sqrt(3)-1/2>1, proving a unique global maximum. Taylor expansions at zero and infinity give the stated coefficients. Fresh bisection on [0,1] gave 0.5314695510636116; Simpson quadrature on the azimuthal pentagon integral with 1024, 2048 and 4096 subintervals gave 0.38515580567415336, 0.38515580567417518 and 0.38515580567417662. These check the numerics only. The frozen script was inspected, not run.

## originality

FAIL

Two distinct published Resultary records give both the same complete law under the same centered Haar model and the same unique global optimizer. The angular formulas and the inverse-sine formulas are exactly equivalent. The thin/long limits follow by Taylor expansion of those already covered exact functions, and the height/edge ratio is a change of scale. This is an equivalent-coverage decision, not an attribution of provenance or an inference from dates alone.

## value

PASS

A complete centered section law for a natural one-parameter family and a unique aspect ratio maximizing pentagons are meaningful geometric results; in particular the optimum is separated from the equal-edge prism. The duplication is an originality failure, and the residual Taylor expansions do not warrant a standalone repaired finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
