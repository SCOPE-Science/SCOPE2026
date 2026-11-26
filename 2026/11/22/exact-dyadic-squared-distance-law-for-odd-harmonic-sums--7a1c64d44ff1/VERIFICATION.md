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

Put n=b−a>0 and c=b+a. For n odd, both sides have valuation zero. For n=2m, c is even and positive; pairing the denominators c±(2i−1) gives O_b−O_a=2cT with T=Σ_{i=1}^m 1/(c²−(2i−1)²). An independent direct congruence proves the key valuation without an infinite series: for s=ν₂(m), put f(x)=1/(c²−x²) on odd x. For every r≥1 the square difference (x+2^r)²−x² is divisible by 2^{r+1}, so the same holds for the difference of the corresponding f-values since their denominators are units. Induction by pairing odd representatives x and x+2^r in modulus 2^{r+1} now gives Σ_{x odd mod 2^{s+1}}f(x)≡2^s mod 2^{s+1}, starting with f(1) odd. The m odd denominators' deviations comprise m/2^s complete systems, so T≡m mod 2^{s+1} and ν₂(T)=s. Thus ν₂(2cT)=ν₂(nc). The written proof instead obtains the same congruence from inverse even-power sums; its geometric series converges since c is even, and its tail is divisible by 2^{s+2}. This covers every shifted interval with a≥0, including a=0; for equal indices both congruences hold trivially. An independent exact-fraction test matched all 820 pairs with 0≤a<b≤40, e.g. O₃−O₁=8/15. The finite test is corroboration, not the proof.

## originality

PASS

The distinct claim is the valuation for every pair of nonnegative indices and the resulting square-collision equivalence, not the fixed-start formula, the aligned-block case, or the reversal-pairing technique. The inspected sources contain all three of those antecedents but do not cover the arbitrary-interval valuation.

## value

PASS

The theorem gives a usable exact two-point invariant of a classical rational sequence: two harmonic values collide modulo 2^r exactly when their indices have equal squares at that modulus. It also evaluates all shifted intervals without computing their denominators or sums. This is structurally stronger than the one-point and aligned-block valuations, and not a numerical slice or a repackaging of the reversal trick alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
