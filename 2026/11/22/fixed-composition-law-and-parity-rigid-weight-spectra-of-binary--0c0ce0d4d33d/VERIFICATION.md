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

Equality of prefix and suffix ones counts at length j is equivalent to equality at the complementary length, so the inward walk needs only floor(n/2) pairs. Its steps cannot jump across zero. On the positive path the first pair has weight u, and reflection at height zero preserves the later step weights, including the two distinct horizontal colors. Summing the difference of unrestricted path counts over positive end heights leaves Laurent coefficients at 0 and 1 of (1+uz)^(m−1)(1+u/z)^(m−1). Pair reversal doubles the count while preserving composition; the middle bit is free at odd lengths. This verifies the products and support, including the empty second sum at m=1. The even middle coefficient is the geometric mean of the neighboring squares, while strict binomial log-concavity gives strictness at odd interior indices. For convolution with (1+u), the deficit is the sum of two neighboring deficits and a cross term nonnegative by ratio monotonicity; at least one of the neighboring deficits is positive, including the support ends with zeros padded. The falling-factorial Vandermonde calculation gives the asserted second falling moment and then the variance; adding the independent central bit contributes 1/4. Independently, for even weight k=2j the conditional probability is 2p_m(1−p_m) times binom(m,j)^2/binom(2m,2j); for odd weight k=2j+1 it is (m−j)(2j+1)/m² times that same ratio. Applying Stirling uniformly on compact current-density intervals gives the claimed constant in both parity cases. Pascal's identity makes the odd-length case a convex mixture at adjacent even-length weights. The uniform assertion is understood in the quantitative sense of line 72, with the current density in the leading term; replacement by a limit p is along a convergent sequence.

## originality

PASS

Qualified to the evaluated fixed-weight refinement and its parity, moment and sharp bulk consequences, not the walk bijection, independent middle bit, ordinary reflection method, or total counts. The older colored-path bijections encode the weight information, making the refinement natural, but the inspected prior results do not give the evaluated fixed-weight law or its consequences.

## value

PASS

A weight layer is a natural constrained binary source. The old total cannot distinguish how border avoidance varies across such layers. The sharp bulk probability, the exact variance in the other sampling ensemble, and the alternating log-concavity equality set give concrete useful structure beyond re-enumerating the old length sequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
