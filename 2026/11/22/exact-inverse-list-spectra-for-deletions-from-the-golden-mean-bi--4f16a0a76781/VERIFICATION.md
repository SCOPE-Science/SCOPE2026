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

The claim in RESULT.md lines 4–40 fixes the receiver y and counts distinct 11-avoiding binary parents, not masks, even for m=0 or d=0. Match each receiver symbol at its earliest available occurrence. The skipped prefix for that symbol consists exclusively of its opposite, so this greedy parsing counts each parent once. Before a matched 1 the skipped zeros are arbitrary except for a mandatory zero after a previous matched 1; together these factors are t^r/(1−t)^k. Before each matched 0, a skipped 1 is allowed precisely at the start or after a matched 0. The suffix contributes (1+t)/(1−t−t²) after a final 0 and 1/(1−t−t²) after a final 1; including the suffix yields a=m−2k+r+1 optional factors. For the empty receiver the unrestricted legal suffix gives the same series. The t^r shift gives the threshold, and the remaining series has constant term 1 and every positive-degree coefficient at least 2 because a+k≥1 and the Fibonacci factor has positive coefficients. Compositions of the k ones into k−r runs and allocation of the zeros give the stated multiplicities. Weighted last-bit transitions (only 1→1 has weight u apart from the z per bit) give G(z,u); the singleton layer is r=d, and summing layers gives G/(1−u). For j≥1 the coefficient of u^j is z^{j+1}(1−z)^{j−1}/(1−z−z²)^{j+1}. At α=1/φ, 1−α=α² and −αB′(α)=1+α², giving the recorded leading constant c_j, also valid at j=0 from (1+z)/B(z). The other pole has larger modulus. For fixed d≥1, only the ratio of the d−1 and d layers contributes at order 1/m; c_{d−1}/c_d=d(φ³+φ)=(3φ+1)d. A small direct check at m=3,d=1: 000 has five parents, 010 has four (0010,0100,0101,1010), 011 has the sole parent 0101, and 111 has none. The frozen VERIFICATION.md and verify.py were inspected, not executed; their finite distinct-parent and transfer tests support, but do not establish, the all-length bijection or the asymptotic.

## originality

PASS

The distinct content supported is the one-sided golden-mean constraint's exact distinct-parent distribution/all-radius generating function and resulting singleton law, not greedy subsequence matching, the Fibonacci source count, or binary run enumeration by themselves.

## value

PASS

The simplest one-sided binary finite-type restriction produces nonconstant inverse deletion lists, unlike the unrestricted source. The law computes each list from readily measured receiver statistics and identifies exactly when decoding is unique even though deletion masks may be ambiguous. The fixed-radius proportion approaching one with an explicit first correction quantifies this effect for feasible receivers, not for the distribution produced by uniform parents or random masks. This is a useful exact benchmark without claiming a deletion-correcting code construction or a larger universality theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
