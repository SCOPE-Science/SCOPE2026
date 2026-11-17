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

Generator for monomial x^i q^j includes reset term -r 1_{i>0} M_ij, X-Q drift, and independent noises. Positive-parameter quadratic and quartic systems yield M20=2U/(rV), M40=24WH/(r² VJ), κ=6WVH/(U²J)-3; denominators positive for g,r>0. Exact rate derivative has 7th-degree numerator with three parameter-dependent sign roots strictly ordered (p2 root 0.1–0.2, p1 0.4–0.5, p0 0.7–0.75), implying by Descartes exactly one positive minimum for 0<g<g_c and no stationary rate for g≥g_c. The all-positive bath-derivative polynomial ensures strict decrease of κ in g; simple-root implicit expansion yields r*(g)~1/g-5/6 and positive linear extinction at g_c. Contractive reset-time affine recursion justifies unique steady state and moments. Independent SymPy recomputation confirmed p0=6(g+1)²(2g+1)(22g⁴+25g³-15g-6), g_c=0.7459581983862532 and positive-root sign changes at g=0.1,0.5 versus g=0.8,2.

## originality

PASS

Best-of-knowledge original sharp rate/parameter classification, beyond the underlying exact stationary kurtosis formula in Santra–Das (2026). The original same-model paper includes the selective reset, moments, limiting regimes and parameter-plane plots but no global one-critical-point/no-critical-point theorem, unique quartic threshold, strict bath-injectivity proof or optimizer asymptotics in inspected sections. Deriving them from known κ requires a nontrivial uniform seventh-degree polynomial sign ordering; not a mere change of variables. A missed implication elsewhere remains possible.

## value

PASS

A sharp parameter bifurcation separates unique finite optimal reset cadence from monotone κ-response, despite variance decreasing with rate throughout. The explicit quartic threshold and two endpoint scaling laws are natural, experimentally interpretable consequences of memory retained by a viscoelastic bath, not an arbitrary small-parameter optimization. Strict monotonicity in bath parameter gives a stationary-shape identifiability criterion within this model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
