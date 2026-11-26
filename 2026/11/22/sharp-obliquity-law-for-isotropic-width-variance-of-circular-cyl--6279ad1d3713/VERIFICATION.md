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

Independently checked the second moment and slope constants in RESULT.md lines 32–100. Width adds under Minkowski sums, giving 2r√(1−U₃²)+ℓ|v·U|. The uniform law of U₃ and spherical symmetry give the stated mean and the pure-square terms (8r²+ℓ²)/3. For another check of the mixed term, express √(1−U₃²) as π/2 times the azimuthal mean of |e·U| for a unit in-plane direction e. For unit directions with inner product c, angular integration of the two absolute linear projections gives E|e·U||v·U|=2[√(1−c²)+c arcsin c]/(3π): reduce to the plane of the two directions with mean squared projected radius 2/3 and integrate |cos φ cos(φ−arccos c)| over a full turn. Writing c=√m sin φ by symmetry, the remaining quarter-turn average produces F=2/(3π) times the integral of √(1−m sin²φ)+√m sinφ arcsin(√m sinφ). Integration by parts in the arcsine term gives F=2[2E(m)−(1−m)K(m)]/(3π). Differentiation gives F′=(3π)⁻¹∫cos²φ/√(1−m sin²φ)dφ; its endpoint limits are 1/12 and 1/(3π) by domination by cosφ. Variance has slope 4rℓF′ since the mean is constant. The strict increase, sharp secant constants, endpoint gap and inverse statement in m follow, with r and ℓ held fixed and the planar endpoint excluded. Inspected the finite checker without executing it.

## originality

PASS

The supported distinction is the evaluated oblique-cylinder variance profile together with its sharp global slope and inverse law. The mean and upright case are known, and the classical absolute bivariate Gaussian kernel provides a direct alternative starting point for the mixed moment. That prior kernel is partial coverage, not a stated disk–segment elliptic evaluation or quantitative tilt law. The assessment is limited to the available statements and is not a priority certification.

## value

PASS

The known mean cannot distinguish tilt for these fixed lengths, while the variance distinguishes every tilt and does so with sharp quantitative conditioning in sin²θ. The complete exact profile and the planar-limit gap separate the isotropic width statistic from fixed-height or projected-area problems. This is a useful shape-identification result, not merely an elliptic re-expression of the known mean or upright value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
