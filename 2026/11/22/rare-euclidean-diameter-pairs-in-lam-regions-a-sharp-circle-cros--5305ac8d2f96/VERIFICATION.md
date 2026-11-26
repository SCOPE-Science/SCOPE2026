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

For each fixed 0<p<2 the Euclidean unit disk contains the Lamé region, with equality on its boundary only at the four axial tips, including for p<1. The distance deficit bounds the sum of the radial deficits, which control the axial deficits near the tips because transverse squares are o(axial deficit). Thus after localizing to each of four ordered opposing tip pairs, axial scales ε and transverse scales ε^(1/p) give a compact scaled domain. Integrating the transverse widths over U+W<1 gives the stated gamma quotient, Dirichlet law and conditional uniform marks. For p=2−λε with fixed λ, the uniform radial expansion is 1−λεH+O(ε²); near-diameter pairs have both radial deficits O(ε) and antipodal offset O(√ε). The polar Jacobian gives ε^(5/2) and the section a+b+z²/4<c has volume (16/15)c^(5/2). This proves both the integral and marked law, including the disk value 32/(15π). Entropy maximizes at the diagonals with H=log(2)/4; at equality only the four exact diagonals have zero density. As λ tends to infinity separately, the monotone axial region has width of order √(2/(λ log λ)); on that scale 2λH tends to s² and its support is uniformly bounded. Integrating (1−s²)^(5/2) and including four axes gives 4√2/(3π). The captured six Sobol ratios lie between 0.9880 and 1.0016; CHECK.py was inspected, not executed, and those finite diagnostics do not prove the asymptotic.

## originality

PASS

Passes for the area-uniform fixed-shape and moving-shape pair laws, including their radial/axial marks and constants. The disk value and the entropy penalty, cutoff mechanism and logarithmic angular scale viewed without the area sampling are not distinct novelty. The strongest same-day arclength comparison actually includes both signs of its shape parameter, including this record's below-circle regime.

## value

PASS

Uniform area is the natural interior model. The isolated-tip and near-circle limits quantify how loss of a continuum of diameter directions changes both probability and where the successful interior points sit. Exact coefficients and marked laws distinguish the geometry from the corresponding boundary sampling and from quadratic anisotropy; no uniform joint large-λ claim is credited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
