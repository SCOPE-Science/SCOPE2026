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

For a fixed domain D the extensions of each restriction form a coset of its pointwise stabilizer. The only nontrivial stabilizers are at the empty set, singletons and, for even n, antipodal pairs: any nontrivial rotation fixes nothing, and 2x=a characterizes reflection fixed points. Representing each restriction with inverse-stabilizer weight and replacing the second domain by its image gives the intersection-rank formula; equivalently, inversion bijects maps of prescribed image with maps of prescribed domain, independently of the first factor. The empty/singleton/antipodal weight defects give total S, incidence v and pair-incidence square sum epsilon*n/8. Expanding t^{|D∩E|} up to degree two on the double-defect terms proves both corrections, and evaluating at t=1 gives the size. Vertex inclusion gives the mean; acceptance coupling with a uniform subset gives marginal TV ≤S/2^n, hence joint/intersection TV ≤2S/2^n and transfers the CLT. In fact the event rank≥3 gives a lower bound [(1-S/2^n)^(-2)-1] Pr(Bin(n,1/4)≥3), so the stated scale is sharp as n tends to infinity. Independent exact replay: python /workspace/branches/independent_math_1_4.py 1, counting distinct image tuples per domain then summing over pairs of masks, verified every coefficient, the size and the rational mean at n=3..8. The frozen script was inspected, not run; its mean comparison uses float tolerance, unlike this replay. Finite counts corroborate but do not prove the all-n result.

## originality

PASS

The representation and stabilizers are known; the supported distinction is the explicit all-ranks uniform-distinct two-factor law with its parity corrections and exponentially accurate binomial comparison. Neither the single-element cycle enumerators nor the closest intersection statements supply this law under its sampling hypotheses.

## value

PASS

Complete product-rank information for the canonical cycle action goes beyond the known one-element counts. It resolves the parity-sensitive way extension duplication affects all small-rank coefficients, and quantifies a precise binomial approximation for the uniform law on actual restrictions rather than on redundant representations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
