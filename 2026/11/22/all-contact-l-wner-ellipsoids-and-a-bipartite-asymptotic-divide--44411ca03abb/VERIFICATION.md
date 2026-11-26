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

The contact measure has uniform marginals. On the centered affine directions (the covariance formulas with A/k are restricted to 1-perp), the adjacency has eigenvalues −s on class contrasts and 0 on within-class contrasts. Orthogonal sum/difference coordinates yield the four stated positive eigenvalues and certify full dimension. For an ordered edge the two within-class projected components are supported in different classes, giving r(s−1)/N in each sign; the class-constant components give (r−2)/N and r/N. For a diagonal the U components double and V vanishes. These reproduce both inverse-covariance norms. Independently factored the cleared contact numerator as −2 times the stated quadratic and reproduced the exact factorization of F at the uniform mass. F decreases from 2(r−1)/(r−2) to −∞, so the unique contact mass lies strictly inside (0,1). The covariance trace forces both orbit gauges to be d; strict convexity excludes all other contacts. Averaging containment proves the trace/determinant bound and its strict equality condition even with unrestricted competitor centers. All vertices have squared distance d/N, and the same mean certificate proves ball optimality. The determinant ratio and p~(r−1)/(r(r−2)s) give the positive fixed-r limit; the bipartite substitution yields √2 exp(−1/4) s^(−1/4). The advertised checker was not included among the frozen files; VERIFICATION.md reports it, but the audited proof and independently reconstructed symbolic identities do not rely on it.

## originality

PASS

The supported distinct result is the explicit all-contact outer ellipsoid for balanced PQ multipartitions with r≥3, the s=2 threshold for uniform weighting and the fixed-r asymptotic. Earlier bipartite and star formulas and the classical determinant certificate are not new; none of the inspected statements covers the r≥3 answer.

## value

PASS

Equal-size multipartitions are a natural extension of the bipartite geometry. The explicit optimal design resolves whether a uniform vertex covariance suffices and evaluates the distortion in volume from using the minimal containing ball. The change from a vanishing ratio to a strictly positive limit for each fixed r≥3 is a qualitative boundary rather than a cosmetic change of parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
