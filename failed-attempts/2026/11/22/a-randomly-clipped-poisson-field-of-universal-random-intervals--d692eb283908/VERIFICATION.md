---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For an interval to meet every other interval, its left endpoint must be at most the least right endpoint and its right endpoint at least the greatest left endpoint. Including self-comparisons is harmless. On bounded rescaled windows the three corner preimages are disjoint for large n, each with density 2/n under the appropriate two-coordinate map. Taking the n-th power of the single-sample joint Laplace functional therefore gives independent intensity-two Poisson limits. Regard the corner measures as locally finite on the closed quadrant, their limiting intensities supported on their stated wedges or quadrant. The two threshold minima have survival e^(−t²), by the triangular wedge area t²/2; the finite survival formulas give tightness beyond any fixed cutoff. On compact windows, clip the spanning process at the two minima; the independent limiting process almost surely has no points on the moving boundaries. Thus integration against each continuous test function, and mass on the bounded clipped support, are continuous at the limit. This gives joint convergence and the asserted conditional law of the limit, with iid uniform points given its thresholds and count. The mixed-Poisson density integral reduces by s=a+b and v=a/(a+b) to 4·2^k/k! times Γ(k+2)/2 times B(k+2,k+2), giving the displayed mass function and moments. As a separate check, conditional on finite thresholds Q=q<P=p and their attaining indices, neither attaining interval is universal; the other n−2 sorted endpoint pairs are iid in the triangle restricted by r>q and l<p. The universal part is a rectangle of density 2 with probability 2q(1−p)/[1−q²−(1−p)²] under this restriction. At the stated scaling this gives precisely the same conditional Poisson parameter. Replay: apply the inequalities in RESULT.md lines 25–29, the disjoint-window Laplace functional at lines 31–37 and the beta–gamma integral at lines 47–56. The extension uses two iid endpoints per interval and quantile coordinates, not arbitrary within-pair dependence or ordinary Euclidean scaling for nonuniform distributions.

## originality

FAIL

The core marked law is already mathematically covered by the available companion result 9e288e46509a: it proves joint convergence of all three endpoint clouds and identifies exactly the same moving clipping map in the proof of its broader joint theorem. Keeping the clipped points instead of taking their count is an immediate continuous-mapping corollary of the proved input. This is a positive mathematical coverage finding, not failure to retrieve Sarkar, or an assertion of who discovered the result first. The two records have the same displayed publication day and no verified ordering or explicit attribution linking them to one another. No standalone original remainder is established by the count integral or the credited existence probability.

## value

FAIL

A spatial description of full-degree vertices is scientifically meaningful, and would add information to an existence probability or count law alone. As a standalone contribution on top of the available joint three-cloud construction, however, the result has no nonroutine remainder: the locations are its clipped spanning points, the conditional placement is the homogeneous-Poisson placement property, and the count mass and moments are elementary integrations of its already specified conditional parameter. The frozen result supplies no new quantitative rate, different model or further structural invariant that survives this comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
