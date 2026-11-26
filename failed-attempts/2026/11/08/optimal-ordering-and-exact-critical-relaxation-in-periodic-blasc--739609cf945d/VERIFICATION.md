---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The Cayley transform gives w'=λw/(1+(λw/2)^2) on the stated radial interval. Divide w_n by the periodic positive prefix product P_j; the inverse square Z then gains exactly 2c_j+c_j²/Z with c_j=P_(j+1)²/4. Positivity yields linear growth and convergence from all x_0<1, including zero. Summing the inverse-Z term gives Z_(mk+j)=2Ck+O(log k) for every fixed phase. Its block sum differs from D/(2Ck) by O(log k/k²), absolutely summable, which proves the finite centered limit. Using 1−x=2w/(1+w) gives the stated intermediate-phase limit. A nontrivial adjacent swap affects exactly one prefix product and orders C strictly; only equal entries tie in such exchanges. Thus the extrema are unique as value words, not a claim that arbitrary nonextremal permutations have different values. The fastest/slowest comparison is at phase zero, or equivalently for words ordered starting at the observation phase. The exclusion x_0=1 is necessary for the inverse-square coordinate.

## originality

FAIL

A distinct earlier catalog statement covers the same map family, exact neutrality, all finite periodic words and real initial states, and proves the identical coefficient law with a sharper error and stronger sorting assertion. The only ostensibly additional phase limit follows directly by rotating the word, or by the earlier partial-composition expansion. This is demonstrated mathematical coverage, not an inference from date alone.

## value

FAIL

Sharp schedule dependence is mathematically meaningful, but the submitted result adds no independently useful unknown mathematical conclusion beyond the stronger existing theorem. Re-expressing its coefficients and evaluating examples, or taking its leading law at a rotating period start, does not supply additional scientific value under this review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
