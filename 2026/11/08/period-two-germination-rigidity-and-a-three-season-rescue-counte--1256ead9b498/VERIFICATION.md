---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The symbolic verification computes the two-season characteristic trace and determinant, expands and factors \(P_g(ab)\) and \(P_g(as)\), and exactly reconstructs the period-three projection products at the specified germination fractions. The independent rational-arithmetic routine checks 1,235 admissible parameter/policy configurations and the three exact matrices. Run `python verify.py` with Python and SymPy installed.

The proof of the infinite-domain theorem does not rest on samples: convexity bounds the trace; two factorizations and eigenvalue location prove the global maximizers and strictness. The period-three growth/no-growth boundaries are exact algebraic inequalities rather than finite-time simulation.

The modeled output is the population's linear expected-abundance multiplier, not an extinction probability. Literature comparisons were restricted to accessible full text and available abstracts, so independent historical-priority validation remains outstanding.
