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

The 14 halfspaces characterize the Voronoi cell: for half-integral lattice points the cube bound controls integer parts and the l1 bound controls half-unit parts; the axial bound alone controls integral points. Any vertex is on a cube facet (the l1 ball's own vertices violate the cube), and each such facet is a diamond whose corners yield the 24 signed permutations of (1/2,1/4,0). The common squared norm is 5/16, the minimum squared separation is 1/8, and the covolume is 1/2. The equal-radius convex-combination identity forces a point of deficit below 1/64 into a disjoint radius-1/8 vertex ball where only three planes constrain membership. The cone coordinates have Jacobian 16 and deficit t-8Ht^2, with 1/10<=H<=1; its smaller root lies below 2 epsilon and within the ball, while the other root is at least 1/16 and cannot contribute inside the ball. The volume multiplier is 24 times (16/3) divided by 1/2. Lagrange inversion for t=epsilon/(1-8Ht) gives the coefficient formula, uniformly integrable on the displayed range. Integrating the monomials by factorial ratios gives the first three moments of H and the stated coefficients; the positive lower bound on H ensures positivity at all orders. Independence and the leading cubic term give the sample maximum law. In the replacement, the comparison with Luo is normalized by E[||X||^p]=2^(-p/3)E_p(A_bcc); the even moments of the independent radial-factor representation agree exactly, including total mass. Conditional integration of the radial factor gives the credited global survival quadrature.

## originality

PASS

The frozen presentation undercredits Luo's same-cell facet quadrature: it directly gives a global radial law, not only a moment-determinacy assertion. The corrected result claims only the explicit, fixed-simplex endpoint extraction and convergent positive rational coefficient formula. The distribution itself is credited as covered by the global quadrature and the extreme limit is a consequence, not an independent novelty claim.

## value

PASS

The squared-deficit endpoint is a natural quantization-error invariant at a standard lattice. Resolving its support gives a convergent series with explicitly computable rational coefficients and a positive, calibrated leading constant, information that is not furnished by global moment optimization or by the unevaluated shrinking-domain quadrature. This permits high-order near-worst-case comparisons at fixed covolume, and the same leading coefficient sets the law for sample maximum error. The contribution is that local extraction, not a second identification of the entire law or an optimization theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
