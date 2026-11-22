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

# Reproducibility and checks

The package contains a standalone standard-library Python checker `verify.py`, the full character table in `character_table.csv`, and the actual pass output in `verification_output.txt`. Run `python3 verify.py` in a fresh directory containing these files; no Internet, nonstandard package, or third-party data is required. It verifies all eleven finite conjugacy cases by exact orbit construction, orbit-diameter filtering, incompatibility graph generation, and exhaustive memoized deletion recurrence at \(-1\). Two pivot tie-break orders agree on all computed values. Small-cube comparisons use separately generated orbit sets and direct independent-subset enumeration. The Specht projection calculates all eleven multiplicities and verifies the dimension sum \(253\); a separate exact 11-by-11 orthogonality check confirmed the character library.

The geometric fixed-locus identification, Lefschetz sign, rational quotient-invariants property, and representation projection are mathematical arguments stated in `RESULT.md`. Finite checks do not prove claims for untested dimensions; none are claimed. The \(64\)-vertex identity case may cache around four million subsets and require significant RAM. Complete proof validation and independent originality assessment have not been performed by a separate mathematical reviewer.
