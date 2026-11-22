---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

The final theorem explicitly restricts to three-side-tangent nondegenerate inellipses and an interior target w_i>0 (allowing target on filled-ellipse boundary). Restricting F_u to each side gives a squared linear form, u_i>0 and sum u_i=1. Exact Hessian determinant 4u1u2u3 and center value -u1u2u3 give normalized area pi sqrt(product u). The inequality F_u(w)<=0 is exactly the Heron triangle inequality for sqrt(u_i w_i); hypograph convexity follows from geometric-mean concavity. The objective sum log u_i is strictly concave on the convex feasible domain, with an interior Slater point u_i proportional to 1/w_i and boundary product zero. Unconstrained Steiner u=(1/3)^3 is feasible iff 2sum w_i^2<=1. When infeasible, exactly one Heron inequality is violated there, so the single active constraint yields sqrt(w_k u_k)=sqrt(w_i u_i)+sqrt(w_j u_j); all other triangle inequalities then hold strictly. Its one-parameter product ABC q^2(q+1)^2/[A(q+1)^2+Bq^2+C]^3 has derivative proportional to the displayed cubic with sign pattern +,+,-,- and exactly one positive zero. The median t>2/3 gives u=(1-t,t/2,t/2) and H=(pi/2)t sqrt(1-t), matching C1 at t=2/3. Independent exact SymPy checked the q-derivative, F_u(4/5,1/10,1/10)=0 for u=(1/5,2/5,2/5), and the right second derivative -3sqrt(3)pi/4. No sample proves universality; the convex proof does.

## originality

PASS

Four statement-level comparisons distinguish the specified result from the inspected primary-source coverage; best-of-knowledge priority, not an absence-of-search novelty guarantee. 

## value

PASS

Maximal-area three-side-contact ellipses under one point-inclusion constraint form a natural affine-invariant geometric design problem; an all-interior-target constructive optimum, sharp Steiner saturation region, and nontrivial curvature break are motivated and not mere replacement of a classical unrestricted optimum. Three-side tangency and closed point containment are explicit limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
