---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Read the frozen statement, proof and all supporting files. In deficit coordinates δ=1−x, v=y, the new deficit is nonnegative because (1−δ)e^δ≤1, and the new v is positive and at most v. Uniformly for 0≤δ≤Kv, the updates are δ′=av+O(v²) and v′=v+O(v²), so K>a gives δ′<Kv′ for sufficiently small v, including the δ=0 boundary. Since δ′≥av/2 in a smaller wedge, a positive limit of the nonincreasing v would eventually force a uniform contraction of v, a contradiction; v→0 and v′/v→1. Independently recovered the quadratic graph coefficient B=a²(d+1)/2 and reciprocal increment ad/2+[3a²d(d+1)/8]v+O(v²) from the formal expansion. This formal computation applies to actual wedge orbits: the graph H(v)=av+Bv² has defect O(v³), H(v) is inside the same wedge for sufficiently small v, and the transverse derivative of D−H(V) is O(v) between δ and H(v). For the scaled error |δ−H(v)|/v³ the resulting multiplicative coefficient is O(v)(v/v′)³→0 and the forcing is bounded, so it remains bounded. This yields a controlled fourth-order remainder for the cubic v update, not just a formal center graph. Positive reciprocal increments in the limit give 1/v_n∼(ad/2)n; one further summation gives 1/v_n=(ad/2)n+O(log n). Substituting back leaves an absolutely summable O(log n/n²) increment error after removing the linear term and (3a(d+1)/4)/n. The harmonic sum minus log n converges, proving the finite orbit-dependent constant and the unavoidable positive coefficient. The uploaded SymPy checker and numerical diagnostics were read, not run.

## originality

PASS

Qualified best-of-knowledge pass for the model-specific cubic correction and finite renormalized clock on the wedge, not the original map, threshold, quadratic slaving, leading rate, or the general reciprocal-increment method. The strongest same-map paper was identified via its publisher and abstract, but independent full-text access was unsuccessful; the frozen package's precise report on its quadratic calculation is not represented as independently verified source reading. Open analogous clock results were compared by equations, parameter surface, and observable, not by title alone.

## value

PASS

A reciprocal decay rate at neutral invasion is a natural deterministic timing observable for this published map. The exact logarithmic drift is detectable beyond the leading algebraic law and cannot be tuned away by a change of initial state. The finite orbit-dependent correction is proved on an entire positive invariant wedge rather than a formal center curve. The general iteration device is standard; the value is the controlled coefficient and range of validity for this specific nonlinear threshold, not general or empirical ecological significance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
