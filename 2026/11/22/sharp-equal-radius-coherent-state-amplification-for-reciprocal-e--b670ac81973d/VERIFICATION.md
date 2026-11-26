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

The squared monomial norm is πΓ((n+1)/m)/m, so the kernel is (m/π)E_(1/m,1/m)(z w̄). For fixed w, positivity of the series bounds its modulus by the positive-axis kernel, with growth at most a polynomial factor times exp(O(|z|^m)). Thus e^(±g)K_w is in the weighted space since max(d,m)<2m. Projection of the anti-holomorphic symbol on K_w yields its conjugate value at w times K_w by pairing against monomials. This verifies the product domain and the exact normalized two-point factorization. For ζ=R²exp(iθ) in a fixed small sector, the dominant Mittag–Leffler term is mζ^(m−1)exp(ζ^m) with an algebraic remainder (the term in ζ⁻¹ has reciprocal gamma factor 1/Γ(0)=0). Its prefactor modulus cancels at equal radii; division by the uniformly exponentially large leading factor gives log Q=R^(2m)(cos(mθ)−1)+O(exp(−cR^(2m))). On the closed angular complement the kernel sector bounds give O(exp(−c'R^(2m))) after positive-axis normalization. In the near sector the maximum polynomial gain over the common phase is d|a_d|R^d|θ|+O(R^(d−1)|θ|+R^d|θ|³), by taking the exact leading-monomial phase maximum and bounding the lower monomials. Because d<2m, the far sector cannot beat the diagonal. Near it the inequality 0≤C R^d|θ|−c R^(2m)θ²+O(exp(−c'R^(2m))) confines every maximizer to |θ|=O(R^(d−2m)). After setting θ=vR^(d−2m), the normalized log objective converges uniformly on bounded v to d|a_d||v|−m²v²/2, even when d<m. Its unique maximizing magnitude gives both constants. Unit kernel normalization yields the stated boundedness consequences, using the published existence of the bounded extension at integer d=m. The Gaussian kernel gives the exact check |sin(θ/2)|=|a_1|/(2R) for sufficiently large R and log maximum |a_1|²/2.

## originality

PASS

The equal-radius two-coherent maximum and necessary separation, with exact constants, are distinct from every inspected predecessor. The two-kernel expression, Gaussian case, qualitative boundedness test, and sector asymptotics are existing inputs. The closest earlier saddle has the same shift scale and magnitude in a radial coordinate, but for a different, integrated squared statistic.

## value

PASS

At fixed radius the two normalized coherent states test the same radial scale, and the known boundedness proof already motivates this matrix coefficient. The exact size of its amplification and the common angular magnitude required of all extremizers give quantitative information absent from a bounded/unbounded decision. The same law governs log-amplification tending to zero, staying finite, or diverging, and gives a useful critical norm lower bound depending only on the top coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
