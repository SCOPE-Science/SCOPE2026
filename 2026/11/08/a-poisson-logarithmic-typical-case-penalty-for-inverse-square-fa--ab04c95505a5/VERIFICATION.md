---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For sorted uniform locations, omitting report i costs its nearest-neighbor distance δ_i and its lottery probability is δ_i^-2/Σδ_j^-2. With n-1 facilities, the optimum is the minimum adjacent gap g*. Thus exact conditional expected approximation ratio R_n=(Σδ_i^-1)/(g* Σδ_i^-2). Uniform spacings are normalized iid exponentials, whose common normalizer cancels. The adjacent-minima identity produces A_n=2ΣE_j^-1-Σmax(E_j,E_(j+1))^-1 and analogous squares. The first sum divided by n log n converges in probability to one by truncation while corrections have finite mean; the square sum is controlled by its extreme point process and corrections vanish on n² scale. Joint scaled minimum and square sum converge to the first and all inverse-squared arrivals of a unit-rate Poisson process. Slutsky yields R_n/log n => 1/(T_1 Σ_j T_j^-2), strictly positive nonconstant. Independent exact rational profiles (3<=n<=7) checked cost ratio and adjacent corrections; numerical samples cannot prove the limit.

## originality

PASS

PASS best-knowledge: Chan–Lin–Wang first give the Inverse-Square omission mechanism and tight worst-case order sqrt n; their inspected mechanism and main approximation results do not establish the conditional expected approximation ratio on iid uniform one-dimensional report profiles. Related one-omission and gap-product published findings concern different omission probabilities or worst-case bounds. The Poisson nearest-spacing extremes and harmonic denominator yield a distinct new distributional typical-case law. Any hidden appendix or unindexed average-case treatment remains a priority risk.

## value

PASS

PASS: The same mechanism exhibits a marked gap between worst-case square-root distortion and typical logarithmic divergence, with a genuinely random nondegenerate explicit Poisson limit. The exact conditional cost formula makes clear this is not a single realized lottery outcome, and the limit gives quantifiable risk for a natural random population model beyond worst-case analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
