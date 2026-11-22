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

For an orthogonal projector P_U reproducing sampled constants, i and i² but not e0, q=P_Ue0 obeys sum q=1, sum iq=0, sum i²q=0. Writing |a|=a+2(-a)+ yields G(q)=n−1+2 sum_{i<j}(q_j−q_i)+. If G(q)=n−1, q is monotone decreasing; the first and second moment conditions imply all i q_i vanish for i>=1, then q=e0, contradiction. This proves strict expansion by one endpoint impulse for every polynomial degree 2<=d<=n−2. Degree0 constant has norm0, degree n−1 identity norm1; affine slope b=(sum(i−μ)x_i)/S and the oriented pair identity give norm1. Exact independent rational Gram inversion n=4..10 reconstructed the quadratic endpoint column, ratios (17/15,6/5,87/70,80/63,9/7,217/165,661/495), and exhaustive 4-point binary cuts confirmed sharp norm17/15. The degree-two continuum endpoint kernel k(t)=9−36t+30t² has oriented Gini integral1 and negative contribution64/125, giving 189/125. It is a fixed-input asymptotic witness, not an asserted operator-norm limit.

## originality

PASS

PASS best-of-knowledge for the basis-free three-moment obstruction and exact all-degree Gini nonexpansivity classification plus quadratic impulse asymptotic. Persson–Strang and older Savitzky–Golay theory give discrete-polynomial filtering and moment reproduction, not complete-pair Gini operator monotonicity. The published quadratic endpoint sensitivity theorem has the **same** q_j kernel but analyzes ℓ∞ row norm and arithmetic second-order phase rather than pairwise Gini; the exact kernel itself is credited prior rather than new.

## value

PASS

Complete-pair Gini variation is a natural inequality-sensitive non-Euclidean stability measure for sample smoothing. A sharp qualitative boundary between affine and any higher polynomial reproduction, valid for any orthogonal subspace reproducing moments up to order two, is a structural obstruction and not a routine consequence of Euclidean contraction. The explicit persistent degree-two ratio and n4 sharp example quantify that boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
