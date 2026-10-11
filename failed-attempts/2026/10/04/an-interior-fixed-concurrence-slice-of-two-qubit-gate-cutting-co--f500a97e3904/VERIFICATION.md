---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The two non-perfect-entangler Cartan branches at \(C_{\max}=1/2\) are \(\theta_1+\theta_2=\pi/12\) and \(\theta_2+\theta_3=5\pi/12\). Weyl-chamber ordering gives the valid bounds \(g_t\le(5-2\sqrt3)/12\) and \(g_t\ge3/4\). Substitution into the source's exact monotone gate-typicality envelope \(F(g)=1+3g+3\sqrt{g(4-3g)}\) yields the two separated cost bounds; the two stated Cartan points realize values on opposite sides. The inequalities are symbolic; the bundled grid is only corroborative.

## originality

FAIL

The result is a mathematically correct but direct corollary of exact formulas and envelope theorems already published together in Hart's paper. Fixing \(C_{\max}=1/2\), applying Weyl-chamber ordering, and feeding the resulting elementary \(g_t\) bounds into Hart's sharp \(\gamma\)-versus-\(g_t\) envelope is enough to obtain the claimed forbidden interval. Under the required implication standard, the fact that Hart did not print this slice and mentioned topology as future work does not make this corollary original.

## value

PASS

An explicit interior disconnected slice is a meaningful geometric diagnostic for feasible gate-cutting cost and answers a natural slice of the attainable-set topology question. The failure is originality, not mathematical usefulness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
