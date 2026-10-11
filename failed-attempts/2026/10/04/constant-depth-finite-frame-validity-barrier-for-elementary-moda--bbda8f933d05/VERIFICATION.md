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

Takahashi's finite-reduction step supplies, for a finitely axiomatizable elementary modal logic, one fixed first-order sentence that agrees with the finite validating frames. On the labeled universe \([n]\), a fixed first-order sentence is evaluated by a constant-depth polynomial-size unbounded-fan-in circuit: relation atoms read adjacency bits, equality is hardwired, Boolean connectives add constant depth, and each quantifier expands to one unbounded AND/OR over \([n]\). Because the sentence, variable width, and quantifier nesting are fixed, the resulting family is nonuniform \(\mathsf{AC}^0\). The contrapositive and the parity-hardness corollary then follow from closure under composition and the classical parity lower bound.

## originality

FAIL

The scientific statement is mechanically implied by two pre-existing ingredients: Takahashi's fixed first-order description of the finite validating frames and the standard theorem/construction placing fixed first-order model checking in \(\mathsf{AC}^0\). Under implication-based originality, the fact that Takahashi phrases his advertised complexity consequence only as membership in P does not make the stronger AC0 corollary independent. The parity obstruction is then the standard composition with parity \(\notin\mathsf{AC}^0\).

## value

PASS

Although not original, the sharpened formulation is mathematically useful: it replaces a conditional P-versus-NP obstruction by a much stronger fixed-circuit upper bound, making unconditional circuit lower bounds such as parity reductions available as elementarity obstructions. The representation caveat is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
