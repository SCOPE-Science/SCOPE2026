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

For an atom inside a gap the only nonzero noiseless cardinal coefficients are the two positive sinh ratios; exponential multiplicativity extends the two-node equations to all nodes. Their cosh-ratio sum is at most one, as is the single exterior exponential, so integration covers any finite nonnegative Borel measure including atoms or zero. The Markov quadratic form gives the inverse Q with nonpositive off-diagonals and strictly positive row sums; each interior sum is (1-rho_left rho_right)/((1+rho_left)(1+rho_right)), and the endpoints and n=1 obey the same strict sign. Write M=I+QD=B-E with diagonal B>0 and E>=0 off diagonal. The column sums of M are 1+d_j(Q1)_j>=1, so E B^{-1} has column norm less than one and M^{-1}=B^{-1} sum_{k>=0}(E B^{-1})^k>=0, with positive diagonal even if some nuggets vanish. This proves the full-support strict case; when all nuggets are positive the neighboring entries connect the chain, and the inverse is strictly positive, proving the nonzero-measure strict case. Summing the equation gives 1^T(v-w)=(Q1)^TDw>=0, where v=K^{-1}b, and equality at a noiseless node atom proves sharpness. For 1<alpha<=2, the sign of the first weight for the exterior atom at a+b is the sign of (1+d_2)-exp(lambda[(a+b)^alpha-a^alpha-b^alpha]); the exponent tends to infinity for fixed a>0, including any prescribed finite nugget. The two-site determinant is positive. An independent exact check (`python /workspace/branches/audit_checks.py ou`) includes mixed zero and positive nuggets and an exact Gaussian weight -127/29360128; the frozen checker was inspected, not executed. Nothing here covers non-diagonal noise or exponents below one.

## originality

PASS

Do not credit the classical noiseless OU bridge, integrated-cardinal-function method, or M-matrix inverse theory as new. Checked evidence supports the combined arbitrary-measure, arbitrary finite heteroscedastic diagonal-nugget subprobability theorem and the sharp power-exponential obstruction with preassigned nuggets. The closest indexed and published results concern noiseless design, selected optimal designs, positivity under narrower hypotheses, or correlated noise.

## value

PASS

The subprobability bound supplies a directly usable sup-norm stability guarantee for an unconstrained noisy quadrature rule with arbitrary nodes and measures, not just at optimized sites. The lack of any finite diagonal-nugget protection for all exterior targets when alpha>1 is a motivated stability boundary and distinguishes smoothness from robustness. Positivity is not mistaken for small integration error or good matrix conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
