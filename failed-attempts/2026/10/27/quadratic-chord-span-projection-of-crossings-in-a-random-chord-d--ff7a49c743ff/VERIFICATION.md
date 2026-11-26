---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A fixed chord e at distance d leaves a uniform matching on the other vertices. Its mean number of crossings with the remaining matching is (d−1)(2n−d−1)/(2n−3). Subtracting the unconditional crossing mean n(n−1)/6 from the total conditional mean and multiplying by 1/(2n−1) gives the stated fixed-edge covariance. Write wₑ=(n−d)², N=2n, T for the incident-weight sum at any vertex and W for the sum over all edges. The conditional mean of Q is wₑ+(W−2T+wₑ)/(N−3), hence the coefficient of wₑ in Cov(Q,Iₑ) is (N−2)/[(N−1)(N−3)]; centering subtracts the mean edge weight n(n−1)/3. Thus the proposed centered residual is orthogonal to every individual edge indicator, not just rotationally invariant combinations. Summing the second and fourth powers of span deficits yields the claimed Var(Q). Independently, give the n labeled chords pairs of iid continuous uniform endpoints and use their cyclic ranks. For overlapping crossing indicators with one shared chord, their two conditional probabilities given that chord are 2U(1−U), with U a uniform oriented arc fraction. Conditional independence gives covariance 2/15−1/9=1/45; disjoint chord pairs are independent and individual crossing variance is 2/9. Consequently Var(X)=(2/9) binom(n,2)+(6/45) binom(n,3). Pythagoras gives both component variances, and subtracting 6/7 from the explained fraction gives (2n−9)(n−4)/[14(n−1)(n+3)], nonnegative for integer n≥2 and zero just at 4. The variance formula includes the exact-fit n=2 case. The sign threshold and Pell equation follow by summing fixed-edge covariances by class. The smallest positive solution to x²−12y²=1 is (7,2); its inverse unit reduces the positive y of any solution to a nonnegative smaller integer, yielding the asserted sequence. All such x are odd and y<(x+1)/2, ensuring the reconstructed d is admissible.

## originality

FAIL

The entire length covariance profile, threshold and Pell family are explicitly covered in Resultary cb8a3a4f935f. More importantly, combining that exact mixed-covariance vector with the full length covariance matrix in distinct Resultary 6e004b32ef71 mechanically gives the claimed quadratic projection by the normal equations. Rotation invariance then gives the individual-edge orthogonality. The published crossing variance supplies the remaining variance formula. The identifiable contribution is therefore an assembly of existing formulas using standard regression and symmetry, not a distinct exact result under the review standard.

## value

FAIL

The projection is a natural and interpretable summary of how chord spans predict crossings. In this submitted form, however, the result is a direct normal-equation specialization of exact known covariance arrays; the sharp fraction is arithmetic and the exact Pell classification is already stated elsewhere. The package does not establish a distinct structural result or additional useful scope beyond that mechanical consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
