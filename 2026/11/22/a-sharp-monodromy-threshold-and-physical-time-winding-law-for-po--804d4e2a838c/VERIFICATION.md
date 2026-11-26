---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For a,b,c>0 and integer k≥1, the polar identities give r=(r₀^(−2k)+2kat)^(−1/(2k)) and θ̇=br²sin²θ+cr⁴. The decreasing radius gives stability, attraction and forward completeness. At k=1, in s=log(r^(−2)), θ′=A sin²θ+B e^(−s). For any sufficiently late crossing of nπ, the barrier (n+1)π−L/(s−s₀+D), L=1/(2A), starts strictly above θ and has derivative exceeding the right-hand side there: the sine term uses at most half the derivative, and the exponential uses less than half uniformly for s≥s₀. Thus θ is bounded and its increasing limit must lie in πℤ. At k≥2, ∫r⁴dt diverges, including the logarithmic case k=2. At fixed radius q, substitution of tan θ on a quadrant gives the full-turn time 2π/[q³√(c(b+cq²))]. On a physical interval of length Mq^(−3), the radius stays within relative O(q^(2k−3)) of q. Taking M>2π/√(bc), comparison with the angular speeds at the two endpoint radii first bounds the actual turn within that interval and then sandwiches its duration. Consequently r^(−(2k−3)) increases by 2π(2k−3)a/√(bc)+o(1) each turn. Summing and using monotonicity between crossings gives the exact limit for the real-valued N(t). For k=2 and a=b=c=1 this gives N∼t^(1/4)/(π√2), hence t_n∼4π⁴n⁴. All assertions apply to any fixed nonzero initial point, not just a trajectory at a particular phase.

## originality

PASS

The resolved sources share tools and the angular degeneracy motivation but do not supply the joint finite/infinite winding classification and leading physical-time asymptotic for this shrinking family. The indexed exact match is the frozen record itself. A related distinct catalogue record was compared on substance, without inferring order from its date.

## value

PASS

This family is a controlled comparison: positive off-origin angular speed and global attraction persist while changing just radial order switches the existence of characteristic rays. It gives a sharp counterexample to using pointwise angular positivity as a winding test, and a quantitative benchmark in physical time including the exact leading coefficient and quartic revolution times. The contribution is the coupled classification and timing, not the polar algebra or a claim about arbitrary analytic singularities.

The dated certificate retains the supplied scientific assessment, sources and limitations.
