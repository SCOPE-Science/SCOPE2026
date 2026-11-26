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

For positive t, the differentiated integrands of H are bounded locally in t even for unbounded K; at t=0 the first moment suffices. H'(0+)=γ−μ<0, H''>0, and there is an ε>0 with positive mass on K≤γ−ε, forcing divergence of H. The unique minimum c*=H(t*) is in (0,1). The exact ratio (1−F(v))/(1−v)=H(t) gives a global supporting line with just the two contacts v* and 1. Up to v* the derivative F'=H−H'/γ decreases strictly from μ/γ to c*, so the joined curve is the least concave majorant and optimizing over the entire closed interval gives all four regimes, including the two-maximizer c=c* case and the unique zero optimizer at c=μ/γ. The positive-time return of H to 1 proves the unique surplus crossing. For the witness, e^(t*/2)=√3; the partial slope equation is q+9/q=8c with q=e^(t/2) in (1,√3), confirming the smaller root, crossing v=8/9, and both partial-branch limits.

## originality

PASS

Passes to best current knowledge for the sharp optimizer classification with arbitrary initially present rate mixture within this ideal single storm, not for concave-envelope methods, heterogeneous wash-off generally, or engineering tank optimization. The closest indexed delayed-exponential paper has material overlap in mass–volume curves and crossings but not the objective, model hypotheses or optimizer law. The closest independently inspected primary passages have short/long wash-off components and engineering design comparisons but use different rates, decision variables and merit functions.

## value

PASS

The problem asks whether increasing a per-volume cost favors less of a storm gradually or produces a discontinuous full-to-partial switch. The unique cost tie, complete branch and crossing formulas are useful as an exact benchmark for heterogeneous first-flush design heuristics. They are not just application of an envelope to a known empirical curve: the result identifies precisely the contacts and strict branch structure for every admissible initial-stock law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
