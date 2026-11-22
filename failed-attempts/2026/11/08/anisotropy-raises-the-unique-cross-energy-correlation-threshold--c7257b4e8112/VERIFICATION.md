---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-19.md",
      "INDEPENDENT_AUDIT_2026-11-19.json"
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

The exact invariant position is a causal convolution of bounded forcing under strictly positive diagonal drift; with independent uniform-sphere marks, E[n_i^2 n_j^2]=1/[d(d+2)] and conditioning on shared exponential clock intervals gives Cov(X_i²,X_j²)=v^4/d²(Cov(S_A,S_B)−2E[J_AB]/(d+2)). The renewal equations in the source are exact, and independent stationary-generator recursion reconstructed the same rational numerator P=dU−V and positive denominator symbolically in SymPy, with no reliance on finite-only tests. The coefficient ratios of V/U are strictly decreasing for g>0 (v1/u1>=12>v2/u2>34/7>4 and positive v0), so V/U decreases continuously from infinity to 4; the sign is negative for d<=4 and crosses exactly once, simply, for d>=5. The exact g0 evaluation P(g0)=−(A−B)²s²(2d+1)(4d−7)/(d−4)² and dP/dp>0 at g>=g0 prove sharp lower bound and strict monotonicity under anisotropy. Recomputed numerical positive roots (d,A,B)=(5,1,2):9.325485849042453, (6,1,2):4.743416490252569, (5,1,1):6; numeric checks only corroborate analytic proof. Positive parameters/d>=2, zero thermal noise, and common iid redraw are indispensable.

## originality

FAIL

A prior published November 2, 2026 SCOPE/Resultary theorem (aa1b705578c0) displays precisely the same rational cross-energy covariance polynomial, all-d sign diagram, unique root, and sharp strict equal-stiffness lower bound, in fact in the broader model with independent thermal Brownian forcing. The only ostensibly extra global fixed-s monotonicity in the November 8 statement follows immediately by differentiating the published affine-in-p polynomial and using the already-proved root localization. The new result is therefore a covered reformulation/corollary, not an original final claim.

## value

FAIL

The phenomenon is physically motivated (joint squared-coordinate fluctuations and sharp dimension boundary), but the assigned final package recomputes the same complete natural classification, exact rational expression and threshold of the already-published November 2 result. Its additional fixed-s monotonic statement is a one-derivative corollary of that prior polynomial and known root bound, with no new object, invariant, boundary, or independently useful mathematical gap left. As a separate new finding it is known-result recomputation and routine calculus, not a worthwhile additional mathematical contribution; this is distinct from the fact that the original earlier theorem itself is valuable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
