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

For a periodic W¹,¹ primitive, its derivative has zero total mass, and the product of its normalized positive and negative parts expresses its centered sample vector as a mixture of the vectors of centered arc indicators, times V/2. Endpoint atoms may be approximated by disjoint smooth derivative bumps away from sample sites to obtain the supremum; for limiting cuts touching sample sites, first approach from the admissible sides. For k consecutive included sites the squared output is F_k(L)=k(1−L)²+(N−k)L². Convexity selects a short or long endpoint for each run, and complementation turns the short endpoint into a long one; empty and full arcs are complements. Long endpoints have cyclic mean (k+1)/N, and F_k increases strictly above k/N. This proves the sharp uniform-design lower bound, with equality requiring every long cut to equal its mean for each central k. Consecutive shifts in the odd case and gcd(2m,m+1)=1 for even m force equal gaps; for odd m the gcd is two and the gaps alternate. In that case even k give the larger of the two long lengths (k+1+e)/N and odd k give (k+1)/N. The central and nearest even cuts yield m²+1 and m²+2e+e² after multiplying the squared constant by 4N, so exactly e≤√2−1 is allowed. At N=2 the formula specializes to (1/4) max(1,2 max_i g_i²). Replay: RESULT.md lines 26–46. CHECK.py and VERIFICATION.md were inspected but not executed; their recorded finite rational checks are not the proof.

## originality

PASS

The derivative-measure reduction is a standard idea. The supported distinct result is the exact all-N Euclidean trace-design law with continuous mean and the complete optimizer classification, including a bounded nonuniform alternating family. Inspected scalar discrepancy, BV boundary trace, and Hilbert sampling results do not establish it. This is best-knowledge comparison, not historical priority.

## value

PASS

The theorem gives both the worst possible centered sample deviation for a given design and exactly which node placements minimize it, even when equally spaced sites are not the only optimum. The parity-dependent rigidity and quantitative tolerance for alternating gaps are useful to anyone choosing sites under a total variation budget; the result is not limited to a toy size or a finite sweep.

The dated certificate retains the supplied scientific assessment, sources and limitations.
