---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The cited scheme multiplier agrees with the paper's equation (11) at z=-a, and independence gives the exact power of F_a(p). For 0<a<=2 the multiplier contracts almost everywhere. For a>2 the log-amplification is integrable, has negative mean [(a-1)log(a-1)-(a+1)log(a+1)]/a and is strictly positive on a set of positive measure. The strong law gives the negative trajectory exponent (also for 0<a<=2), and strict cumulant convexity gives exactly one positive crossing, with the claimed signs. The uniform exponential bound follows by separately bounding exp(delta Z_a) by u^(-delta) and exp(-delta Z_a) by (3/2)^delta |u-(1-1/a)|^(-delta), for 0<delta<1 and a>=2; it controls the third cumulant derivative in a fixed smaller neighborhood of zero. The logistic limit gives variance pi^2/3 and a strictly positive limiting cumulant at fixed 0<p<1, forcing the critical p to zero. Dividing the Taylor expansion at the root by p and using the mean asymptotic -2(log a+1)/a proves the stated coefficient. The source verifier was inspected, not executed; the analytic proof supplies the unbounded assertions. S1 is semi-implicit and S2 fully implicit, as in the paper's collective terminology.

## originality

FAIL

A distinct indexed theorem gives the same entire moment boundary in inverse coordinates, including the equivalent sharp stiff-limit coefficient, and additional results. This is a failure of distinct mathematical coverage relative to the checked corpus, not a finding that the October 25 catalogue item predated the October 18 item or that the frozen theorem is false.

## value

PASS

The full negative-ray classification and sharp collapse rate are substantive mathematical information: they quantify how increasingly rare expansions destroy every fixed-order moment stability while pathwise stability persists, a distinction a single mean-square cutoff cannot express. This assesses the scientific importance of the mathematical question and its answer, not a separate novelty credit for the frozen item.

The dated certificate retains the supplied scientific assessment, sources and limitations.
