---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

On the space perpendicular to the constant vector, connected weights give a positive definite Laplacian. The inverse trace is strictly convex: its second derivative in direction H is twice the squared Frobenius norm of A^(-1/2) H A^(-1), and off-diagonal entries recover edge weights, so a nonzero edge direction gives a nonzero H. The feasible budget simplex is compact; approaching disconnection makes the inverse trace diverge. Thus averaging over simultaneous permutations of matched indices fixes the unique minimizer and gives only weights a,b, with a>0. On the constant and zero-sum parts of both bipartitions the off-diagonal block aJ+(b−a)I yields eigenvalues 0, 2((n−1)a+b), na and (n−2)a+2b, the last two each with multiplicity n−1. This gives the displayed budget and all-pairs resistance formulas, including the zero-matching boundary. For N=2(n−1)X^(-2)+(2Y²)^(-1) and D=1/n+(n−2)X^(-2)+(2Y²)^(-1), independent differentiation gives (n−1)(tD−N) after removing the constant factor. The cross term of N'D−ND' is n(X−2Y)/(X³Y³)=−n²/(X³Y³), and N'/n is negative, so N/D decreases to zero. Equality at T_n(0) gives only r=0, and T_n(1)=1. For the determinant, log-det is strictly concave in affine weights (or in b on its feasible segment), not asserted concave after changing to r. The matrix-tree product gives the stated τ. At r=0 the derivative is 2(n−1)/(n−2)+1/(n−1)−(2n−1)t/(n−1). The sign transfers to b; strict concavity includes equality on the deleted side. Subtraction gives the claimed positive gap, and expansion gives n^(-1)+O(n^(-2)). For fixed t<1, nN(cn) tends to 2/(1+2c)² and nD(cn) to 1+1/(1+2c)²; monotone bracketing at fixed c on either side of c_t proves convergence and the budget-share limit. For t>1 the threshold tends to 1. The supplied symbolic/numerical checker was read, not run; the independent checks are analytic.

## originality

FAIL

The actual resistance-optimization package is already present in an earlier indexed record under a reversed a,b convention and B=1. The apparent additions do not leave a distinct scientific claim in the inspected catalogue: the exact determinant cutoff and the exact comparative support interval and gap are explicitly present in distinct records, and a broader spectral-moment record includes both thresholds. This is verified content coverage. It is not a claim that the later catalogue entries have chronological priority or that the results are externally peer reviewed. The explicit matched budget-share expression and arbitrary B are immediate changes of normalization, not new results.

## value

PASS

The mathematical question is motivated: the same cost classes yield different support under standard resistance and tree-determinant criteria, and the explicit nonempty price interval gives actionable information beyond uniqueness or symmetry. This assesses the substance of the comparison, not the originality of this rendition. Changing B by scaling or restating a known ratio as a budget share does not in itself add value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
