---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

Reconstructed facet area*support normalization: each ±coordinate pair yields log cosh(z_i), and |det A|=1 gives affine covariance. Setting g(u)=log cosh(sqrt u), direct derivative g<0 yields Jensen maximal on equal squared coordinates and subadditive lower bound attained at one coordinate. Sharp inner and outer Euclidean radii and complete contacts follow. Signed-coordinate permutations force both unique extremal ellipsoids to be balls; averaging candidate quadratic forms proves no noninvariant ellipsoid improves Banach–Mazur ratio. The inverse-square radius h(s)=arcosh(e^s)^2 is strictly convex, and its increasing elasticity yields monotonicity; elementary asymptotics give endpoint/dimension limits. Independently recomputed derivative signs and checked values; numerical verifications not universal proofs.

## originality

PASS

PASS, qualified. The 2026 source smooth-covariogram theorem gives the critical logcosh Orlicz functional, its normalization, and limiting bodies, not the exact ellipsoids, full contacts, BM metric, and level/dimension profile for all volume-one parallelotopes. A previously published triangle case has different facet structure. General Orlicz projection-body and symmetric unconditional norm results provide methods but no inspected theorem with the complete exact formulas for this logcosh modular.

## value

PASS

PASS. This is a natural all-dimensional affine class and an exact one-parameter family of canonical transition Orlicz bodies, not an ad hoc slice. The complete ellipsoid-and-contact classification, sharp BM distance and strict level/dimension profile quantify crossover from Euclidean to ℓ1 geometry; the bounded high-d fixed-level limit is a motivated structural invariant beyond an individual numeric evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
