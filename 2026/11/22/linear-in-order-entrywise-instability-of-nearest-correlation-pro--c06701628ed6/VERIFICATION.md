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

In the fixed-diagonal affine space, the off-diagonal coordinate isometry up to factor sqrt(2) preserves both nearest points and the max-entry size of differences. For k=n-2 and any r>0, the two contrast eigenvalues are 2(1-c^2) and k(1-a^2)/(k-1); the two-constant sector has matrix with diagonal 2c^2, ka^2 and off-diagonal -sqrt(2k)ca. Its determinant is zero and trace positive. The kernel is precisely span(1,1,r,...,r). Differentiating the simple zero eigenvalue in zero-diagonal directions gives the halfspace with inward normal q_ij=v_i v_j; its exterior-direction projection has tangent-plane linear part I-qq^T/||q||_2^2. The (1,2) row has nonnegative diagonal, negative other entries, and absolute sum exactly 1+F_k(r). At the boundary this is a directional tangent-plane calculation, not a claim of an ordinary two-sided derivative of the projector. For each fixed direction, the scaled convex sets increase to a dense subset of the tangent cone as the scale decreases; bounded nearest points therefore converge to the unique tangent-cone nearest point. A common exterior shift of two directions realizing the row signs yields two distinct nearby finite inputs and their ratio limit. F_k has a positive attained maximum since it is positive at r=1, tends to -1 at zero and to 0 at infinity. At r=s/sqrt(k), F_k/k converges uniformly on compact s intervals to s^2/(2+4s^2+s^4); the small-s numerator bound and large-s quartic denominator bound trap all maximizing sequences away from both tails. Differentiating in s^2 gives the unique limiting maximizer 2^(1/4) for s and maximum (2-sqrt(2))/4. Firm nonexpansivity in n(n-1)/2 independent coordinates bounds the full Lipschitz modulus from above at linear order, not by the particular family constant.

## originality

PASS

The specific realizable rank-(n-1) normal family with its exact row gain and optimized asymptotic lower coefficient is distinct. The universal upper bound and the transfer from a local halfspace to finite pair sensitivity are shared with a broader smooth-projection result and are not independently novel. Other same-day findings establish coordinate growth for different projectors, not the fixed-diagonal elliptope witness.

## value

PASS

For a standard operation in correlation repair, the theorem determines the growth order of a natural measure of worst-case individual-entry error and exhibits the exact local geometry that causes it. Realizing rank deficiency while maintaining the whole unit diagonal is a relevant constraint, not an arbitrary parameter restriction. The optimized witness makes the lower bound useful even though the full sharp constant is open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
