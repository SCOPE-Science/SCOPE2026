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

Equations (8), (10), and (15) of arXiv:2311.15359 give exactly the specified floor-based rank sets and fixed population normalizers. The extended sine-power bump is C3, with first three derivatives zero at the joins; the derivative of the perturbed quantile is everywhere greater than 0.8015. The inverse thus has a positive C2 density, and tail equality plus change at the midpoint excludes the entire Lévy scale family. The claim for the displayed density is C2, not C-infinity; genuinely C-infinity compactly supported bumps also work under the monotonicity condition. Under common uniforms, both samples maintain ranks and agree on every used order statistic when N_p>=k and N_q<ell. The coupling inequality gives the TV bound, hence also controls every rejection probability based on this statistic. Stirling at the near-threshold masses and Chernoff upper bounds prove the two binomial exponents, with the lower excursion dominating. Conditional on N_p=k-1, the added count up to q is Bin(n-k+1,1/2), and lies between 1 and ell-k with probability tending to one. That event strictly raises the lower band while leaving the upper band unchanged, proving the matching exponent for this coupling only. The one-point CDF separation distinguishes the full samples. No sharp TV lower bound or ensemble-test conclusion is inferred.

## originality

PASS

The exact published statistic and rank geometry are established, as are the coupling and binomial tools. The supported contribution is the construction of fixed smooth nonnull alternatives that are invisible in the whole statistic law at an exponential rate, with a matching exponent for the specified coupling. This is stronger than equality of population conditional means or of local first-order behavior.

## value

PASS

The result exposes a concrete detection limit of an actually specified goodness-of-fit test, uniformly over all rejection rules based on its statistic, even though an elementary statistic on the full data separates the same alternatives. Explicit finite-n error bounds and the sharp coupling exponent quantify the effect without overclaiming a TV lower bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
