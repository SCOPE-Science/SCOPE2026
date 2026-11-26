---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For each lag j=t-k-1 the exact probability lies between (1-q)q^j and q^j. Independent Bernoulli choices yield the uniform log moment bound m[s²/(2β)+Oβ(s+1)] by splitting the geometric product at j=floor(s/β). At s=βr/m this gives log upper tail at most −βr²/(2m)+O(r+1). Requiring all m hits at the first h=ceil(r/m) arrivals costs at most βmh(h−1)/2−mh log(1−q) in negative log probability, with the same leading coefficient. Taking disjoint birth intervals gives order n/(h+1) independent witnesses, without assuming independent degrees. The upper union bound and lower no-witness probability are summable at n=2^j at the respective (1±ε) thresholds. Monotonicity and consecutive dyadic log ratios extend the simultaneous rational-ε bounds to all n; the root convention and a uniform additive m compare the two maxima. This verifies the almost-sure limit for fixed m and β and with multiplicity only. The inspected artifacts/verify.py is a replay of finite rational identities, not the limit proof, and was not executed.

## originality

PASS

The supported distinction is the sharp first-order maximum law, not introduction of the model. The same one-parent model explicitly left maximal degree open; the same general-m model is used in work on random walks. No checked statement or implication gives the frozen maximum asymptotic for geometric weights.

## value

PASS

The maximum was an explicit gap for the one-parent model. The first-order limit distinguishes exponential age bias from logarithmic-degree behavior in uniform models, and the factor √m quantifies the effect of independent multiplicity rather than merely bounding the maximum. Neither fixed-vertex degree laws nor graph-walk behavior answer this question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
