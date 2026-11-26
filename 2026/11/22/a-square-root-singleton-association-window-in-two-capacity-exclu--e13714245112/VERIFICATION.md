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

On fixed mass the incoming-minus-outgoing flux relative to the proposed product weight is h(c)−h(b) for a rightward directed pair; checking the nine pairs gives h=(0,1+t,(1+t)²), hence telescoping around the ring, and reversal gives the same balance for left hops. Right-hop rates are positive on every allowed right transfer; the underlying undirected transfer graph is connected at fixed mass and the positive stationary law rules out transient classes, giving uniqueness also at q=0. The fixed-mass fugacity gauge gives the symmetric three-point law conditioned on sum d=N−L. Requiring one or two zero increments gives the exact probability ratios and determinant. At d=0, the nonnegative, nonconstant characteristic function supplies strict Cauchy–Schwarz for consecutive moments, giving positive pair covariance and increasing conditional probabilities; fixed sum and exchangeability give the opposite sign for ordinary occupations. This is pairwise covariance and conditional singleton monotonicity, not a full multivariate association claim. For d/√L→c, symmetrizing the determinant before expansion retains the exact squared characteristic-function difference. To justify domination explicitly, φ(θ)≤exp(−4pθ²/π²) on [−π,π], and after scaling L times the difference is bounded by p(u²+v²). The tilted Gaussian second-square variance is 1/(2p²)−c²/(2p³), giving L² times the covariance equal in the limit to a²(1−c²/p)/2. The ordinary variance tends to 2p. Uniform slot counting at t=1 gives the two hypergeometric singleton probabilities, whose difference factors as stated; the extreme masses have deterministic indicators. Numerical coefficient propagation independently checked both signs (e.g. at w=2.5 and L=2000, scaled covariances are 0.154524 at d=0 and −0.247380 at d=34, compared with leading terms 0.154321 and −0.247068). Uploaded check.py and VERIFICATION.md were inspected, not executed. No sign is determined on the limiting boundary, nor an all-density finite threshold for general t.

## originality

PASS

The supported distinct result is the sharp deformation-dependent mesoscopic covariance profile and resulting square-root sign window. The stationary product law is prior. The half-filled sign and conditional monotonicity already follow from established generalized central trinomial moment theory after the canonical identification, and the exact t=1 expression is a direct consequence of the established binomial canonical model. These components are credited, not independently counted as new. No inspected source implies the off-center, general-deformation sign profile from those components.

## value

PASS

The singleton event is a natural local but nonmonotone observable. Its much smaller correlation scale and sharp general-deformation density crossover separate it from ordinary occupation correlations forced by particle conservation. The exact profile controls the sign on both sides of a natural fluctuation-scale boundary, rather than just evaluating a finite case. The result is equal-time and makes no transport or dynamical association claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
