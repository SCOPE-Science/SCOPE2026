---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: For L=log u and x=-xi in [0,1], direct differentiation of S/chi=(1-x)[(1+delta)(exp(Lx)-1)/x-L] gives S'/chi=L-(1+delta)H_+(x) in compression. At x=0, H_+=L-L^2/2; at x=1, H_+=exp(L)-1>L. Writing F(y)=(exp(y)-1)/y and B(y)=y+2F'/F'' gives H_+'=L^2F''(B-L). The decisive identity 3F''^2-2F'F''=exp(y)[exp(y)(y^2-4y+6)-2y-6]/y^4>0 follows since its bracket has q(0)=q'(0)=0 and q''=y^2exp(y)>0. Hence B increases from 3 and is >y, so H_+ either increases or has exactly one minimum; its threshold level has precisely the claimed crossing. For expansion, g_- integral from 0 to ell of exp(-sx) has g_-'<0 and g_-''>0, so H_-=g_--(1-x)g_-' decreases, giving eta<ell/(2+ell). The duration logarithm is positive strictly concave at both physical signs, so (1-x)K(x)/x decreases; endpoint duration is finite for fixed mismatch. Implicit derivatives at the boundary verify both linear onset coefficients. Independent SymPy verified the nonstandard q-identity and sample sign cases; this is not an infinity proof.

## originality

PASS

Qualified PASS for the complete compression/expansion mismatch phase boundary, uniqueness and linear endpoint onset. Fu et al supply the original entropy and duration expressions and selected nonmonotone examples; searched Resultary findings did not reveal an older theorem proving the global threshold surfaces, but full source manuscript was inaccessible and no novelty certainty is claimed.

## value

PASS

PASS: An interior entropy-production maximum is a central physical diagnostic of the prescribed polytropic stroke. Exact initial-temperature-offset thresholds distinguish a peak from monotonic entropy generation and resolve the previously illustrated nonmonotonic behavior with nontrivial global shape control, including large compression ratios; mathematically significant parameter boundary, not a trivial substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
