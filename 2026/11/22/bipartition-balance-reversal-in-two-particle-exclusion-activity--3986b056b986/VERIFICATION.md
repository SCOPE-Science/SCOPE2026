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

Every accepted hop changes the shore-occupancy class by one, so the three-class rate reduction loses no counted events. Under uniform pairs the class masses are r(r-1), 2rs, s(s-1) divided by n(n-1); the exit rates are 2s, n-2, 2r respectively, with an absent class omitted. Independently, complete returns from the mixed class AB to itself are iid regenerative cycles of two hops. For a=n-2 the cycle duration is Exp(a) plus an independent mixture of Exp(2s) and Exp(2r), with respective weights (r-1)/a and (s-1)/a. Writing H=(r-1)/(2sa)+(s-1)/(2ra), its mean is 1/a+H and its variance is 1/a^2+2[(r-1)/(a(2s)^2)+(s-1)/(a(2r)^2)]-H^2. The delayed renewal formulas give mean rate 2/E[X] and Fano ratio 2 Var(X)/(E[X])^2; the initial and terminal partial cycles do not change the long-time rates. This yields exactly the claimed rational functions (symbolic difference zero); a bounded exact rational check over every unordered shore split at n=4–30 confirmed the result. For example the star and balanced values change from 26/25 and 53/50 at n=5 to 10/9 and 26/25 at n=6. The coefficient n^2-6n+4 is strictly negative for n=4,5 and positive thereafter. The four-site star has constant rate 2 at every accessible state, hence genuine Poisson activity; all other cases have F>1. Dividing the formula by its leading denominator gives the stated macroscopic limit, not process convergence. Replay: python3 /workspace/review_evidence/check_1_2_4.py.

## originality

PASS

The arbitrary-graph mean, Fano Green identity, universal nonnegative excess and four-site star equality are already covered. The square's 10/9 case appears in earlier Hamming work and also in distinct same-date cycle work. The surviving new claim is the evaluated Fano ratio across all positive shore sizes, with the strict balance reversal and dense-imbalance limit. Ordinary-generator spectra and the general Green formula do not provide this response to partition imbalance without an additional activity calculation.

## value

PASS

The closed law gives the entire accepted-jump noise ordering across bipartitions at fixed vertex count. The reversal between five and six and the persistence of the excess under dense relative imbalance are meaningful comparisons that are not evident from the earlier inequality or the ordinary exclusion spectrum. This separates effects of topology on count fluctuations from effects on the mean rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
