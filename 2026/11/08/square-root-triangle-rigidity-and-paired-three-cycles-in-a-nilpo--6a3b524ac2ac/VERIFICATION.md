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

Direct differentiation yields pointwise trace(J)=det(J)=tr(J²)=0 and hence nilpotence. On a periodic orbit, z_i=Ax_i², so h_{i+1}=A(x_i-x_{i+1})² and x_{i+1}=P(h_i). For three indices this says the heights are precisely A times the three pairwise squared differences of real q_i=P(h_i). Distinct heights exclude zero and real line triangle distances satisfy max=sum of other two after square roots. Conversely interpolation q(r²)=0,q(s²)=(r+s)/sqrt A,q((r+s)²)=s/sqrt A gives a genuine degree-2 polynomial and both opposite cyclic height orders; coordinate reconstruction is exact. Direct substitution verifies the two rational example cycles and the reversal is not a rotation.

## originality

PASS

Castañeda–Rebollo-Perdomo and Chamberland prove existence via repeated-coordinate three-cycles, not a classification of the three-distinct-height stratum or a converse realizing every positive triangle triple. A same-day fixed quadratic family develops two symmetry-breaking three-cycles at a sharp parameter threshold, a restricted subclass rather than a theorem covering every P and every admissible triple.

## value

PASS

The original nilpotent-Jacobian dynamics literature asks whether three-cycles are unique. The square-root distance obstruction and exact converse give a complete natural missing orbit stratum and paired rational counterexamples, rather than an arbitrary slice or computational curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
