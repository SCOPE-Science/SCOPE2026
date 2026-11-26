---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The theorem as stated in Finding is correct after independent analytic reconstruction; the frozen proof itself has an error at RESULT.md lines 43 and 49. Conditional on z=|n_z|, which is uniform and independent of the projective azimuth, each visit covers an open arc centered at quadrature. A gap g leaves length [g-2b_t(z)]_+ uncovered, including repeated visits represented by zero gaps. Jensen proves optimality. Zero miss occurs exactly when every gap is at most 2 arccos(t), because a larger gap gives positive miss on an interval of z of positive length. For t>=c_m, any nonconstant gap vector has a max strictly larger than both the mean and 2 arccos(t); choose 2b_t(z) strictly between max(min gap,2 arccos(t)) and max gap, giving strict Jensen on a positive-length interval. For the edge put gamma=pi/(2m), s=sin(gamma), c=cos(gamma), delta=t-c. The correct expansion is 2(gamma-b_t(z))=2 delta/s-(s/c) z^2+O_m(delta^2+delta z^2+z^4), not (2 delta-s z^2)/c. The exact positive support ends at sqrt(t^2-c^2)/s. Integration to its leading endpoint sqrt(2c delta)/s gives K_m=4m sqrt(2c)/(3 pi s^2); the integrated remainder is O_m(delta^(5/2)), including the endpoint replacement. Thus the coefficient in Finding is correct although the displayed intermediate calculation is not. The visit-count ceiling also holds for m=2 by the same gap argument. 'Guarantee' here is probability one, not pointwise over all geometries: at the threshold there are edge-on, equality configurations, and one visit at t=0 also fails for a null set. A bounded independent Simpson check gave 0.10286909015 and 0.19408187233 at t=0.92 for the two stated schedules; for m=3 the edge ratios at delta=0.001, 0.0001, 0.00001 were 6.72408, 6.70484, 6.70292 versus exact K_3 about 6.70271. The packaged diagnostic was inspected, not run; it integrates the claimed formula rather than independently deriving it.

## originality

FAIL

A separate same-day indexed record gives the same substantive scheduling result: inner-working-angle-only circular-orbit completeness, global equal spacing for every count at least three, a sharp completeness threshold with rigid versus nonrigid phases, an exact completeness law, and the sharp visit count. The earlier two-visit record already exhibits the same 3/2 onset mechanism. The additional displayed coefficient is obtained by expanding the equal-spacing completeness law, not a separately established distinct scheduling result. The available evidence does not establish a material original increment for this combined claim. This is not an assertion of chronological priority, nor that the same-day abstract states the coefficient or all the same assumptions; the abstract's direction of the threshold comparison is ambiguous and its full text was inaccessible. The decision rests on the positive indexed overlap and mathematical implication of an exact law for the same model, not on the retrieval failure alone.

## value

PASS

As a mathematical target, exact optimal schedules, the equality regimes, and the onset of miss probability give a useful benchmark for correlated visits; miss probabilities cannot generally be multiplied as though visits were independent. The benchmark says how geometric completeness degrades just past the threshold and is not an instrument or mission-performance recommendation. This value judgment does not confer originality on the frozen record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
