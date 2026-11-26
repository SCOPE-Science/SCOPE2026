---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The coefficient vector V^{-1}N for a generator factor V has covariance (V^T V)^{-1}, not the Gram matrix itself. Its exact law is g+sTu with s^2=(1-epsilon)/epsilon. Condition on g: the mixed-sign event restricts sT to (L,U), whereas for unanimous signs it is sT>H after a global sign change. Integrating the standard normal density gives a global cubic remainder about zero, bounded by |x|^3/(6 sqrt(2 pi)); fixed nonzero coordinates ensure the three extrema have finite third moments. The mixed gap has positive expectation because the feasible interval has positive length on an open Gaussian event; the maximum of at least two independent nondegenerate centered normals has positive mean. Replacing 1/s by sqrt(epsilon)+O(epsilon^{3/2}) yields both claimed errors. For equal magnitudes the sign-count integral is strictly log-convex by Hölder: the odds Phi(aT)/Phi(-aT) are nonconstant for 0<epsilon<1. Its p to n-p symmetry gives strict decrease to the midpoint. In the leading constant, the p labeled normals occupy exactly the p lowest ranks with conditional probability 1/binomial(n,p); only then does the interval have length equal to the stated adjacent spacing. Read RESULT.md lines 52–105, VERIFICATION.md and verify_angles.py; the recorded finite numerical result was not rerun and does not prove the theorem. No uniformity near zero coordinates or strictness at epsilon=1 is inferred.

## originality

PASS

Credit Schange with the exact low-rank integral, including the signed negative-rank-one specialization. The supported distinction is the structural comparison across its fixed-spectrum sign patterns together with the explicit sharp singular coefficients, in particular their adjacent-rank spacing identity. Rescaling the known integral is a short route to the leading laws; the formula alone is not a stated or automatic ordering across sign counts or an order-statistic identity. Those require identifying strict log-convexity in the sign-count exponent and using the random label allocation in the mixed-sign limit. Neither the simplex equicorrelation results nor the inspected regular-simplex section result covers this comparison.

## value

PASS

A complete strict ordering and sharp singular law show what generator lengths and the Gram spectrum fail to determine, even on the simplest nontrivial low-rank family. The difference is geometric rather than a numerical refinement: at the identical spectrum the limit can be one half or zero, and a particular adjacent Gaussian spacing quantifies the collapse at each mixed sign split. The value is the structural comparison and precise boundary geometry, not computing one more instance of a known integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
