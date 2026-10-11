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

The source Hamiltonians imply that classical-field segments preserve cavity photon number, whereas each quantum-field segment preserves total excitation and the qutrit can carry at most two excitations. Thus after k quantum segments, starting from vacuum, cavity support is bounded by photon number 2k. Since \(|N,g\rangle\) is an admissible target, k must be at least \(\lceil N/2\rceil\). Luo--Yu's construction processes the pairs \((N,N-1),(N-2,N-3),\ldots\) and uses exactly that many quantum segments, including the odd singleton. An independent support-closure calculation through k=10 reproduced the 2k bound.

## originality

FAIL

The defining Luo--Yu paper already states the exact conservation properties, explicitly organizes each quantum step to process two adjacent excitation blocks in parallel, and advertises the resulting factor-two reduction in the number of evolution steps. The claimed lower bound is the immediate capacity consequence that one qutrit-assisted quantum segment can raise reachable cavity support by at most two. Combining that one-line conservation bound with the published construction mechanically yields \(\lceil N/2\rceil\). Under the audit rule, this is implication-level covered even though the source does not label it an optimality theorem.

## value

FAIL

Architecture-level optimality is a motivated question, but here the result adds only the routine observation that a three-level ancilla can transfer at most two excitation units per quantum segment to a construction already described as advancing two blocks per step. It does not expose a hidden obstruction, new control invariant, or nontrivial boundary beyond the source's advertised resource mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
