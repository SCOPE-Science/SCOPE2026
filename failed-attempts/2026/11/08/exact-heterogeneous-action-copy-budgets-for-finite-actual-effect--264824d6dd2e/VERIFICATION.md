---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

As a universal guarantee, the iff is correct. A frame on r states with one neighborhood equal to the whole state set for every agent forces at least r completions of any fixed action. For sufficiency, choose a largest copy coordinate k. With x_k fixed the mixed-modulus map is a product of translations; with x_i fixed for i≠k, one can prescribe the target residue modulo m_i by choosing x_k, then uniquely set the other residues by choosing their own labels. This proves slice surjectivity even when some m_i=1. Compose with a surjection onto the actual outcome set. For a prescribed outcome in a fixed action's neighborhood, each other agent can select a neighborhood containing that outcome by the common-union condition and choose copy labels to force it; the nonempty-intersection fallback never creates an outcome outside the fixed neighborhood. The inequality is not asserted to be necessary for each particular easier frame. The supplied checks/verify_budget.py was found and inspected, not executed; its reported finite checks are not the universal proof.

## originality

FAIL

The distinct October 18 indexed heterogeneous-budget theorem already gives the entire universal criterion and the same construction and obstruction. Replacing exactly r local outcomes by at most r and choosing one vector at every world yield the frozen statement by applying that earlier local theorem to each actual outcome count. This is demonstrated coverage, not an inference from a search score or from the cited uniform case.

## value

FAIL

The heterogeneous tradeoff is useful in its original formulation, but this record rederives the known complete feasible region by the same slice construction. Its at-most-r and fixed-vector formulations require only local substitution; the finite checks do not add a new exact invariant, strengthened theorem or meaningful instance-sensitive boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
