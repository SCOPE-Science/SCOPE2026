---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The frozen census is correct, but its eight-site witness read in increasing site order is false: 00111101 has preperiod 5 and eventual period 16. The replacement explicitly declares the orientation and gives all phases of the valid least-period-eight word 00101111; 000111 has least period nine. The replacement also distinguishes the 31 vertices after degree pruning from the 30 in cyclic SCCs. A separate graph build enumerated both side columns using the local constraints at each fixed middle column and ran SCCs without degree pruning; it reproduced every row at heights 1,2,3,4,5,8,9,10, with temporal periods measured on pairs of columns. Configurations fixed at height t give unique indexed cyclic walks and vice versa because the rule is deterministic. Each simple length-l component contributes l exactly when l divides n. Subtracting the appropriate proper-divisor fixed sets and dividing by the phase count proves C8 and C9. At height 10 every closed walk stays in an SCC with a common period dividing 2 or 5, so all such states are in Fix(F²) or Fix(F⁵); no extrapolation over n is used. The corrected limsup convention gives zero entropy for heights 8 and 9.

## originality

PASS

The repaired finding claims only the evaluated all-circumference census for primitive 8, 9 and 10 on labelled rings. Prior transfer-graph methods, separate lower heights, and individual glider witnesses are not claimed as novel.

## value

PASS

A complete short-return census in the standard Rule 110 model resolves three consecutive low periods without a spatial cutoff. It exhibits a natural contrast with exponential lower clocks, and a universal absence at 10 despite positive lower-divisor sectors. The arithmetic populations distinguish all ring sizes and are usable data, not a finite-size conjecture or an isolated witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
