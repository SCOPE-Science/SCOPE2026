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

The commutator has triangular kernel (b(x)-b(t))/x, square integrable by the Lipschitz bound, so its squared Hilbert–Schmidt norm is the kernel integral without any additional factor. The ramp functions meet continuously at both breakpoints and have the required pinned endpoints. Integrating the affine differences on the three intervals gives the displayed logarithmic expression, including its continuous a=0 value and the opposite-sign tent at a=1/2. Differentiation gives E'''=-4(4a²+4a-1)/(a(2a+1)^3), so E'' first rises from minus infinity and then decreases to its positive right-end value. It crosses zero exactly once. Thus E' first decreases then increases; the positive endpoint signs and the opposite signs at 1/100 and 1/64 prove exactly two critical points, the first a strict maximum, the second a minimum. Since the two endpoint energies coincide and E initially increases, the first point is the unique maximum within the family. An independently written bounded calculation used range reduction and exact rational atanh-series remainder bounds to reproduce all four derivative signs, the positive right-end curvature, and the strict witness bound E(1/64)-E(0)>0.00054767456646. This last inequality rules out the tent even in the full admissible class without finding the unrestricted optimizer.

## originality

PASS

The supported distinction is a strict exact counterexample to tent optimality for the endpoint-pinned Hilbert–Schmidt problem and the exact three-ramp optimization supporting it. The leading prior overlaps are the same Hardy commutator with a different symbol family, and related Cesàro commutator spectral results with a different kernel or objective. They establish context but do not supply this signed pinned witness or the one-parameter maximum.

## value

PASS

The tent is the natural pointwise upper envelope for nonnegative pinned unit-Lipschitz profiles. The strict witness shows that this pointwise argument fails for a genuinely two-point, directionally weighted commutator energy. The gain is not an optimization tolerance or an unmotivated tiny perturbation: the positive one-sided derivative at the tent gives a robust strict improvement by adding the boundary ramp, while the other critical point and right-end behavior show how the orientation matters within the family. This is an exact counterexample relevant to the larger extremal question, with a precise limited optimum rather than a claim to have solved the full problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
