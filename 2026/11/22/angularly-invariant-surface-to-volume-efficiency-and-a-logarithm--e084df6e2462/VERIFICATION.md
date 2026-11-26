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

The two transverse-normal coordinates and the normal to the axes' plane give rectangular sections and Jacobian sin(beta). Radial distance to each axis has gradient of length one on its exposed patch, so coarea gives S=V_R+V_r; the common boundary lies in finitely many curves and contributes zero area, including at equality. Homogeneity gives the stated F-representation of Q. For t>1, 3−Q is the expectation of g=t(t−1)/(t²−y²) under density proportional to sqrt((t²−y²)(1−y²)). The t-derivative of g has a positive numerator at least (t−1)², and the covariance with the density score is nonnegative because both functions increase in y. This proves strict decrease of Q; continuity, F(1)=16/3, F'(1+)=8, and uniform g→1 at infinity give the range (2,3]. After y=sin u, with Delta=sqrt(1−k² sin²u), the area integrals reduce to E and integral cos²u/Delta=[E−(1−k²)K]/k². Integrating the derivative of sin u cos u Delta gives the stated volume elliptic reduction. For the cusp, t=1+eta and u=1−y give F'' integrand −4 sqrt(u)/(u+eta)^(3/2) times (1+O(u+eta)), with endpoint integral −4 log(1/eta)+O(1). This yields the stated Q cusp and Q'(1+eta)=−3/2+(3/2)eta log(1/eta)+O(eta), so the right second derivative is not finite. Expanding the integral uniformly in 1/t² gives F=2πt[1−1/(8t²)+O(t^(−4))] and the far-end expansion. There is a common seam even at equality; the singularity concerns resolution of the equal-radius endpoint degeneracy, not first existence of a seam.

## originality

PASS

The foundational volume integral and its elliptic evaluation and the equal-radius Steinmetz normalization are existing coverage, not new findings. The inspected prior volume formulas also encode analytic ingredients for the area and end expansions via differentiation. The supported distinct claim is the strict all-ratio inverse theorem for this specific efficiency, with its sharp endpoint behavior; the inspected sources did not show a monotonicity theorem for it or a stronger assertion from which that theorem is immediate.

## value

PASS

Recovering the radius ratio from scale-normalized boundary area per volume in a classical convex family without angular data is a natural inverse problem. Strict monotonicity makes the recovery unambiguous, and the logarithmic second-order correction rules out a smooth quadratic approximation at the symmetric endpoint. Neither a volume formula alone nor a finite table establishes this sign or boundary regularity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
