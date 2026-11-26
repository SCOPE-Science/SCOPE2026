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

At t<=1 and t>=d the functional is a norm. In the intermediate regime put c=(t−1)/(d−1). The polar of the convexified ball is the intersection of the dual constraints ||z||∞<=1 and ||z||1<=t. Assigning an aligned dual entry of modulus 1 at a largest coordinate and modulus c at all other coordinates yields h(x)>=M+c(||x||1−M), M=||x||∞, valid over either scalar field. The resulting scalar ratio min(1+r,t)/(1+cr) peaks at r=t−1. The pair (1−c)e1 and c·(1,…,1) has denominator 1−c+tc and numerator t, proving both sharpness statements by matching the upper bound. Differentiation gives the sign of d−t^2, so sqrt(d) is the unique global optimum and substitution gives (sqrt(d)+1)/2. On ℓ1 the sup-norm bound gives t when t>1, and the same finite supports approach it. Equality would force both nonzero entries of the pair, as vectors, to have singleton supports since q_t(x)=||x||∞ there; the sup-norm triangle equality forces the same support, on which the quotient is at most one. A zero vector gives ratio one as well. The norm regime t<=1 follows directly, and no completeness claim is needed. Analytic verification; the frozen finite rational checker was inspected, not executed or used as proof.

## originality

PASS

Best-of-knowledge pass for the exact dimension/scale constant and infinite nonattainment, not for the generic fact that binary and convexification distortions coincide for the gauge of a union of two convex balanced balls. In that setting any element of the convexified unit ball is one convex combination of one element from each ball, by grouping convex combinations within each ball. Applying the binary estimate gives the full convexification bound; the reverse follows from h<=q and subadditivity of h. The distinct mathematical comparison is the explicit sharp value for this pair of classical balls, with its scale optimum and limiting phenomenon. The matched ellipse and cube/cross geometry records do not compute that constant.

## value

PASS

The precise convexity defect of two canonical norm balls, as their relative scale varies, gives the sharp worst-case square-root dimension growth and identifies the budget where it occurs. The loss of attainment in the infinite coordinate space records a concrete difference between finite and unbounded support. These add value beyond the generic grouping identity for convexification and beyond a bound from norm equivalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
