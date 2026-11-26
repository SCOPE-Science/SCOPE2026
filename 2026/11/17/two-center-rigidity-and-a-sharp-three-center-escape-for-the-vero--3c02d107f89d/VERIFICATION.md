---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For nonzero traceless A, find a unit A-isotropic vector by indefiniteness and rotate an eigenbasis of its traceless two-dimensional compression by 45 degrees. This gives an entire A-isotropic orthonormal basis. The B-values on that basis sum to zero. The projective A-null locus is connected: for signature (2,1) or (1,2), taking the lone-sign coordinate to 1 gives an ellipse, while for rank two it is the union of two intersecting projective lines. Thus the B-values give a common zero, also immediate if A=0. At this point the two squared distances are exactly 1/3+||C_j||_F^2 because ||p(u)||_F^2=1/3 and the cross terms vanish. Zero alone covers, proving the first two radii and giving exactly the optimizer pairs containing zero. For the three planar axes spaced by 60 degrees, the perpendicular axes are also spaced by 60 degrees modulo 180, so every nonzero planar projection is within 30 degrees of some perpendicular axis. This gives min_j (u·v_j)^2≤1/4, also for zero projection, with equality on the chosen axes. The projector product is ((u·v)^2−1/3)/2 and the squared distance to −p(v)/8 is 1/3+1/192+((u·v)^2−1/3)/8. Its nearest-center maximum is 21/64, less than 1/3 by 1/192. The translated center corresponds to the trace-one matrix (3I−vvᵀ)/8 with positive eigenvalues 1/4, 3/8, 3/8. Spectral decomposition identifies the convex body as the translated trace-one PSD set, so these centers are interior. This is the exact radius of this configuration only, not of optimal three-coverings. The frozen numerical checks are corroborative and were not used for universal conclusions.

## originality

PASS

The classical joint-range theorem already supplies the key common-zero lemma and directly implies the two-center conclusions after the distance calculation. Credit that part as an application, not a novel quadratic-form result. The distinct contribution is the exact critical count for strict improvement on this normalized surface, with the explicit, contact-attaining three-ball configuration. The inspected equal-diameter obstruction concerns a lower radius and does not establish this result.

## value

PASS

The embedded projective plane is already a natural extremal equal-ball example. Finding its first improvable ball count identifies a qualitative feature of the radius profile, not merely a small numeric gain. The exact contact value of an explicit interior-center triple, together with the degenerate optimizer locus at two centers, gives a benchmark for the next optimization problem without claiming to solve it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
