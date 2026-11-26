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

For fixed c>1 and x>0, h'(x)=h(x)(h(x)/x−1)>0 by the strict integral bound E1(x)<exp(−x)/x. Thus the log-ratio slope h(x)−h(x/c) is positive, and the small- and large-argument expansions give the endpoints 1 and infinity. Inverse differentiation gives the stated scalar relative condition number. With L=−γ−log x and a=log c, the E1 series gives h(x)=1/L+o(L^−2) and h(x/c)=1/(L+a)+o(L^−2); the difference is asymptotic to a/L². Also R−1 is asymptotic to a/L, giving both claimed forms. These statements concern the recovered ratio parameter x, not the full inverse for (T,S) or a stochastic noise model.

## originality

FAIL

Theis already gives the full forward formula and two-observation recovery in the precise same-place setting. The record's sole quantitative refinement is its direct scalar inverse log derivative: subtract the log-sensitivity rows of the two prior drawdown expressions and reciprocate. The common standard exponential-integral expansions then give the endpoint and late-time statements directly. Failure is for mechanical coverage, not a claim that a prior source prints the same condition-number notation or that the mathematics is false.

## value

FAIL

Weak identifiability at late times is a natural applied concern, but the exact number claimed here is a routine scalar derivative of the known drawdown response, and its singular scaling follows directly from the classical logarithmic form. The record supplies no additional recovery limitation or observational conclusion beyond that in this particular choice of relative coordinates; in particular it does not analyze measurement errors in drawdown or sensitivity of both recovered parameters. The explanatory calculation is correct, but not a distinct scientifically valuable exact invariant under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
