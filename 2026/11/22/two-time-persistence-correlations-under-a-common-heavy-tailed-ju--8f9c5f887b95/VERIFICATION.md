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

Conditioning on the common integrated rate gives the product of the two killed-walk survival curves. Reflection makes q_x(a) a sum of 2x unrestricted heat masses, giving q_x(a)∼x√(2/πa) at unit total rate. With b_t=τ^{1−1/α}t^{1/α}, the disjoint complete periods before and after t give the joint clock transform exp(−(u+v)^α−(c−1)v^α); at most two partial periods vanish in probability under this normalization. The negative p moment of the normalized complete sum, N=floor(t/τ)>p/α, is (t/τ)^{p/α} B(p/α,N−p/α)/(αΓ(p)), bounded and convergent by the gamma ratio. The uniform bound for p>1 controls the scaled product in L^p since A_ct≥A_t. This justifies the positive limiting mixed moment and separately the marginals. In the double Mellin integral use u+v=w and v/w=cos²θ; the radial integral is Γ(1/α)/α times the stated angular weight, and the angular Jacobian contributes the factor 2. The independent product is M_α(1/2)^2 c^{−1/(2α)}. Strict covariance follows from the independent-copy identity for two strictly decreasing functions of the nondegenerate S₁. For c≥2 couple S_c/c^{1/α}=c^{−1/α}S₁+((c−1)/c)^{1/α}S′ with S′ independent; the normalized mixed integrand is dominated by 2^{1/(2α)}(S₁ S′)^{−1/2}, integrable, and tends to the independent integrand. For α=1 the stable clock is deterministic. At α=1/2,c=2 the half-angle substitution reduces the angular integral to ∫₀¹(1+z²)dz=4/3 with prefactor one; equal time gives π/2. No claim of monotonicity in c is used.

## originality

PASS

Credit the single-walker clock and survival results, standard stable Mellin tools and the acknowledged equal-time overlap. The supported distinct result is the unequal-observation-time two-walker joint asymptotic and dependent-clock enhancement curve, including the exact double-time ratio. The strongest inspected single-walker and stable-product statements do not imply this curve.

## value

PASS

Identical one-walker marginals cannot tell whether rate histories are shared. The full unequal-time comparison provides an exact dependence signature with strict enhancement at every finite ratio for α<1, a clean double-time benchmark, and a proved decorrelation limit. This is more than a new evaluation at a selected point, and avoids promising finite-time or monotonic behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
