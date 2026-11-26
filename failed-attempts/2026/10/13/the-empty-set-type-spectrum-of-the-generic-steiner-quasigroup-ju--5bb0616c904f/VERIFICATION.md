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

In the pure single-operation language completeness gives the sole 0-type. Idempotence reduces every one-variable term to that variable, so QE gives exactly one 1-type. If x≠y, then z=x·y is distinct from both by the Steiner inverse identity and commutativity; x·z=y and y·z=x. Together with idempotence this closes the three normal forms and determines all atomic equalities. If x=y every term reduces to x instead. Both equality patterns are realized (the published theorem already guarantees a nontrivial model); QE gives exactly two complete 2-types. Barbina–Casanovas Theorem 3.3 supplies continuum many complete empty-set 3-types of this very theory. For n>3 the tuple obtained by repeating the first variable induces an injection of the complete 3-type space, and a countable language has only countably many formulas in the given finite tuple, giving the matching upper bound. Read the frozen VERIFICATION.md and verify.py without running the script: the finite example checks the table on three elements, not QE, the continuum lower bound, or the universal inference from the identities.

## originality

FAIL

Covered as an immediate corollary, not shown to have appeared verbatim. The cited primary source already resolves the only non-elementary step by proving continuum many complete 3-types in the exact theory and quantifier elimination in the exact signature. The remaining arities follow from elementary normal forms and generalities about type spaces, with no distinct substantive claim proved.

## value

FAIL

The sequence is a correct explanatory corollary, but the record adds no new model-theoretic structure or independently motivated unknown exact invariant. The exact first arity is mechanically fixed by the published 3-type result and the elementary one- and two-generator closure calculation. Recording the already determined sequence is not a substantive scientific addition under the value criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
