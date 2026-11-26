---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For R=1 the horizontal chord cut from the square of half-width sqrt(1-z²) changes at c|z|=(a±b)sqrt(1-z²). The Jacobian is 1/sqrt(a²+b²); the algebraic terms at the two thresholds cancel, yielding the inverse-tangent formula and its stated axis limits. At fixed c the area is four times the centered interval mean of a strictly convex derivative; pairing symmetric points shows strict increase with the interval radius 2ab, including the integrable c=0 limit. The sign of D' is the sign of g; differentiating arctan x−3x/(x²+3) proves g'>0, and the limits −4 and 4/3 prove one strict profile minimum and the maximum at k=0. Inclusion of the ball proves the lower bound, with strict excess in every other plane by an open set of radial directions with xy≠0. Independently split polar quadrature at the active-cylinder switch for seven normals, including coordinate boundaries, agreed with the formula to 10⁻⁴⁷ at 50-digit precision; the stationary value was independently 3.8203968413887654300 at k=1.3201367133766767181. This is numerical corroboration only; the universal check is RESULT.md lines 40–96. Frozen verify.py lines 13–80 and VERIFICATION.md describe a separate finite quadrature check; the source script was inspected, not executed.

## originality

FAIL

A distinct earlier indexed Resultary record states the full central theorem: the same solid, elementary area formula on all central orientations and boundaries, sharp values and equality normals, strict fixed-c balancing, and the one-minimum diagonal profile. It additionally treats affine maxima. This is demonstrably already covered in the catalogue, not inferred from a title or a failed retrieval. The date/relationship does not settle ultimate historical priority or authorship.

## value

FAIL

The angular profile and equality classification are worthwhile geometric invariants in isolation, but the frozen submission adds no distinct invariant, improvement, or demonstrated independently useful proof contribution beyond the exact, broader catalogue treatment. No surviving narrowed claim is identified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
