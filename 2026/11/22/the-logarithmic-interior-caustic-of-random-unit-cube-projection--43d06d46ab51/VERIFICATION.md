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

The projected generator lengths are sqrt(1−n_i²), and planar zonotope perimeter is twice their sum by additivity of widths. Strict concavity on the squared-coordinate simplex gives the six axis minima and eight diagonal maxima. For fixed z=|n_3|, the folded azimuth is uniform on [0,π/2]. Squaring the sum of the two variable radicals gives 1+z²+2 sqrt(z²+(1−z²)² sin²(2β)/4), which is increasing on the half-interval. Solving the threshold yields the stated radicand, and the two azimuth pieces give angular measure arcsin(sqrt(R)), so integrating their conditional probability over uniform z gives the unconditional CDF. The level z=1 is null. Away from the axes the Lagrange multiplier equation forces equal nonzero absolute coordinates. At the twelve saddles the tangent Hessian is diag(−2√2,2(√2−1)), obtained by subtracting the normal multiplier from the ambient diagonal Hessian; at each maximum it is −sqrt(3/2) times the identity. After Morse rescaling a saddle gives quadratic form x²−y² with weight at zero (4π sqrt(2−√2))^(−1). In u=x+y,v=x−y the Jacobian 1/2 cancels the two signs in the logarithmic integral, giving log(1/|p−p_*|) with unit coefficient; a smooth weight minus its value at zero is O(|u|+|v|), whose pushforward is bounded locally. Summing over twelve saddles gives the stated coefficient on both sides. Compact regular preimages give a smooth density, and the isolated critical directions carry no mass. At an axis, tangent radius r gives P−4=2r+O(r²), so six disks of radius ε/2+O(ε²) give 3ε²/8. At a diagonal the quadratic deficit is (√6/4)r², so eight disks give 4 sqrt(2/3) ε+o(ε). The use of full-sphere 1/(4π) throughout avoids a sign-quotient factor error; rescaling lengths divides the density coefficient by side length.

## originality

PASS

The supported distinct claim is the cube projection's exact interior singularity and calibrated endpoint laws. The projected-perimeter identity and moments are prior. The elementary azimuth CDF reduction is verified, but no priority is asserted for quadrature independent of the sharp asymptotics. Vickers–Brown is materially relevant and its inaccessible detailed cuboid treatment leaves a priority risk; its inspected abstract is not a negative finding about the full paper.

## value

PASS

The random orthogonal perimeter of a unit cube is a natural projection statistic with known moments but nontrivial distribution shape. An explicit unique interior logarithmic divergence and distinct sharp endpoint probability scales quantify phenomena moments or a smoothed histogram cannot resolve. The exact coefficients, together with a one-dimensional CDF, are useful calibration and numerical benchmarks for projection distributions; the value is not the already-known zonotope perimeter identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
