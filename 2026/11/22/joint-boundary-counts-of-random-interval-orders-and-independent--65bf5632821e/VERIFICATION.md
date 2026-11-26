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

IID atomless endpoints give a uniform perfect matching of ranks. An interval is minimal exactly when it opens before the first right endpoint, so M_n≥k means no internal match in the first k ranks. Reflection gives the analogous last-l ranks event. Conditional on j initial openings, the next endpoint is new with probability (2n−2j)/(2n−j). For the joint event the rank blocks A,B are disjoint; choose and biject h endpoints of each to make the A–B pairs, assign the remaining k+l−2h labeled vertices injectively into the middle c, and pair the remaining 2z middle ranks. The product is exactly k!l!c!/[h!(k−h)!(l−h)!2^z z!], with the stated bounds from z≥0 and h≤min(k,l). This includes k or l zero and n=1; mixed finite differences give the masses. For uniform endpoints, the minimum right endpoint T and reflected maximum left endpoint W exclude disjoint squares of endpoint space for thresholds a+b≤1, giving (1−a²−b²)^n and the joint independent limit for sqrt(n)(T,W). Conditional on the winning interval and T=t, the other endpoint pairs are independent truncated to R>t, with P(L≤t | R>t)=2t/(1+t); this distribution does not depend on the winning index. Thus the scaled difference between the counts and 2sqrt(n)(T,W) goes to zero in L²: conditional variance is O(n E T)=O(sqrt(n)), and the squared bias is O(1) by E T^4=O(n^−2). Reflection handles W. The product bound exp(−k(k−1)/(4n)) gives uniform fourth moments and uniform integrability of scaled squares and products. Integrating the limiting tail gives mean sqrt(pi) and second moment 4, hence the stated variance and zero limiting correlation. The checker was read, not run; the argument proves all n.

## originality

PASS

The supported distinct claim is the finite exact bivariate survival law for the counts of precedence-minimal and precedence-maximal intervals. The same-day endpoint-extreme result explicitly covers the underlying joint Rayleigh limit for endpoint positions, and another same-day result gives that limiting law after doubling for different degree observables. The boundary-count limit follows by a concentration bridge and should not be treated as an independent discovery of the endpoint law. These sources do not supply the exact finite rank-block joint law for the counts.

## value

PASS

Both extremal-rank counts measure the boundary of the natural random precedence poset. Their transparent exact joint law is useful for finite probabilities and dependence and distinguishes the order boundary from previously studied graph and containment observables. The asymptotic independence and moment statement clarify how that finite dependence behaves; they complement rather than substitute for the exact count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
