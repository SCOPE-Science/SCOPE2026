---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For Basic Chebyshev isotonic selector B_n(a)_i=(prefix maximum + suffix minimum)/2, the midpoint between least and greatest uniform-error isotonic fits is a true L∞ best approximation. On each strict input-rank chamber its Jacobian preserves constants, and global two-input Gini Lipschitz equals the maximum chamber Jacobian norm along line segments. Every Gini seminorm direction decomposes into nonnegative binary superlevel cuts, reducing each Jacobian norm to all nontrivial cuts modulo complements. Independently enumerated exactly 2+18+168+1800+22320 chamber/cut pairs for n=2..6 with rational arithmetic; sharp moduli 1,1,1,1,9/8. The explicit 6-input same-chamber witness gives 9/8. The all-n half-block perturbation gives lower floor(n²/4)/(2(n-2)), while positive row-stochastic Jacobians and cube maximum bound yield upper floor(n²/4)/(n-1). n>6 constants are bounded, not claimed exact.

## originality

PASS

Best-of-knowledge novelty after comparing exact claims and implications, not title matches; the identified structural prior inputs are explicitly credited and all material access limits retained. No inspected earlier theorem implies this complete final claim.

## value

PASS

The Basic unweighted Chebyshev selector is a classical canonical isotonic fit, and its two-input complete-pair Gini stability is distinct from sup-norm approximation and ordinary adjacent total variation. The sharp first expansion at exactly six observations and unbounded order-n sensitivity matter for robust dispersion stability; finite exact cutoff plus analytic all-size bounds are mathematically motivated beyond code correctness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
