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

The change u=y-x, w=2az-x^2 is nonsingular for a>0 and gives u'=-(a+gamma*z)u-beta*y*w, w'=-2aw+2ayu. In E=a*u^2+beta*w^2/2 the cross terms cancel. Variation of constants in z'+2az=y^2 gives z>=-Z_- exp(-2at) for all times of existence, so E'<=(-2a+2gamma*Z_- exp(-2at))E and integration gives the stated bound, also valid on the stationary locus E=0. Finite-time bounds on u,w and the integral of x'=au bound all original coordinates, giving forward completeness. The integrable exponential bound on x' gives a single limiting s and the stated tail bound; the formulas for y,z transfer the rate. The convergence is uniform on compact sets of initial states, so the limit is a continuous retraction, invariant along forward trajectories. Bounded convergence proves support on the closed equilibrium parabola for invariant probabilities. For a compact invariant set, invariance means equality under every forward map, not merely positive invariance: preimages in the compact set and the uniform energy estimate force zero energy. The normal matrix has trace -3a-gamma*s^2/(2a) and determinant 2a^2+(2a*beta+gamma)s^2, giving strict normal attraction at gamma>=0 and a transverse eigenvalue with positive real part if gamma<0 and s^2>6a^2/(-gamma). This is not a classification of negative-coupling nonlinear dynamics. `python /workspace/review_replay.py 2` independently replayed the exact energy derivative and the two spectral invariants from the stated vector field.

## originality

PASS

The supported new part is global, quantitative convergence for arbitrary positive mixed coupling on the balanced parabola surface, including negative initial height and the resulting complete recurrence/measure conclusions in that regime. Neither the zero-coupling case, the parabola itself, nor the normal spectral threshold is credited as independently new.

## value

PASS

Keeping an entire positive coupling ray on the equilibrium surface, rather than setting the mixed coupling to zero, addresses a natural constraint of the original cubic family. The height estimate treats a sign-indefinite transient and proves all-state convergence, selected phase and absence of compact recurrent motion. This extends the global theorem, not just a local trace computation; the known negative sign boundary appropriately limits the claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
