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

The matched adjacency is (d+1)-regular. For the fan, the top eigenvalue exceeds d by connected nonnegative-matrix strict comparison with the two disjoint copies. The second Perron block is x_v times the constant vector divided by lambda-d, so the v-coordinate of the first block gives the scalar equation. Its left side increases and its right side strictly decreases from infinity to zero (the constant mode gives a pole with positive residue at d). The cross-block star has radius sqrt(n); the disjoint internal part has norm d, giving sqrt(n)<=lambda<=sqrt(n)+d. For lambda comparable to sqrt(n), the diagonal Neumann series has coefficients 1,0,d,t_v and error at most d^4/[lambda^5(1-d/lambda)]. Put s=sqrt(n) and write the truncation as s+a+b/s+c/s^2. In the equation multiplied by lambda the left-hand coefficients at s,1,1/s are 2a-d, 2b+a^2-da and 2c+(2a-d)b, and the right-hand coefficients are 0,d,t_v-2ad. Thus a=d/2, b=d/2+d^2/8 and c=(t_v-d^2)/2. The original equation has residual O_d(s^-3) and derivative >=1 for all lambda>d, proving uniform distance to its unique root. The two Cartesian cycle products in the proof have equal order and degree and t_v=0 versus 2 once the other factor has length at least four; their correction differs as stated. The inverse-radius consequences are only adjacency spectral thresholds, not exact stochastic persistence claims. A bounded check using the explicit Cartesian-cycle Fourier eigenvalues to evaluate the diagonal resolvent reproduced the scaled eigenvalue difference moving toward 1 (0.5711, 0.7431, 0.8575, 0.9247 at n=120,480,1920,7680); replay /workspace/branches/spectral_design_replays.js, graphCheck. VERIFY.py was inspected but not executed. It checks two fan computations, using matching regularity analytically rather than constructing the matching matrix as the frozen verification prose suggests. This is a nonmaterial description issue, not an assumption of the proof.

## originality

PASS

The submitted contribution is the fixed-degree, uniform high-order expansion under the common edge budget, especially the first local-triangle correction. The matching formula is explicitly known, the exact scalar identity follows from classical rooted coalescence, and the leading sqrt(n) growth is elementary. These are baselines, not distinct contributions. The strongest available broader results do not supply the uniform higher-order coefficient or the equal-order, equal-degree witness distinguishing it. This conclusion is bounded by the checked literature and catalogue.

## value

PASS

The elementary scale contrast on its own would be weak: the star norm already yields it. The substantive quantity is the first local-structure term with an error uniform over fixed-degree regular inputs and attachment vertices. The same-order product examples show that this term measures a real separation even after the leading degree and size contributions cancel. That gives an exact structural explanation of how the abstract spectral comparison can depend on motifs, without implying a stochastic persistence result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
