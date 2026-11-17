---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For unit-scale BetaPrime(a,b), the score g=((b+1)x-(a-1))/(x(1+x)) gives derivative hprime=h(h-g). For a>1, g is negative up to m=(a-1)/(b+1), rises then falls with one positive maximum at c, and for x>=c the survival/density ratio satisfies S/f>1/g, forcing h-g<0. On the rising-score interval every zero of h-g has strictly negative derivative, establishing exactly one interior maximum; a<=1 decreasing by increasing density-shift ratio. With a=1+ε and x=ε+ε²z, |z|=O(|log ε|), uniform beta-function and incomplete-survival expansions yield h-g=ε[b(log ε+ψ(b+1)-ψ(1))-z]+O(ε²log² ε). Its derivative is -1/ε+O(|log ε|), so the root error is O(ε³log² ε); the height follows from h expansion. Uniform only for b on compact subsets of (0,∞), ε→0+. Exact a=2 rational formula and mpmath numerical checks corroborate, not prove asymptotics.

## originality

PASS

Best of knowledge: prior Beta-prime hazard-shape and generalized F survival analyses discuss decreasing versus arc-shaped hazards or ageing classes, but no inspected accessible theorem contains the shape-dependent ε² log ε displacement and ε log ε height asymptotic at a↓1. Full Cox (2008) and Glaser (1980) inaccessible due disconnected authorized Oxford VPN; they remain material priority risks rather than grounds for automatic rejection.

## value

PASS

The beta-prime hazard changes structurally from decreasing to a unique interior maximum at a=1. The peak position and height are natural survival-analysis invariants; their sharp logarithmic boundary-layer correction and explicit b-dependence are not determined by a known qualitative shape classification or by a routine table lookup. This is a motivated quantitative onset theorem for a two-parameter family with controlled error, not an unsupported microscopic improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
