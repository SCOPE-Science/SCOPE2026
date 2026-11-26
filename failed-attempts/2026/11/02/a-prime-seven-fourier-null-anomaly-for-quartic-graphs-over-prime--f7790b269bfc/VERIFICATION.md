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

For a primitive frequency, f(x)=ax+bx^4 has derivative not identically zero modulo p. Expanding f(x0+pz) modulo p² and summing the z digit gives p times the root-of-unity sum over the derivative's roots. There are at most three terms. A nonempty sum of fewer than p such p²-th roots cannot vanish: its integer exponent polynomial, if divisible by the monic Phi_{p²}, would have value at 1 divisible by Phi_{p²}(1)=p, contradicting its term count. For b nonzero modulo p the derivative condition is a cube-image criterion, with 1+(p-1)/gcd(3,p-1) admissible reduced a values, each with p² joint lifts. The imprimitive sum is p times a prime-field sum of p roots, whose exact zero criterion is equal output multiplicities, i.e. a permutation. B=0 and A nonzero is linear; A=0 and B nonzero fails because x and -x agree. The verified Masuda–Zieve bound rules out p>=17 for the remaining binomial, and the independent census gives only c=3,4 at p=7 among all candidates at 5,7,11,13. The extra 12 at p=7 follow from six B choices per ratio. Finite character diagonalization counts all surviving coefficients; the rank expression and limits follow, with origin nonzero and p=2,3 excluded. Independent exact full-frequency checks for 5,7,11 found ranks 521,913,13421. Neither this finite corroboration nor the source script is used to extrapolate across primes.

## originality

FAIL

The exact prime-seven exception, including both ratios and the entire imprimitive null count, is already the explicitly classified origin-translation block in Resultary 1f76e4a64221, after multiplying by p² and reversing frequency signs. The distinct prime-square primitive sector is an immediate specialization of Cochrane–Zheng §4's local sum formula, followed by the standard cyclotomic noncancellation for fewer than p terms and the cube-image count. Consequently the full stated support and rank, though presented for a different operator and not literally listed in the earlier sources, follow directly with no new classification step. This is a demonstrated implication, not a failure based on inaccessible literature or a claim that the earlier Gabor operator is itself the convolution operator.

## value

FAIL

Quartic graph Fourier support is a natural operator invariant, but the prominent arithmetic anomaly is already an identical prime-field block and the remaining contribution is the routine cube-image and lift count after the established prime-square formula. The finite rank table corroborates correctness but adds no new structural arithmetic or independently useful unknown exact fact beyond that direct implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
