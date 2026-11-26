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

For u=x^p-y^q, small negative y gives u>=|y|^q>|y|^r, so the negative region occurs only at positive y. On |u|<y^r both inverse x roots exist, and their combined Jacobian is comparable to y^{-gamma}, gamma=q(1-1/p). With u=y^r v the negative integral has y power r(1-2s)-gamma; the v integral is finite for s<1 and the y integral diverges at equality r(1-2s)-gamma=-1. This gives beta<1/2; higher s then diverge by monotonicity. The negative-y wedge |x|<=|y|^(q/p) has f comparable to |y|^(2q) and proves divergence on the positive side at alpha=(1/p+1/q)/2. For s<alpha, the positive portion of |u|<2y^r uses the same y exponent as the negative strip, plus only simple v=+/-1 poles, and converges since alpha<beta. The complement is dominated by |x^p-y^q|^(-2s): in the near-cusp region scaling x=|y|^(q/p)v gives y power q/p-2qs and at most simple v poles, while the x-dominant region gives x power p/q-2ps. All exponents pass exactly as needed. The two factors have primitive parametrizations y=t^p, x=t^q times units, with first coprime exponent q; the factor ideal equals (x^p-y^q,y^r), of colength pr. The beta formula is strictly increasing and invertible for r with fixed p,q. Independent finite consistency checks: 18 threshold boundary and exact Groebner-basis cases with python3 /workspace/branches/reproduce_records_1_to_4.py; they do not substitute for the all-parameter analytic argument. Frozen verification and same-model audit were read, not counted as independent evidence.

## originality

PASS

Best-of-knowledge pass for the explicit two-sided contact law, not for ordinary RLCTs, Puiseux computations or general signed resolution. The ordinary threshold forgets r and no independently located catalogue statement covers the negative threshold or the complete signed pair. The closest cited full-text comparisons remain access-limited; the restricted hypotheses as reported by the frozen package are consistent with the independently checked nondegeneracy and reducibility distinctions, but are not a whole-paper exclusion.

## value

PASS

A natural Newton-degenerate reducible cusp family exhibits a measurable geometric distinction: fixing both individual characteristic pairs and the ordinary real threshold does not fix the signed negative threshold, which determines the intersection multiplicity pr. This is an exact parameter-complete local example, neither a general resolution method nor a claim about unrelated real branches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
