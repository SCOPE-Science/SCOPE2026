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

Average conjugates over simultaneous permutations of matched pairs and part interchange. This preserves feasibility and the uniform projector, and convexity ensures the centered norm cannot increase. In the averaged chain c=1−a−(m−1)b is the holding probability, and the cross block is (a−b)I+b11ᵀ. The centered nontrivial modes (part difference and the two paired zero-sum modes) have eigenvalues 2c−1, c+a−b and c−a+b, so the norm is max{|2c−1|,c+|a−b|}. Substituting b=(1−a−c)/(m−1), the latter linear modes are [(m−2)c+1−ma]/(m−1) and [mc+ma−1]/(m−1). Convex-combine 1−2c with each of these, choosing weights to cancel c. This gives unconditional lower bounds m(1−2a)/(3m−4) and (m−2+2ma)/(3m−2), including m=2 when the first mode's slope is zero. At their sole crossing a*=2/(3m) they equal 1/3. On the first branch the proposed b,c are nonnegative, c+a+(m−1)b=1, b≥a and c≤1/2; on the second the same checks hold with b≤a. The selected linear mode equals 1−2c on each branch, attaining the lower envelope of feasible objectives. The endpoints m=2,a=0 and a=1 retain the extra unit-modulus eigenvalues in the centered norm. For common bounds, the matched-edge average lies in [ℓ,u], and the strictly decreasing then increasing fixed-a response is minimized by clipping a*. This neither asserts uniqueness nor optimizes a finite-time distance. The frozen exact-rational checker was inspected, not run; these calculations prove the all-parameter result.

## originality

PASS

Bounded best-of-knowledge pass for the full fixed-probability tradeoff and its common-interval extension, not for the unconstrained balanced optimum, crown endpoint, or symmetry method. The strongest plausible published and indexed overlaps fix those individual cases or give a general reduction; none of the compared results evaluates the two-orbit constrained frontier at intermediate a.

## value

PASS

Fixing a distinguished partner link is a natural constraint in a two-class reversible network. The exact frontier quantifies how both inadequate and excessive use of such links harms mixing, identifies the switch between two spectral bottlenecks and tells when a permitted range incurs no cost. This is a useful all-size, all-capacity design law beyond the generic SDP and already-known endpoints.

The dated certificate retains the supplied scientific assessment, sources and limitations.
