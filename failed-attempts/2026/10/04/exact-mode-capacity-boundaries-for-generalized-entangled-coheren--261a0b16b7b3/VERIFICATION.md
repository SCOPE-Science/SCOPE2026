---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Starting from the source normalization equation Ab^2+Bbc+c^2=1, real c exists iff b^2<=4/(4A-B^2), and A-B^2/4 simplifies to d(1-t)(1+dt). Substituting the source linear and nonlinear unconstrained optima and writing s=sqrt(d) gives exactly the two strictly increasing cubics stated, hence iff root boundaries. Independent numerical evaluation at x=16 gives R_L^2 approximately 255.75065 and R_N^2 approximately 17.01439, so capacities 255 and 17. The large-x leading laws are x^2 and x^2/16. The frozen RESULT contains a local malformed TeX expansion `\frac1004+\frac18`; the correct expansion is x/4+1/8+O(x^-2). This defect does not change the stated boundary/asymptotic conclusions but is a scientific-text error.

## originality

FAIL

The Liu--Lu--Sun--Wang primary paper already supplies the exact normalization ellipse/bound |b|<=Gamma, both exact unconstrained optimal coefficients, and reachable/unreachable regions for those optima. The submitted cubic boundaries are obtained by direct substitution of those published formulas, the change of variable s=sqrt(d), and elementary algebra; the floor capacities and factor-16 asymptotic follow from the same inequality. Under the required implication-level standard, an algebraic reparameterization of an exact published feasibility condition is covered even though the source presents the region graphically rather than naming the cubic roots.

## value

FAIL

The boundary is a direct substitution/reparameterization of the source's exact normalization bound and exact optimizer, followed by routine monotone-cubic algebra. The factor-16 and d=255/17 examples are useful annotations but do not add a motivated structural lemma, new physical obstruction, or nonmechanical classification beyond the already-defined feasible region. The user standard explicitly rejects textbook substitutions and tiny algebraic restatements even when correct.

The dated certificate retains the supplied scientific assessment, sources and limitations.
