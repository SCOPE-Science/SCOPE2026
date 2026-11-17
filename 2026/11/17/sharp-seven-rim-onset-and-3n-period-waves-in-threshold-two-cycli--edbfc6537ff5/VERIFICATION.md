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

# Verification methods and limits

Run with standard Python 3 (no third-party packages):

`python3 exhaustive_finite.py`

`python3 independent_checks.py`

The expected complete stdout files are `exhaustive_output.txt` and `independent_output.txt`. The first script builds the complete functional graph on every labelled three-colour state for rim sizes three through seven. The second checks the same eventual periods by an independently encoded transition and Floyd's cycle detection, as well as checking all fixed states through size nine and the constructive three-step wave through size 120. It also checks the exact return period directly through size 20.

**Verified finite conclusions:** no nontrivial cycles for rim sizes three through six; rim size seven has exactly 27 fixed points, two primitive 21-cycles, 168 initial states entering those cycles, and 6,393 entering fixed points. The full counts for each smaller state space are in the output files.

**Scope boundary:** finite checks do not prove the unbounded-period construction. The general proof is the symbolic three-step update calculation, cyclic-shift equivariance, and primitive rotational symmetry argument in `RESULT.md`. There is no independent expert proof, no complete large-size orbit classification, and no evidence for a universal transient bound.
