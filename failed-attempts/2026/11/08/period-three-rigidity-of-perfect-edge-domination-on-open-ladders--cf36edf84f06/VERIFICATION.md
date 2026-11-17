---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

PASS: The exact 81-state W/Y/B color automaton is a complete local rephrasing of PEDS: an omitted edge requires endpoint selected degrees summing to one; selected edges can meet. The reachable/co-reachable intersection has the isolated BB loop plus a directed six-cycle with four permitted boundary phases, yielding z^{3n-2}+4z^n for n≡2 mod 3 and z^{3n-2}+2z^n otherwise. Six-step cyclic weight increment gives n for proper sets. Independently enumerated every edge subset for n=2..7, recovering (4,2,2,4,2,2) proper sets of size n plus the full edge set; the finite-state argument (not small n) supplies the all-n extension. The no-DIM conclusion follows because every nontrivial pattern has incident selected edges. The generated open-ladder source checker was read, not relied on as a standalone proof.

## originality

FAIL

FAIL: The complete formula, all-cardinality rigidity, phase counts, lack of dominating induced matchings, and complete transition classification were *already publicly established* in Resultary's October 26 open-and-circular ladder paper and repeated in its November 2 open-ladder theorem. This is exact statement-level coverage, not a similarity of titles. A different 81-state coloring and six-cycle presentation versus prior 64-state bit automata is merely an equivalent finite-state encoding and yields no new final scientific claim.

## value

FAIL

FAIL: The complete formula, six-cycle rigidity, n-edge proper-set count, and no efficient edge domination are all direct repeats of earlier fully proved open-ladder results. The alternative automaton is a recomputation of a known table with no motivated new invariant or sharper boundary. Correctness and independent finite verification do not make this repetition valuable as a new research finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
