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

Central symmetry lets an inscribed disk be centered at zero, and projection of the coordinate normals to the plane makes the inradius (1-z^2)^(-1/2), z=min_i|U_i|. With a>=b>=z, strict a<b+z is exactly the hexagon criterion: all three pairs of cube faces then meet the plane in segments through their relative interiors. If a>b+z the largest-coordinate faces miss the plane and the other pairs give four edges. The tied generic boundary has zero Haar mass. On one sign/order chamber parametrize the other two components as sqrt(1-z^2)(cos t,sin t); the area element is dz dt and t ranges from theta(z) to pi/4. The six-edge subinterval begins at max(theta, pi/4-phi); the crossover a=2z,b=z is z=1/sqrt(6). The 48 sectors have normalization 12/pi times their angular lengths, giving both subdensities and no atoms. Direct differentiation gives the stated Jacobian in R. If z>1/sqrt(6), a>=b+z would force 1>=6 z^2, impossible, so the all-direction claim holds even for nongeneric normals. At (a,b,z)=(2,1,1)/sqrt(6) the largest-coordinate pair meets only at two opposite vertices and the other pairs supply four edges, giving the sharp bound. The conditional probability is strictly increasing below the cutoff, then constant one, not strictly increasing on the whole support. The claimed strict association still follows: for any nondecreasing g not essentially constant, a level separating values on positive-measure lower and upper sets permits pairs with the lower radius also below the cutoff. Both differences in the independent-copy covariance product are then strictly positive on a positive-measure set. The finite clipping/quadrature checker was inspected but not run or treated as a continuum proof.

## originality

FAIL

The distinct indexed two-radius result 9f3bd844588d establishes the exact Haar density in the minimum-coordinate/inradius coordinate and angular variable, and establishes the two angular branches and their exact cut point. The same proof identifies the branches with the quadrilateral and hexagonal geometries. Integrating its joint angle density over those two already determined intervals and changing variables gives exactly the frozen type subdensities, conditional probability, and cutoff. The additional monotonicity and positive association are immediate consequences of this probability formula. This is demonstrated same-object mathematical coverage, not a conclusion based on either marginal alone. The catalogue lists both records on the same day, so no historical order is inferred.

## value

FAIL

The relationship between a metric invariant and the combinatorial type is a natural question. Here the prior-compared orientation density, type boundary and crossover already supply the full exact answer by interval lengths. The additional strict association is a routine monotone-function consequence, not a further independent geometric phenomenon at this scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
