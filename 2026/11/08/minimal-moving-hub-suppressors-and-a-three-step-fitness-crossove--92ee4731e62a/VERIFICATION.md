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

# Verification and scope

Run `python3 verify.py` with the standard Python library. It re-derives the exact fixation probability from the two explicit 8-state parent-reproduction transition matrices at each tested rational fitness. For each block length, the checked number of distinct positive integer fitness values strictly exceeds the proved maximum degree of the cross-multiplied rational-function identity. Hence those tests certify a polynomial identity for all real positive fitness values; this is logically stronger than sampling a function at isolated points. Additional checks establish the sign-polynomial factorizations and the three-step single-root reduction, and test the static-path identity by the same degree argument.

The verifier checks exactly 30, 58, 86 and 114 integer interpolation nodes for block lengths one through four, respectively, and 18 further integer nodes for the static path. Sign conclusions follow by coefficient positivity and monotonicity, not by discretized fitness scans. Coefficient arrays appear in `COEFFICIENTS.txt` and are embedded in `verify.py`.

Unproved scope: arbitrary block durations five or more, random switching, arbitrary within-phase starting times, other graphs, death–birth updating, state-dependent fitness, mutation, and external originality certification. This is a same-model mathematical and computational review only; no independent audit was performed.
