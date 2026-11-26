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

Central symmetry gives W=2h. The radius-a ball is included, and au for U_z≠0 strictly satisfies both cylinder inequalities, so all and only equatorial directions minimize. For (x,y) in the smaller disk, the z contribution is |s|sqrt(b²−y²). Its Lipschitz perturbation of the objective at the equatorial optimizer av is bounded by L|s||q−av|, against a support loss at least sqrt(1−s²)|q−av|²/(2a). Completing the square gives h=a+|s|g(θ)+O_{a,b}(s²) uniformly. Compact separation off the equator and min g>0 imply |s|=O(ε); the event and the strip |s|≤ε/(2g) differ in spherical measure by O(ε²). Integrating dθ ds/(4π) establishes the claimed slope; on that strip the mark change of variables gives the product law with azimuth proportional to 1/g. The slope is strictly decreasing from infinity to zero at fixed a by its positive integral expression, which also verifies the inverse. The stated equal-radius comparator agrees with maximizing (|u_x|+|u_z|)sqrt(a²−y²)+u_y y and the small-product log law localized near ±e_y.

## originality

PASS

The distinct contribution is the fixed unequal-radii probability asymptotic with its elliptic coefficient, marked conditional limit, and recovery from endpoint and slope. Closest indexed laws concern the equal-radius degeneration or central chords, and the other inspected primary geometric formulas concern a different functional.

## value

PASS

Random line projections are a natural way to observe the body without choosing its orientation. The degenerate minimum is a whole circle, so ordinary isolated-minimum approximations do not describe the marked localization. The exact finite slope distinguishes two radii from an endpoint alone and separates this regime from the singular equal-radius case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
