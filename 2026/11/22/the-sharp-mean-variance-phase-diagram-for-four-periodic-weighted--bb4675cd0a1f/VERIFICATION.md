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

For any half-line unit vector, grouping the coordinates into the four residue classes and applying Cauchy–Schwarz bounds the numerical-range modulus by the weighted cyclic quadratic form of their four norms. Conversely, take a long constant repetition of a nonnegative maximizing vector of the four-cycle form, normalized in the half-line space; the fractional endpoint loss tends to zero. This verifies the reduction including zero weights, without requiring an irreducible Perron eigenvector. The bipartition gives w(T)=s/2 for s=||B||, B=[[a,d],[b,c]]. With mean one, sum 4 and squared sum Q=4(1+v), uniform test vectors give s>=2; equality forces both row sums and both column sums to be 2. Thus the only first-branch minimizers are alternating 1±sqrt(v). For the second branch, each entry is at most s and 2<=s<=4; maximizing the sum of squares of four entries in [0,s] of sum 4 gives Q<=s²+(4-s)². Indeed a maximum is at an extreme point of the capped simplex, with at most one entry not at an endpoint, and strict convexity excludes non-extreme equality. When two entries are positive at equality one equals s, and they cannot share a row or column (the row or column Euclidean norm would exceed s). Opposite edges therefore give all equality cases, and the diagonal examples realize the bound. Sum and square-sum bounds force 0<=v<=3 and the two families realize the entire interval. For 1<=v<3 set (a,b,c,d)=(2-e+D,e,2-e-D,e) with D²=2(v-1)+4e-2e². For sufficiently small e>0 this is positive, preserves both moments, and converges to the extremizer; v=3 itself permits only one positive entry. Thus the claim about positive weights is an infimum on the feasible range v<3, and both endpoints are accounted for. RESULT.md lines 17–36 and VERIFICATION.md lines 19–27 are consistent with this reconstruction; finite-section approximations or numerical replay are not needed.

## originality

PASS

The established periodic numerical-radius formula and the two-period value are not new. The supported distinct claim is the exact constrained four-period minimum, including the change from alternating full support to opposite-edge support and its positive-weight nonattainment. The strongest inspected comparisons either evaluate the norm for a specified sequence without optimizing the two moments, optimize a different period, or optimize a different functional.

## value

PASS

This gives the exact two-moment envelope in the first even period where an arbitrary sequence is not necessarily alternating. It determines when the mean alone stays sharp, when increasing variance strictly raises the optimum, and when positive weights can only approach it. The distinction between attainable equality and a boundary infimum is useful information not supplied by the norm formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
