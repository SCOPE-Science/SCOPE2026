---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The simplex sum and positivity follow from the exact homogeneous replicator vector field. With s=u1+u3-u2-u4, x=u1-u3, y=u2-u4, C=(1-s^2)/4 and d(log(product_i u_i))/dt=a s^2 exactly. For a>0 the product lower bound confines every interior trajectory to a compact positive simplex set; LaSalle reduces omega limits to s=0; there s-dot=-(a+2)xy and (x,y) is a nonzero rotation unless x=y=0, hence the maximal invariant subset is U. For -1<a<0 a positive product limit would imply interior precompactness and force convergence to U, contradicting strictly submaximal initial product and monotone decrease, so product->0 and min_i u_i->0. For a>0, eigenvalues -a/4, ±i(a+2)/4; the quadratic center-manifold invariant polynomial h_2=4(a+2)^2(x^2-y^2)/D - 4a(a+2)xy/D (D=a^2+4(a+2)^2) has zero invariance residual. The quartic radial drift angular average is -a(a+2)^2/(2D), positive damping; periodic normal-form transform yields dot Z=-beta Z^2+O(Z^(5/2)), hence tE->1/beta. The unique strong stable manifold is the invariant x=y=0 line; all other interior orbits exponentially track the center manifold. SymPy independently checked the exact h_2 identity and angular mean; two integrations to T=6000 exhibited finite-time approach, not proof of the asymptotic claim.

## originality

PASS

Best-of-knowledge PASS: the closest directly model-matched 2026 paper supplies the vector field and center spectrum, whereas available material does not establish this exact global-in-time homogeneous sign-of-bias and sharp inverse-time coefficient. Important unresolved historical priority risk: full text of that model-matched article was not accessible; no unsupported assertion that the unread whole article is non-covering.

## value

PASS

A genuinely nonlinear center-spectrum question left open by oscillatory finite-time plots is settled globally by a model-specific product Lyapunov identity; the exact universal original-time 1/t amplitude and identified exceptional faster-decay invariant line sharpen the dynamical classification. Negative-bias extinction provides the opposing sharp sign regime. These are structural, mathematically motivated results and not a textbook restatement of imaginary eigenvalues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
