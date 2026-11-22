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

# Reproducible checks

All scripts require only standard-library Python 3 and run within this directory:

```
python3 verify.py
python3 check_independent.py
```

The first program exhaustively follows 277633 configurations, for ring lengths 3–11 at two colors, 3–10 at three colors, 3–8 at four colors, and 3–7 at five colors. It checks the first-entry cutoff and exact recurrent classification, and constructs independently the pair-state adjacency matrix to compare its traces with the closed formulas. The second program independently tabulates all three plurality ballots on 131924 configurations and checks the sharp transient witness for lengths 3 through 29. Their recorded outputs are `verify.log` and `check_independent.log`. No randomized sample or extrapolation is presented as proof.

The arbitrary-length proof in RESULT.md uses strictly decreasing singleton counts and an exact rank-\(2q\) transfer-matrix compression. Code cannot validate the nonstandard run-persistence and spectral-reduction arguments for all inputs and lengths; these are demonstrated mathematically in the proof. There has been no external or independent scientific audit.
