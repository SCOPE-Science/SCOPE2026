---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a directed union of left submodules over the stated field, basis elements of a finite-dimensional test space in Sym(M)#A involve finitely many polynomial variables. They all lie in one stage, and the stage's equivariant symmetric-algebra inclusion preserves the action and dimensions in its nonzero finite-dimensional Følner witness. Theorem 3.1 of Bartholdi, under the stated cocommutative Hopf hypotheses, supplies submodule, quotient and extension closure and hence finite direct sums; the zero module is extensively amenable as Sym(0)=k. An arbitrary sum is a quotient of a coproduct of extensively amenable submodules, so the largest submodule exists. Image closure gives functoriality; hereditary restriction is T(L)=L intersect T(M) for L contained in M, and the preimage of a nonzero extensively amenable submodule of M/T(M) contradicts maximality by extension closure. No computation is required. The theorem is correct; the claim in the prior-work paragraph that Bartholdi does not state arbitrary direct-sum closure is false. Also, arbitrary colimit closure is an immediate further consequence of coproduct and quotient closure, although not part of the Finding.

## originality

FAIL

The strongest matching primary source expressly proves the permanence statements, with the same finite-support argument. Localizing Serre is the definition of that list of closures in a module category, and the radical is its standard consequence. The absence of the two category-theoretic terms from the paper is not a mathematical gap.

## value

FAIL

The torsion-theoretic perspective can be useful terminology, but the claimed scientific increment is the same already published permanence plus textbook module-category deductions. No new characterization of the radical, construction in an example, or nonroutine structural property is established. No independently valuable remainder survives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
