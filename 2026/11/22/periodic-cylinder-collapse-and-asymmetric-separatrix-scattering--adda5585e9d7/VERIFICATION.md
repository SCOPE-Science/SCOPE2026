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

On the stated autonomous boundary a=c=0, the coercive quartic energy confines the planar variables; the height derivative is bounded on each energy level, so the full flow is complete. In-well cycles and well equilibria have fixed nonzero sign of x and cannot give bounded lifts. On above-barrier ovals the central symmetry is a half-period shift. Pairing the shifts gives 2α times the half-period integral of x sinh(βx), strictly signed for β≠0 and zero at β=0. Thus the lifts drift linearly plus a bounded periodic term except at β=0, where each above-barrier energy has a cylinder of periodic lifts. Differentiating ±A sech(kt) gives the zero-energy separatrices, with integrable height derivatives. The substitution v=sech(kt) on each half gives J and the stated signed, nonzero displacements. Setting w=1−v in J(s) yields the endpoint factor √(2π/s)e^s, whereas J(−s) is dominated by v=0 and is asymptotic to 2/s. The only recurrent points are the equilibrium line and, at β=0, the periodic lifts; recurrence for a probability excludes the other orbits. On the periodic region at β=0, label a circle by energy and height at the unique x=0,y>0 crossing per period; conditional invariant measures on these circles are uniform in time. For the limiting return displacements, u=x² cancels the factor x in the half-well travel-time integral. Its density is proportional to [(u_+−u)(u−u_−)]^(−1/2), with u_+→A² and u_−→0; for E<0 an affine rescaling fixes the arcsine density, and for E>0 u_−<0 gives integrable arcsine domination after scaling u by u_+. Counting both legs gives exactly the claimed individual or summed limiting displacements. These are analytic checks against RESULT.md lines 11–53. The supplied standard-library numerical checker and VERIFICATION.md were read, not executed; finite quadrature is not used to certify any global claim.

## originality

PASS

Pass is for the exact autonomous-boundary full-flow census and the signed separatrix scattering laws, not the Duffing phase portrait or the general return-drift test. The nearest distinct available records overlap in model or method, but do not supply that combined specialized claim. The exact conservative-boundary result referred to by a same-day record may refer to this finding; neither identity nor priority follows from that reference.

## value

PASS

The no-damping/no-forcing slice is the natural integrable boundary of the published model, not an arbitrary sample. Periodicity of planar projections there conceals loss of recurrence in the actual full variables; the exact census answers which bounded or recurrent motions really survive. The branch-specific transition data and unequal large-weight scales are useful beyond the generic return-drift test. No extrapolation to the damped, forced or chaotic setting is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
