---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the stated weighted Laplacian, the uniform-cycle inverse sends e_0-e_4 to an antisymmetric vector with amplitudes (x+2)/Q and 1/Q on A and B, and zero on C. The rank-one Downdate denominator is D/Q>0; this gives the three stated diagonals and strict A>B>C diagonal ordering. The trace gain is the negative log derivative of the diagonal. Independently setting N=(x^2+3x+1)D and d=1-w gives G_B/G_C=1+dx/N and G_A/G_C=1+(x+2)^2 dx/N. Expanding the derivatives recovers the stated polynomials as F=xN'-N and J=((x+2)^2-1)F-2(x+2)x(N+dx). F increases from a negative constant and J has one coefficient sign change and opposite endpoint signs. At the B=C score crossing, (dx/N)'=0 but the A-to-C diagonal ratio is increasing, so R_A<R_B=R_C; hence that crossing comes strictly before the A=B crossing. This proves the whole minimizer and tie classification. I verified both rational root brackets at w=1/2. Three- and four-cycles with one exceptional edge have at most two reflection orbits; no broader minimality is implied. RESULT.md, proof steps 1–5, is a replay path; the supplied script was inspected, not executed.

## originality

PASS

Trace/determinant disagreement and screening-driven migration are already known in other graph families. The supported distinctive claim is the exact three-orbit, two-boundary singleton classification for every weak-edge weight on the five-cycle, together with its fixed determinant optimum. No stronger covering statement was established in the inspected sources.

## value

PASS

The smallest defective cycle family member with three candidate orbits gives a natural model for a local conductance perturbation. The exact and universal two-threshold law is useful beyond exhibiting generic design-objective disagreement: it identifies every screening interval and both tie sets where a one-landmark choice changes even though marginal-variance ordering does not. The claim is limited to noiseless singleton observations and the specified weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
