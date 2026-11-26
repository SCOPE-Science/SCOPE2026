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

The squared-weight products give the 2-isometry identity, while every initial weight exceeds 1. On positive shifts both polar isometries are the ordinary shift, so iterating the arithmetic average of weights and the arithmetic average of log weights yields the two stated binomial expressions. The gap is strict by Jensen and its singular values are the positive weights. With k fixed, h'(n+c)=-1/[2(n+c)(n+c+1)], so the leading variance is k/(16n^4) and the exponential Jensen gap is k/(32n^4), giving compactness and divergence also at p=1/4. For the joint scale, the Taylor error in L² about n+c+k/2 is O(k^-2) by the fourth binomial moment and exponentially small exceptional event; its cross term with the linear part is O(k^-7/2). On the central event the fluctuation is uniformly o(1), so its third absolute moment is o(k^-3) by the variance bound, with the exponential exceptional event again negligible. The Efron–Stein conditional one-bit variance factor is 1/4; splitting the remaining binomial at k/4 yields (107). The exponential term there can even be absorbed into C_c k/(n+k)^4 using (n+k)/(n+c)≤1+k/c, furnishing an integrable Riemann-sum domination for 4p>1 and uniform tail control for the supremum. Integration gives 1/[2^(p+1)(4p-1)] and the profile's maximum is 1/2. Individually both iterates lie between w_(n+k) and w_n, so their gaps from the ordinary shift are asymptotic to 1/(2n) at fixed k, and are not trace class.

## originality

PASS

The natural shift family and both iteration identities are prior results. The supported distinction is the mean-minus-Aluthge orbit's sharp Schatten membership, fourth-order profile and exact joint-limit constants. No inspected source gives or directly implies that combined conclusion without the additional asymptotic and integrability argument.

## value

PASS

The input is the natural class of positive nonisometric 2-isometric weighted shifts and the transforms are standard competitors. The difference from the unweighted shift for each orbit separately has a harmonic tail, whereas the mutual difference has fourth-order decay; exact membership in quasi-ideals, including failure at the boundary, is a materially stronger comparison than common norm convergence. The uniform profile bridges the fixed-iteration tail and the many-iteration rate and gives exact trace, Hilbert–Schmidt, and operator-norm benchmarks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
